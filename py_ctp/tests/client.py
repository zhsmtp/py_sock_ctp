
import json
import time
import ctypes

from py_ctp.py_sock_ctp import Py_sock_ctp
from py_ctp.py_ctp_mdapi import CThostFtdcMdApi, CThostFtdcMdSpi
from py_ctp.py_ctp_struct import CThostFtdcReqUserLoginField, CThostFtdcDepthMarketDataField, CThostFtdcRspUserLoginField, CThostFtdcRspInfoField


class MyMdSpi(CThostFtdcMdSpi):
    def SetApi(self, api):
        self.api = api

    def OnRtnDepthMarketData(self, pDepthMarketData: CThostFtdcDepthMarketDataField):
        print(pDepthMarketData.InstrumentID, ' price=', pDepthMarketData.LastPrice,
              'at', pDepthMarketData.UpdateTime, pDepthMarketData.UpdateMillisec)

    def OnFrontConnected(self):
        print('OnFrontConnected')
        pReqUserLoginField = CThostFtdcReqUserLoginField()
        self.api.ReqUserLogin(pReqUserLoginField, 1)

    def OnRspUserLogin(self, pRspUserLogin: CThostFtdcRspUserLoginField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        print('OnRspUserLogin: login, trading day is', pRspUserLogin.TradingDay)
        print('OnRspUserLogin: ErrorID=', pRspInfo.ErrorID,
              'ErrorMsg=', pRspInfo.ErrorMsg)


if __name__ == "__main__":
    sock = Py_sock_ctp(ctp_port=50007)
    sock.open()
    md_api = CThostFtdcMdApi.CreateFtdcMdApi('.', False, False, sock)
    print('trading day before login:', md_api.GetTradingDay())

    md_spi = MyMdSpi(sock)
    print(md_spi.ptr_spi)
    md_spi.SetApi(md_api)
    md_api.RegisterSpi(md_spi.ptr_spi)
    md_api.RegisterFront('tcp://180.168.146.187:10111')
    print('---------->Init()')
    md_api.Init()
    time.sleep(3)
    print('---------->SubscribeMarketData()')
    md_api.SubscribeMarketData(['fu2009', 'rb2010', 'MA2009'], 3)

    print('10s 之后关闭')
    time.sleep(10)
    md_api.Release()
    sock.close()
    md_spi = None
