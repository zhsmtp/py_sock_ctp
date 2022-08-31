import socket
import json
import struct
# import multiprocessing
import threading
import queue

import ctypes
import binascii

class Py_sock_ctp:
    '''
    sock, client, for sending req
    sock2, server, for receving rsp, a Thread will do it
    '''
    def __init__(self, ctp_port=50007, listen_rsp_fun=[]):
        self.ctp_port = ctp_port
        self.listen_rsp_fun = listen_rsp_fun

        # 打开cpp_ctp库，连接50007端口，创建socket
        # export LD_LIBRARY_PATH=.:./server/ctp_api_6.5.1_20200908/linux64/:$LD_LIBRARY_PATH
        # echo $LD_LIBRARY_PATH
        # set PATH=.;.\server\ctp_api_6.5.1_20200908\win64\;%PATH%
        self.cpp_ctp_dll = ctypes.cdll.LoadLibrary('cpp_ctp')
        self.cpp_ctp_dll_start = self.cpp_ctp_dll.start
        self.cpp_ctp_dll_start.restype = ctypes.c_void_p
        self.cpp_ctp_dll_stop = self.cpp_ctp_dll.stop
        self.cpp_ctp_dll_stop.argtypes = [ctypes.c_void_p]
        self.cpp_ctp_ptr = None

        self.is_open = False
        self.listen_rsp_running = False

        self.sock = None
        self.sock_accepted = threading.Condition()
        self.sock_stopped = threading.Condition()
        self.send_lock = threading.Lock() #multiprocessing.Lock()
        self.sock_addr = None
        self.server_sock = None # 监听 ctp_port，返回 sock
        
        self.listen_thread = None
        self.start_cpp_ctp_thread = None


        self.ret_dict = None                        #dict, 键值是req_id, 值是 Condition变量和返回值的tuple
        self.res_ret_json_payload_queue = None      #queue

    def open(self):
        if not self.is_open:
            self.ret_dict = dict()
            self.res_ret_json_payload_queue = queue.Queue()

            # 创建server socket，监听ctp_port端口
            self.server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.server_sock.bind(('localhost', self.ctp_port))
            
            # self.listen_thread = multiprocessing.Process(target=self.listen_rsp_ret)
            self.listen_thread = threading.Thread(target=self.listen_rsp_ret)
            self.listen_thread.start()

            self.start_cpp_ctp_thread = threading.Thread(target=self.start_cpp_ctp)
            self.start_cpp_ctp_thread.start()            

            self.listen_rsp_running = True

            with self.sock_accepted:
                self.sock_accepted.wait()

            
            
    def close(self):
        self.listen_rsp_running = False
        
        if self.sock:
            self.sock.settimeout(1)
            with self.sock_stopped:
                self.sock_stopped.wait(2)
            self.sock.shutdown(socket.SHUT_RDWR)
            self.sock.close()
            self.sock = None
        if self.server_sock:
            self.server_sock.close()
            self.server_sock = None
        if self.listen_thread:
            self.listen_thread.join()
        self.listen_thread = None
        self.listen_rsp_fun.clear()

        self.cpp_ctp_dll_stop(self.cpp_ctp_ptr)
        self.cpp_ctp_ptr = None

        self.is_open = False
        print(f'Py_sock_ctp({self.ctp_port}) all closed.')

    def add_listen_rsp_fun(self, listen_rsp_fun):
        if listen_rsp_fun not in self.listen_rsp_fun:
            self.listen_rsp_fun.append(listen_rsp_fun)
    
    def remove_listen_rsp_fun(self, listen_rsp_fun):
        if listen_rsp_fun in self.listen_rsp_fun:
            self.listen_rsp_fun.remove(listen_rsp_fun)

    def send_req(self, req_dict):
        req = json.dumps(req_dict)
        ret_value = None
        if self.sock:
            '''
            发送request
            req = {'req_id':uuid.uuid4(),'cmd':'ReqUserLogin','cmd_type':'md','ptr':self.api_ptr,'pReqUserLoginField':vars(pReqUserLoginField),'nRequestID':nRequestID}
            payload格式：
            req len,  8 bytes
            req data, len bytes
            crc32,    4 bytes
            '''
            req_payload = struct.pack('Q', len(req))
            req_payload += str.encode(req)
            req_payload += struct.pack('I', binascii.crc32(req_payload))

            if 'req_id' in req_dict:
                # has return value                
                cond = threading.Condition() # multiprocessing.Condition()
                self.ret_dict[req_dict['req_id']] = cond
                with cond:
                    with self.send_lock:
                        self.sock.sendall(req_payload) # 放在这里防止C++太快，导致还没等待就收完了造成的卡死。。。
                    cond.wait()
                try:
                    ret_value = self.ret_dict.pop(req_dict['req_id'])
                except:
                    pass
            else:
                with self.send_lock:
                    self.sock.sendall(req_payload) 
        return ret_value

    def recv_rsp_ret(self):
        '''
        接收数据，检查crc32，最后把json字符串转化成dict
        '''
        res_ret_payload = None
        if self.listen_rsp_running:
            try:
                if self.sock:
                    if self.sock._closed:
                        return None
                    # 1. 接收8字节的长度数据
                    recv_from_cpp = self.myreceive(8)
                    recv_size = int(struct.unpack('Q', recv_from_cpp)[0])
                    if recv_size == 0:
                        return None
                    # 2. 根据长度，接收json字符串
                    res_ret_payload = self.myreceive(recv_size)
                    recv_from_cpp += res_ret_payload
                    # 3. 计算crc
                    calculated_crc = binascii.crc32(recv_from_cpp)
                    # 4. 接收4字节的crc，如果crc匹配，则返回str类型的json字符串
                    payload_crc = int(struct.unpack('I', self.sock.recv(4))[0])
                    if calculated_crc == payload_crc:
                        # print('recv_rsp_ret: received res_ret_payload = ', res_ret_payload)
                        res_ret_payload = json.loads(res_ret_payload)
                    else:
                        print('recv_rsp_ret: bad rsp, crc32 is wrong!!!!!!')
                        return None
            except TypeError:
                pass
            except Exception: # struct.error and 
                # print('recv_rsp_ret():', e)
                return None            
        return res_ret_payload

    def myreceive(self, req_size):
        chunk = b''
        chunks = []
        bytes_recd = 0

        if self.sock:
            if self.sock._closed:
                return None
            while bytes_recd < req_size:
                try:
                    chunk = self.sock.recv(min(req_size - bytes_recd, 2048))
                except socket.timeout:
                    # 如果超时，直接返回，不报错
                    return None
                except OSError:
                    pass # [WinError 10038] 在一个非套接字上尝试了一个操作。
                except Exception:
                    # 其他错误，报错
                    # print(f'myreceive({req_size}) {type(e)} :', e)
                    return None
                # if chunk == b'':
                #     raise RuntimeError("socket connection broken")
                chunks.append(chunk)
                bytes_recd = bytes_recd + len(chunk)
            return b''.join(chunks)
    
    def start_cpp_ctp(self):
        self.cpp_ctp_ptr = self.cpp_ctp_dll_start(self.ctp_port)

    def listen_rsp_ret(self):
        self.server_sock.listen(1)
        self.sock, self.sock_addr = self.server_sock.accept()
        with self.sock_accepted:
            self.sock_accepted.notify_all()

        # self.sock.settimeout(1)
        self.is_open = True
        print(f'py_sock_ctp({self.ctp_port}) <-----> cpp_ctp ({self.sock_addr}), connected!')
        while self.listen_rsp_running:
            try:
                res_ret = self.recv_rsp_ret()
                if res_ret:
                    if 'req_id' in res_ret:
                        # 只有return才有req_id值
                        if res_ret['req_id'] in self.ret_dict:
                            cond = self.ret_dict[res_ret['req_id']]
                            with cond:
                                self.ret_dict[res_ret['req_id']] = res_ret['value']
                                cond.notify_all()
                    else:
                        for listener in self.listen_rsp_fun:
                            listener(res_ret)
            except Exception as e:
                print('listen_rsp_ret error:', e)
        print(f'py listen_rsp_ret ({self.ctp_port}) stopped!')
        with self.sock_stopped:
            self.sock_stopped.notify_all()