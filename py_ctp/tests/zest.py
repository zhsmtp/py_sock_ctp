import json
import uuid
import time
from py_ctp.py_sock_ctp import Py_sock_ctp
from py_ctp.py_ctp_mdapi import CThostFtdcMdApi, CThostFtdcMdSpi
from py_ctp.py_ctp_tdapi import CThostFtdcTraderApi, CThostFtdcTraderSpi

if __name__ == '__main__':
    for i in range(10):
        print(f'---------{i}----------------')
        pys = Py_sock_ctp(ctp_port=50010+i)

        pys.open()

        mdApi1 = CThostFtdcMdApi.CreateFtdcMdApi('conData/md/', False, False, pys)

        print('mdApi1 @', mdApi1.api_ptr)
        mdSpi1 = CThostFtdcMdSpi(pys)
        print('mdSpi1 @', mdSpi1.ptr_spi)
        mdApi1.RegisterSpi(mdSpi1.ptr_spi)
        mdApi2 = CThostFtdcMdApi.CreateFtdcMdApi('conData/md/', False, False, pys)
        print('mdApi2 @', mdApi2.api_ptr)
        mdSpi2 = CThostFtdcMdSpi(pys)
        print('mdSpi2 @', mdSpi2.ptr_spi)
        mdApi2.RegisterSpi(mdSpi2.ptr_spi)

        mdApi3 = CThostFtdcMdApi.CreateFtdcMdApi('conData/md/', False, False, pys)
        print('mdApi3 @', mdApi3.api_ptr)
        mdSpi3 = CThostFtdcMdSpi(pys)  
        print('mdSpi3 @', mdSpi3.ptr_spi)  
        mdApi3.RegisterSpi(mdSpi3.ptr_spi)
        

        tdApi1 = CThostFtdcTraderApi.CreateFtdcTraderApi('conData/td/', pys)
        tdApi2 = CThostFtdcTraderApi.CreateFtdcTraderApi('conData/td/', pys)
        tdApi3 = CThostFtdcTraderApi.CreateFtdcTraderApi('conData/td/', pys)
        tdSpi1 = CThostFtdcTraderSpi(pys)
        tdSpi2 = CThostFtdcTraderSpi(pys)
        tdSpi3 = CThostFtdcTraderSpi(pys)
        tdApi1.RegisterSpi(tdSpi1.ptr_spi)
        tdApi2.RegisterSpi(tdSpi2.ptr_spi)
        tdApi3.RegisterSpi(tdSpi3.ptr_spi)
        print('tdApi1 @', tdApi1.api_ptr)
        print('tdApi2 @', tdApi2.api_ptr)
        print('tdApi3 @', tdApi3.api_ptr)
        print('tdSpi1 @', tdSpi1.ptr_spi)
        print('tdSpi2 @', tdSpi2.ptr_spi)
        print('tdSpi3 @', tdSpi3.ptr_spi)
        print('wait 1s')
        time.sleep(1)

        # print(req_ret)
        pys.close()
        pys = None
        print('close and wait 1s')
        time.sleep(1)
        print('bye')

        