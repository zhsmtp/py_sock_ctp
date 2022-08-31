import json
import uuid
import time
import threading
import os
import shutil

from py_ctp.py_sock_ctp import Py_sock_ctp
from py_ctp.py_ctp_mdapi import CThostFtdcMdApi, CThostFtdcMdSpi
from py_ctp.py_ctp_tdapi import CThostFtdcTraderApi, CThostFtdcTraderSpi

def run_test(port_num):
    print(port_num)
    pys = Py_sock_ctp(ctp_port=port_num)

    pys.open()

    tdConPath = os.path.join('.', 'conData', 'td', str(port_num))+os.sep
    if not os.path.isdir(tdConPath):
        os.makedirs(tdConPath)
    mdConPath = os.path.join('.', 'conData', 'md', str(port_num))+os.sep
    if not os.path.isdir(mdConPath):
        os.makedirs(mdConPath)

    mdApi1 = CThostFtdcMdApi.CreateFtdcMdApi(mdConPath, False, False, pys)

    print(port_num, 'mdApi1 @', mdApi1.api_ptr)
    mdSpi1 = CThostFtdcMdSpi(pys)
    print(port_num, 'mdSpi1 @', mdSpi1.ptr_spi)
    mdApi1.RegisterSpi(mdSpi1.ptr_spi)
    mdApi2 = CThostFtdcMdApi.CreateFtdcMdApi(mdConPath, False, False, pys)
    print(port_num, 'mdApi2 @', mdApi2.api_ptr)
    mdSpi2 = CThostFtdcMdSpi(pys)
    print(port_num, 'mdSpi2 @', mdSpi2.ptr_spi)
    mdApi2.RegisterSpi(mdSpi2.ptr_spi)

    mdApi3 = CThostFtdcMdApi.CreateFtdcMdApi(mdConPath, False, False, pys)
    print(port_num, 'mdApi3 @', mdApi3.api_ptr)
    mdSpi3 = CThostFtdcMdSpi(pys)  
    print(port_num, 'mdSpi3 @', mdSpi3.ptr_spi)  
    mdApi3.RegisterSpi(mdSpi3.ptr_spi)
    
    tdApi1 = CThostFtdcTraderApi.CreateFtdcTraderApi(tdConPath, pys)
    tdApi2 = CThostFtdcTraderApi.CreateFtdcTraderApi(tdConPath, pys)
    tdApi3 = CThostFtdcTraderApi.CreateFtdcTraderApi(tdConPath, pys)
    tdSpi1 = CThostFtdcTraderSpi(pys)
    tdSpi2 = CThostFtdcTraderSpi(pys)
    tdSpi3 = CThostFtdcTraderSpi(pys)
    tdApi1.RegisterSpi(tdSpi1.ptr_spi)
    tdApi2.RegisterSpi(tdSpi2.ptr_spi)
    tdApi3.RegisterSpi(tdSpi3.ptr_spi)
    print(port_num, 'tdApi1 @', tdApi1.api_ptr)
    print(port_num, 'tdApi2 @', tdApi2.api_ptr)
    print(port_num, 'tdApi3 @', tdApi3.api_ptr)
    print(port_num, 'tdSpi1 @', tdSpi1.ptr_spi)
    print(port_num, 'tdSpi2 @', tdSpi2.ptr_spi)
    print(port_num, 'tdSpi3 @', tdSpi3.ptr_spi)

    print(port_num, 'wait 1s')
    time.sleep(1)

    # print(req_ret)
    pys.close()
    pys = None
    print(port_num, 'close and wait 1s')
    time.sleep(1)
    if os.path.isdir(tdConPath):
        shutil.rmtree(tdConPath)
    if os.path.isdir(mdConPath):
        shutil.rmtree(mdConPath)
    print(port_num, 'bye')

if __name__ == '__main__':
    for i in range(5):
        t = threading.Thread(target=run_test, args=[50010+i])
        t.start()

        

        