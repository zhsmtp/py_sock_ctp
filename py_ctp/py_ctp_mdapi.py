import json
import uuid
from .py_sock_ctp import Py_sock_ctp
from .py_ctp_struct import (CThostFtdcRspUserLoginField,
        CThostFtdcRspInfoField,
        CThostFtdcUserLogoutField,
        CThostFtdcRspInfoField,
        CThostFtdcMulticastInstrumentField,
        CThostFtdcRspInfoField,
        CThostFtdcRspInfoField,
        CThostFtdcSpecificInstrumentField,
        CThostFtdcRspInfoField,
        CThostFtdcSpecificInstrumentField,
        CThostFtdcRspInfoField,
        CThostFtdcSpecificInstrumentField,
        CThostFtdcRspInfoField,
        CThostFtdcSpecificInstrumentField,
        CThostFtdcRspInfoField,
        CThostFtdcDepthMarketDataField,
        CThostFtdcForQuoteRspField,
        CThostFtdcFensUserInfoField,
        CThostFtdcReqUserLoginField,
        CThostFtdcUserLogoutField,
        CThostFtdcQryMulticastInstrumentField)

class CThostFtdcMdSpi:
    def __init__(self, sock_client):
        self.sock_client = sock_client
        #1) send socket cmd let cpp_ctp to create a spi class object. 2)cpp_ctp return the new spi object pointer.
        self.sock_client.add_listen_rsp_fun(self.rsp_handler)
        req = {'req_id':str(uuid.uuid4()),'cmd':'create_spi','cmd_type':'md','ptr':None}
        self.ptr_spi = int(self.sock_client.send_req(req))

    def __del__(self):
        if self.sock_client:
            self.sock_client.remove_listen_rsp_fun(self.rsp_handler)

    def OnFrontConnected(self):
        pass
    def OnFrontDisconnected(self, nReason:int):
        pass
    def OnHeartBeatWarning(self, nTimeLapse:int):
        pass
    def OnRspUserLogin(self, pRspUserLogin:CThostFtdcRspUserLoginField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        pass
    def OnRspUserLogout(self, pUserLogout:CThostFtdcUserLogoutField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        pass
    def OnRspQryMulticastInstrument(self, pMulticastInstrument:CThostFtdcMulticastInstrumentField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        pass
    def OnRspError(self, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        pass
    def OnRspSubMarketData(self, pSpecificInstrument:CThostFtdcSpecificInstrumentField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        pass
    def OnRspUnSubMarketData(self, pSpecificInstrument:CThostFtdcSpecificInstrumentField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        pass
    def OnRspSubForQuoteRsp(self, pSpecificInstrument:CThostFtdcSpecificInstrumentField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        pass
    def OnRspUnSubForQuoteRsp(self, pSpecificInstrument:CThostFtdcSpecificInstrumentField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        pass
    def OnRtnDepthMarketData(self, pDepthMarketData:CThostFtdcDepthMarketDataField):
        pass
    def OnRtnForQuoteRsp(self, pForQuoteRsp:CThostFtdcForQuoteRspField):
        pass
    def rsp_handler(self, rsp):
        rsp_cmd_type = rsp['cmd_type']
        if rsp_cmd_type != 'md':
            return
        # find method
        m = rsp['cmd']
        if m in dir(self):
            rsp_method = getattr(self, m)
        else:
            return
        # call method
        if 'On' not in m:
            return
        elif m == 'OnFrontConnected':
            rsp_method()
        elif m == 'OnFrontDisconnected':
            rsp_method(rsp['nReason'])
        elif m == 'OnHeartBeatWarning':
            rsp_method(rsp['nTimeLapse'])
        elif m == 'OnRspUserLogin':
            rsp_method(CThostFtdcRspUserLoginField(rsp['pRspUserLogin']), CThostFtdcRspInfoField(rsp['pRspInfo']), rsp['nRequestID'], rsp['bIsLast'])
        elif m == 'OnRspUserLogout':
            rsp_method(CThostFtdcUserLogoutField(rsp['pUserLogout']), CThostFtdcRspInfoField(rsp['pRspInfo']), rsp['nRequestID'], rsp['bIsLast'])
        elif m == 'OnRspQryMulticastInstrument':
            rsp_method(CThostFtdcMulticastInstrumentField(rsp['pMulticastInstrument']), CThostFtdcRspInfoField(rsp['pRspInfo']), rsp['nRequestID'], rsp['bIsLast'])
        elif m == 'OnRspError':
            rsp_method(CThostFtdcRspInfoField(rsp['pRspInfo']), rsp['nRequestID'], rsp['bIsLast'])
        elif m == 'OnRspSubMarketData':
            rsp_method(CThostFtdcSpecificInstrumentField(rsp['pSpecificInstrument']), CThostFtdcRspInfoField(rsp['pRspInfo']), rsp['nRequestID'], rsp['bIsLast'])
        elif m == 'OnRspUnSubMarketData':
            rsp_method(CThostFtdcSpecificInstrumentField(rsp['pSpecificInstrument']), CThostFtdcRspInfoField(rsp['pRspInfo']), rsp['nRequestID'], rsp['bIsLast'])
        elif m == 'OnRspSubForQuoteRsp':
            rsp_method(CThostFtdcSpecificInstrumentField(rsp['pSpecificInstrument']), CThostFtdcRspInfoField(rsp['pRspInfo']), rsp['nRequestID'], rsp['bIsLast'])
        elif m == 'OnRspUnSubForQuoteRsp':
            rsp_method(CThostFtdcSpecificInstrumentField(rsp['pSpecificInstrument']), CThostFtdcRspInfoField(rsp['pRspInfo']), rsp['nRequestID'], rsp['bIsLast'])
        elif m == 'OnRtnDepthMarketData':
            rsp_method(CThostFtdcDepthMarketDataField(rsp['pDepthMarketData']))
        elif m == 'OnRtnForQuoteRsp':
            rsp_method(CThostFtdcForQuoteRspField(rsp['pForQuoteRsp']))

class CThostFtdcMdApi:
    def __init__(self, api_ptr, sock_client):
        self.api_ptr = api_ptr
        self.sock_client = sock_client

    @staticmethod
    def CreateFtdcMdApi(pszFlowPath:str,bIsUsingUdp: bool,bIsMulticast: bool,sock_client:Py_sock_ctp):
        req = {'req_id':str(uuid.uuid4()),'cmd':'CreateFtdcMdApi','cmd_type':'md','ptr':None,'pszFlowPath':pszFlowPath,'bIsUsingUdp':bIsUsingUdp,'bIsMulticast':bIsMulticast}
        req_ret = sock_client.send_req(req)
        return CThostFtdcMdApi(int(req_ret), sock_client)
    @staticmethod
    def GetApiVersion(sock_client:Py_sock_ctp):
        req = {'req_id':str(uuid.uuid4()),'cmd':'GetApiVersion','cmd_type':'md','ptr':None}
        req_ret = sock_client.send_req(req)
        return req_ret
    def Release(self):
        req = {'cmd':'Release','cmd_type':'md','ptr':self.api_ptr}
        self.sock_client.send_req(req)
    def Init(self):
        req = {'cmd':'Init','cmd_type':'md','ptr':self.api_ptr}
        self.sock_client.send_req(req)
    def Join(self):
        req = {'req_id':str(uuid.uuid4()),'cmd':'Join','cmd_type':'md','ptr':self.api_ptr}
        req_ret = self.sock_client.send_req(req)
        return req_ret
    def GetTradingDay(self):
        req = {'req_id':str(uuid.uuid4()),'cmd':'GetTradingDay','cmd_type':'md','ptr':self.api_ptr}
        req_ret = self.sock_client.send_req(req)
        return req_ret
    def RegisterFront(self,pszFrontAddress:str):
        req = {'cmd':'RegisterFront','cmd_type':'md','ptr':self.api_ptr,'pszFrontAddress':pszFrontAddress}
        self.sock_client.send_req(req)
    def RegisterNameServer(self,pszNsAddress:str):
        req = {'cmd':'RegisterNameServer','cmd_type':'md','ptr':self.api_ptr,'pszNsAddress':pszNsAddress}
        self.sock_client.send_req(req)
    def RegisterFensUserInfo(self,pFensUserInfo:CThostFtdcFensUserInfoField):
        req = {'cmd':'RegisterFensUserInfo','cmd_type':'md','ptr':self.api_ptr,'pFensUserInfo':vars(pFensUserInfo)}
        self.sock_client.send_req(req)
    def RegisterSpi(self,pSpi:CThostFtdcMdSpi):
        req = {'cmd':'RegisterSpi','cmd_type':'md','ptr':self.api_ptr,'pSpi':pSpi}
        self.sock_client.send_req(req)
    def SubscribeMarketData(self,ppInstrumentID:list,nCount:int):
        req = {'req_id':str(uuid.uuid4()),'cmd':'SubscribeMarketData','cmd_type':'md','ptr':self.api_ptr,'ppInstrumentID':ppInstrumentID,'nCount':nCount}
        req_ret = self.sock_client.send_req(req)
        return req_ret
    def UnSubscribeMarketData(self,ppInstrumentID:list,nCount:int):
        req = {'req_id':str(uuid.uuid4()),'cmd':'UnSubscribeMarketData','cmd_type':'md','ptr':self.api_ptr,'ppInstrumentID':ppInstrumentID,'nCount':nCount}
        req_ret = self.sock_client.send_req(req)
        return req_ret
    def SubscribeForQuoteRsp(self,ppInstrumentID:list,nCount:int):
        req = {'req_id':str(uuid.uuid4()),'cmd':'SubscribeForQuoteRsp','cmd_type':'md','ptr':self.api_ptr,'ppInstrumentID':ppInstrumentID,'nCount':nCount}
        req_ret = self.sock_client.send_req(req)
        return req_ret
    def UnSubscribeForQuoteRsp(self,ppInstrumentID:list,nCount:int):
        req = {'req_id':str(uuid.uuid4()),'cmd':'UnSubscribeForQuoteRsp','cmd_type':'md','ptr':self.api_ptr,'ppInstrumentID':ppInstrumentID,'nCount':nCount}
        req_ret = self.sock_client.send_req(req)
        return req_ret
    def ReqUserLogin(self,pReqUserLoginField:CThostFtdcReqUserLoginField,nRequestID:int):
        req = {'req_id':str(uuid.uuid4()),'cmd':'ReqUserLogin','cmd_type':'md','ptr':self.api_ptr,'pReqUserLoginField':vars(pReqUserLoginField),'nRequestID':nRequestID}
        req_ret = self.sock_client.send_req(req)
        return req_ret
    def ReqUserLogout(self,pUserLogout:CThostFtdcUserLogoutField,nRequestID:int):
        req = {'req_id':str(uuid.uuid4()),'cmd':'ReqUserLogout','cmd_type':'md','ptr':self.api_ptr,'pUserLogout':vars(pUserLogout),'nRequestID':nRequestID}
        req_ret = self.sock_client.send_req(req)
        return req_ret
    def ReqQryMulticastInstrument(self,pQryMulticastInstrument:CThostFtdcQryMulticastInstrumentField,nRequestID:int):
        req = {'req_id':str(uuid.uuid4()),'cmd':'ReqQryMulticastInstrument','cmd_type':'md','ptr':self.api_ptr,'pQryMulticastInstrument':vars(pQryMulticastInstrument),'nRequestID':nRequestID}
        req_ret = self.sock_client.send_req(req)
        return req_ret
