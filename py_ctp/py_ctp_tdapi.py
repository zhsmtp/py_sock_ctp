import json
import uuid
from .py_sock_ctp import Py_sock_ctp
from .py_ctp_struct import (CThostFtdcRspAuthenticateField,
        CThostFtdcRspInfoField,
        CThostFtdcRspUserLoginField,
        CThostFtdcRspInfoField,
        CThostFtdcUserLogoutField,
        CThostFtdcRspInfoField,
        CThostFtdcUserPasswordUpdateField,
        CThostFtdcRspInfoField,
        CThostFtdcTradingAccountPasswordUpdateField,
        CThostFtdcRspInfoField,
        CThostFtdcRspUserAuthMethodField,
        CThostFtdcRspInfoField,
        CThostFtdcRspGenUserCaptchaField,
        CThostFtdcRspInfoField,
        CThostFtdcRspGenUserTextField,
        CThostFtdcRspInfoField,
        CThostFtdcInputOrderField,
        CThostFtdcRspInfoField,
        CThostFtdcParkedOrderField,
        CThostFtdcRspInfoField,
        CThostFtdcParkedOrderActionField,
        CThostFtdcRspInfoField,
        CThostFtdcInputOrderActionField,
        CThostFtdcRspInfoField,
        CThostFtdcQryMaxOrderVolumeField,
        CThostFtdcRspInfoField,
        CThostFtdcSettlementInfoConfirmField,
        CThostFtdcRspInfoField,
        CThostFtdcRemoveParkedOrderField,
        CThostFtdcRspInfoField,
        CThostFtdcRemoveParkedOrderActionField,
        CThostFtdcRspInfoField,
        CThostFtdcInputExecOrderField,
        CThostFtdcRspInfoField,
        CThostFtdcInputExecOrderActionField,
        CThostFtdcRspInfoField,
        CThostFtdcInputForQuoteField,
        CThostFtdcRspInfoField,
        CThostFtdcInputQuoteField,
        CThostFtdcRspInfoField,
        CThostFtdcInputQuoteActionField,
        CThostFtdcRspInfoField,
        CThostFtdcInputBatchOrderActionField,
        CThostFtdcRspInfoField,
        CThostFtdcInputOptionSelfCloseField,
        CThostFtdcRspInfoField,
        CThostFtdcInputOptionSelfCloseActionField,
        CThostFtdcRspInfoField,
        CThostFtdcInputCombActionField,
        CThostFtdcRspInfoField,
        CThostFtdcOrderField,
        CThostFtdcRspInfoField,
        CThostFtdcTradeField,
        CThostFtdcRspInfoField,
        CThostFtdcInvestorPositionField,
        CThostFtdcRspInfoField,
        CThostFtdcTradingAccountField,
        CThostFtdcRspInfoField,
        CThostFtdcInvestorField,
        CThostFtdcRspInfoField,
        CThostFtdcTradingCodeField,
        CThostFtdcRspInfoField,
        CThostFtdcInstrumentMarginRateField,
        CThostFtdcRspInfoField,
        CThostFtdcInstrumentCommissionRateField,
        CThostFtdcRspInfoField,
        CThostFtdcExchangeField,
        CThostFtdcRspInfoField,
        CThostFtdcProductField,
        CThostFtdcRspInfoField,
        CThostFtdcInstrumentField,
        CThostFtdcRspInfoField,
        CThostFtdcDepthMarketDataField,
        CThostFtdcRspInfoField,
        CThostFtdcSettlementInfoField,
        CThostFtdcRspInfoField,
        CThostFtdcTransferBankField,
        CThostFtdcRspInfoField,
        CThostFtdcInvestorPositionDetailField,
        CThostFtdcRspInfoField,
        CThostFtdcNoticeField,
        CThostFtdcRspInfoField,
        CThostFtdcSettlementInfoConfirmField,
        CThostFtdcRspInfoField,
        CThostFtdcInvestorPositionCombineDetailField,
        CThostFtdcRspInfoField,
        CThostFtdcCFMMCTradingAccountKeyField,
        CThostFtdcRspInfoField,
        CThostFtdcEWarrantOffsetField,
        CThostFtdcRspInfoField,
        CThostFtdcInvestorProductGroupMarginField,
        CThostFtdcRspInfoField,
        CThostFtdcExchangeMarginRateField,
        CThostFtdcRspInfoField,
        CThostFtdcExchangeMarginRateAdjustField,
        CThostFtdcRspInfoField,
        CThostFtdcExchangeRateField,
        CThostFtdcRspInfoField,
        CThostFtdcSecAgentACIDMapField,
        CThostFtdcRspInfoField,
        CThostFtdcProductExchRateField,
        CThostFtdcRspInfoField,
        CThostFtdcProductGroupField,
        CThostFtdcRspInfoField,
        CThostFtdcMMInstrumentCommissionRateField,
        CThostFtdcRspInfoField,
        CThostFtdcMMOptionInstrCommRateField,
        CThostFtdcRspInfoField,
        CThostFtdcInstrumentOrderCommRateField,
        CThostFtdcRspInfoField,
        CThostFtdcTradingAccountField,
        CThostFtdcRspInfoField,
        CThostFtdcSecAgentCheckModeField,
        CThostFtdcRspInfoField,
        CThostFtdcSecAgentTradeInfoField,
        CThostFtdcRspInfoField,
        CThostFtdcOptionInstrTradeCostField,
        CThostFtdcRspInfoField,
        CThostFtdcOptionInstrCommRateField,
        CThostFtdcRspInfoField,
        CThostFtdcExecOrderField,
        CThostFtdcRspInfoField,
        CThostFtdcForQuoteField,
        CThostFtdcRspInfoField,
        CThostFtdcQuoteField,
        CThostFtdcRspInfoField,
        CThostFtdcOptionSelfCloseField,
        CThostFtdcRspInfoField,
        CThostFtdcInvestUnitField,
        CThostFtdcRspInfoField,
        CThostFtdcCombInstrumentGuardField,
        CThostFtdcRspInfoField,
        CThostFtdcCombActionField,
        CThostFtdcRspInfoField,
        CThostFtdcTransferSerialField,
        CThostFtdcRspInfoField,
        CThostFtdcAccountregisterField,
        CThostFtdcRspInfoField,
        CThostFtdcRspInfoField,
        CThostFtdcOrderField,
        CThostFtdcTradeField,
        CThostFtdcInputOrderField,
        CThostFtdcRspInfoField,
        CThostFtdcOrderActionField,
        CThostFtdcRspInfoField,
        CThostFtdcInstrumentStatusField,
        CThostFtdcBulletinField,
        CThostFtdcTradingNoticeInfoField,
        CThostFtdcErrorConditionalOrderField,
        CThostFtdcExecOrderField,
        CThostFtdcInputExecOrderField,
        CThostFtdcRspInfoField,
        CThostFtdcExecOrderActionField,
        CThostFtdcRspInfoField,
        CThostFtdcInputForQuoteField,
        CThostFtdcRspInfoField,
        CThostFtdcQuoteField,
        CThostFtdcInputQuoteField,
        CThostFtdcRspInfoField,
        CThostFtdcQuoteActionField,
        CThostFtdcRspInfoField,
        CThostFtdcForQuoteRspField,
        CThostFtdcCFMMCTradingAccountTokenField,
        CThostFtdcBatchOrderActionField,
        CThostFtdcRspInfoField,
        CThostFtdcOptionSelfCloseField,
        CThostFtdcInputOptionSelfCloseField,
        CThostFtdcRspInfoField,
        CThostFtdcOptionSelfCloseActionField,
        CThostFtdcRspInfoField,
        CThostFtdcCombActionField,
        CThostFtdcInputCombActionField,
        CThostFtdcRspInfoField,
        CThostFtdcContractBankField,
        CThostFtdcRspInfoField,
        CThostFtdcParkedOrderField,
        CThostFtdcRspInfoField,
        CThostFtdcParkedOrderActionField,
        CThostFtdcRspInfoField,
        CThostFtdcTradingNoticeField,
        CThostFtdcRspInfoField,
        CThostFtdcBrokerTradingParamsField,
        CThostFtdcRspInfoField,
        CThostFtdcBrokerTradingAlgosField,
        CThostFtdcRspInfoField,
        CThostFtdcQueryCFMMCTradingAccountTokenField,
        CThostFtdcRspInfoField,
        CThostFtdcRspTransferField,
        CThostFtdcRspTransferField,
        CThostFtdcRspRepealField,
        CThostFtdcRspRepealField,
        CThostFtdcRspTransferField,
        CThostFtdcRspTransferField,
        CThostFtdcRspRepealField,
        CThostFtdcRspRepealField,
        CThostFtdcNotifyQueryAccountField,
        CThostFtdcReqTransferField,
        CThostFtdcRspInfoField,
        CThostFtdcReqTransferField,
        CThostFtdcRspInfoField,
        CThostFtdcReqRepealField,
        CThostFtdcRspInfoField,
        CThostFtdcReqRepealField,
        CThostFtdcRspInfoField,
        CThostFtdcReqQueryAccountField,
        CThostFtdcRspInfoField,
        CThostFtdcRspRepealField,
        CThostFtdcRspRepealField,
        CThostFtdcReqTransferField,
        CThostFtdcRspInfoField,
        CThostFtdcReqTransferField,
        CThostFtdcRspInfoField,
        CThostFtdcReqQueryAccountField,
        CThostFtdcRspInfoField,
        CThostFtdcOpenAccountField,
        CThostFtdcCancelAccountField,
        CThostFtdcChangeAccountField,
        CThostFtdcInstrumentField,
        CThostFtdcRspInfoField,
        CThostFtdcCombPromotionParamField,
        CThostFtdcRspInfoField,
        CThostFtdcFensUserInfoField,
        CThostFtdcReqAuthenticateField,
        CThostFtdcUserSystemInfoField,
        CThostFtdcUserSystemInfoField,
        CThostFtdcReqUserLoginField,
        CThostFtdcUserLogoutField,
        CThostFtdcUserPasswordUpdateField,
        CThostFtdcTradingAccountPasswordUpdateField,
        CThostFtdcReqUserAuthMethodField,
        CThostFtdcReqGenUserCaptchaField,
        CThostFtdcReqGenUserTextField,
        CThostFtdcReqUserLoginWithCaptchaField,
        CThostFtdcReqUserLoginWithTextField,
        CThostFtdcReqUserLoginWithOTPField,
        CThostFtdcInputOrderField,
        CThostFtdcParkedOrderField,
        CThostFtdcParkedOrderActionField,
        CThostFtdcInputOrderActionField,
        CThostFtdcQryMaxOrderVolumeField,
        CThostFtdcSettlementInfoConfirmField,
        CThostFtdcRemoveParkedOrderField,
        CThostFtdcRemoveParkedOrderActionField,
        CThostFtdcInputExecOrderField,
        CThostFtdcInputExecOrderActionField,
        CThostFtdcInputForQuoteField,
        CThostFtdcInputQuoteField,
        CThostFtdcInputQuoteActionField,
        CThostFtdcInputBatchOrderActionField,
        CThostFtdcInputOptionSelfCloseField,
        CThostFtdcInputOptionSelfCloseActionField,
        CThostFtdcInputCombActionField,
        CThostFtdcQryOrderField,
        CThostFtdcQryTradeField,
        CThostFtdcQryInvestorPositionField,
        CThostFtdcQryTradingAccountField,
        CThostFtdcQryInvestorField,
        CThostFtdcQryTradingCodeField,
        CThostFtdcQryInstrumentMarginRateField,
        CThostFtdcQryInstrumentCommissionRateField,
        CThostFtdcQryExchangeField,
        CThostFtdcQryProductField,
        CThostFtdcQryInstrumentField,
        CThostFtdcQryDepthMarketDataField,
        CThostFtdcQrySettlementInfoField,
        CThostFtdcQryTransferBankField,
        CThostFtdcQryInvestorPositionDetailField,
        CThostFtdcQryNoticeField,
        CThostFtdcQrySettlementInfoConfirmField,
        CThostFtdcQryInvestorPositionCombineDetailField,
        CThostFtdcQryCFMMCTradingAccountKeyField,
        CThostFtdcQryEWarrantOffsetField,
        CThostFtdcQryInvestorProductGroupMarginField,
        CThostFtdcQryExchangeMarginRateField,
        CThostFtdcQryExchangeMarginRateAdjustField,
        CThostFtdcQryExchangeRateField,
        CThostFtdcQrySecAgentACIDMapField,
        CThostFtdcQryProductExchRateField,
        CThostFtdcQryProductGroupField,
        CThostFtdcQryMMInstrumentCommissionRateField,
        CThostFtdcQryMMOptionInstrCommRateField,
        CThostFtdcQryInstrumentOrderCommRateField,
        CThostFtdcQryTradingAccountField,
        CThostFtdcQrySecAgentCheckModeField,
        CThostFtdcQrySecAgentTradeInfoField,
        CThostFtdcQryOptionInstrTradeCostField,
        CThostFtdcQryOptionInstrCommRateField,
        CThostFtdcQryExecOrderField,
        CThostFtdcQryForQuoteField,
        CThostFtdcQryQuoteField,
        CThostFtdcQryOptionSelfCloseField,
        CThostFtdcQryInvestUnitField,
        CThostFtdcQryCombInstrumentGuardField,
        CThostFtdcQryCombActionField,
        CThostFtdcQryTransferSerialField,
        CThostFtdcQryAccountregisterField,
        CThostFtdcQryContractBankField,
        CThostFtdcQryParkedOrderField,
        CThostFtdcQryParkedOrderActionField,
        CThostFtdcQryTradingNoticeField,
        CThostFtdcQryBrokerTradingParamsField,
        CThostFtdcQryBrokerTradingAlgosField,
        CThostFtdcQueryCFMMCTradingAccountTokenField,
        CThostFtdcReqTransferField,
        CThostFtdcReqTransferField,
        CThostFtdcReqQueryAccountField,
        CThostFtdcQryClassifiedInstrumentField,
        CThostFtdcQryCombPromotionParamField)

class CThostFtdcTraderSpi:
    def __init__(self, sock_client):
        self.sock_client = sock_client
        #1) send socket cmd let cpp_ctp to create a spi class object. 2)cpp_ctp return the new spi object pointer.
        self.sock_client.add_listen_rsp_fun(self.rsp_handler)
        req = {'req_id':str(uuid.uuid4()),'cmd':'create_spi','cmd_type':'td','ptr':None}
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
    def OnRspAuthenticate(self, pRspAuthenticateField:CThostFtdcRspAuthenticateField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        pass
    def OnRspUserLogin(self, pRspUserLogin:CThostFtdcRspUserLoginField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        pass
    def OnRspUserLogout(self, pUserLogout:CThostFtdcUserLogoutField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        pass
    def OnRspUserPasswordUpdate(self, pUserPasswordUpdate:CThostFtdcUserPasswordUpdateField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        pass
    def OnRspTradingAccountPasswordUpdate(self, pTradingAccountPasswordUpdate:CThostFtdcTradingAccountPasswordUpdateField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        pass
    def OnRspUserAuthMethod(self, pRspUserAuthMethod:CThostFtdcRspUserAuthMethodField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        pass
    def OnRspGenUserCaptcha(self, pRspGenUserCaptcha:CThostFtdcRspGenUserCaptchaField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        pass
    def OnRspGenUserText(self, pRspGenUserText:CThostFtdcRspGenUserTextField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        pass
    def OnRspOrderInsert(self, pInputOrder:CThostFtdcInputOrderField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        pass
    def OnRspParkedOrderInsert(self, pParkedOrder:CThostFtdcParkedOrderField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        pass
    def OnRspParkedOrderAction(self, pParkedOrderAction:CThostFtdcParkedOrderActionField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        pass
    def OnRspOrderAction(self, pInputOrderAction:CThostFtdcInputOrderActionField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        pass
    def OnRspQryMaxOrderVolume(self, pQryMaxOrderVolume:CThostFtdcQryMaxOrderVolumeField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        pass
    def OnRspSettlementInfoConfirm(self, pSettlementInfoConfirm:CThostFtdcSettlementInfoConfirmField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        pass
    def OnRspRemoveParkedOrder(self, pRemoveParkedOrder:CThostFtdcRemoveParkedOrderField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        pass
    def OnRspRemoveParkedOrderAction(self, pRemoveParkedOrderAction:CThostFtdcRemoveParkedOrderActionField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        pass
    def OnRspExecOrderInsert(self, pInputExecOrder:CThostFtdcInputExecOrderField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        pass
    def OnRspExecOrderAction(self, pInputExecOrderAction:CThostFtdcInputExecOrderActionField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        pass
    def OnRspForQuoteInsert(self, pInputForQuote:CThostFtdcInputForQuoteField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        pass
    def OnRspQuoteInsert(self, pInputQuote:CThostFtdcInputQuoteField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        pass
    def OnRspQuoteAction(self, pInputQuoteAction:CThostFtdcInputQuoteActionField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        pass
    def OnRspBatchOrderAction(self, pInputBatchOrderAction:CThostFtdcInputBatchOrderActionField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        pass
    def OnRspOptionSelfCloseInsert(self, pInputOptionSelfClose:CThostFtdcInputOptionSelfCloseField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        pass
    def OnRspOptionSelfCloseAction(self, pInputOptionSelfCloseAction:CThostFtdcInputOptionSelfCloseActionField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        pass
    def OnRspCombActionInsert(self, pInputCombAction:CThostFtdcInputCombActionField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        pass
    def OnRspQryOrder(self, pOrder:CThostFtdcOrderField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        pass
    def OnRspQryTrade(self, pTrade:CThostFtdcTradeField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        pass
    def OnRspQryInvestorPosition(self, pInvestorPosition:CThostFtdcInvestorPositionField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        pass
    def OnRspQryTradingAccount(self, pTradingAccount:CThostFtdcTradingAccountField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        pass
    def OnRspQryInvestor(self, pInvestor:CThostFtdcInvestorField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        pass
    def OnRspQryTradingCode(self, pTradingCode:CThostFtdcTradingCodeField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        pass
    def OnRspQryInstrumentMarginRate(self, pInstrumentMarginRate:CThostFtdcInstrumentMarginRateField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        pass
    def OnRspQryInstrumentCommissionRate(self, pInstrumentCommissionRate:CThostFtdcInstrumentCommissionRateField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        pass
    def OnRspQryExchange(self, pExchange:CThostFtdcExchangeField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        pass
    def OnRspQryProduct(self, pProduct:CThostFtdcProductField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        pass
    def OnRspQryInstrument(self, pInstrument:CThostFtdcInstrumentField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        pass
    def OnRspQryDepthMarketData(self, pDepthMarketData:CThostFtdcDepthMarketDataField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        pass
    def OnRspQrySettlementInfo(self, pSettlementInfo:CThostFtdcSettlementInfoField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        pass
    def OnRspQryTransferBank(self, pTransferBank:CThostFtdcTransferBankField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        pass
    def OnRspQryInvestorPositionDetail(self, pInvestorPositionDetail:CThostFtdcInvestorPositionDetailField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        pass
    def OnRspQryNotice(self, pNotice:CThostFtdcNoticeField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        pass
    def OnRspQrySettlementInfoConfirm(self, pSettlementInfoConfirm:CThostFtdcSettlementInfoConfirmField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        pass
    def OnRspQryInvestorPositionCombineDetail(self, pInvestorPositionCombineDetail:CThostFtdcInvestorPositionCombineDetailField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        pass
    def OnRspQryCFMMCTradingAccountKey(self, pCFMMCTradingAccountKey:CThostFtdcCFMMCTradingAccountKeyField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        pass
    def OnRspQryEWarrantOffset(self, pEWarrantOffset:CThostFtdcEWarrantOffsetField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        pass
    def OnRspQryInvestorProductGroupMargin(self, pInvestorProductGroupMargin:CThostFtdcInvestorProductGroupMarginField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        pass
    def OnRspQryExchangeMarginRate(self, pExchangeMarginRate:CThostFtdcExchangeMarginRateField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        pass
    def OnRspQryExchangeMarginRateAdjust(self, pExchangeMarginRateAdjust:CThostFtdcExchangeMarginRateAdjustField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        pass
    def OnRspQryExchangeRate(self, pExchangeRate:CThostFtdcExchangeRateField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        pass
    def OnRspQrySecAgentACIDMap(self, pSecAgentACIDMap:CThostFtdcSecAgentACIDMapField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        pass
    def OnRspQryProductExchRate(self, pProductExchRate:CThostFtdcProductExchRateField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        pass
    def OnRspQryProductGroup(self, pProductGroup:CThostFtdcProductGroupField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        pass
    def OnRspQryMMInstrumentCommissionRate(self, pMMInstrumentCommissionRate:CThostFtdcMMInstrumentCommissionRateField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        pass
    def OnRspQryMMOptionInstrCommRate(self, pMMOptionInstrCommRate:CThostFtdcMMOptionInstrCommRateField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        pass
    def OnRspQryInstrumentOrderCommRate(self, pInstrumentOrderCommRate:CThostFtdcInstrumentOrderCommRateField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        pass
    def OnRspQrySecAgentTradingAccount(self, pTradingAccount:CThostFtdcTradingAccountField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        pass
    def OnRspQrySecAgentCheckMode(self, pSecAgentCheckMode:CThostFtdcSecAgentCheckModeField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        pass
    def OnRspQrySecAgentTradeInfo(self, pSecAgentTradeInfo:CThostFtdcSecAgentTradeInfoField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        pass
    def OnRspQryOptionInstrTradeCost(self, pOptionInstrTradeCost:CThostFtdcOptionInstrTradeCostField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        pass
    def OnRspQryOptionInstrCommRate(self, pOptionInstrCommRate:CThostFtdcOptionInstrCommRateField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        pass
    def OnRspQryExecOrder(self, pExecOrder:CThostFtdcExecOrderField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        pass
    def OnRspQryForQuote(self, pForQuote:CThostFtdcForQuoteField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        pass
    def OnRspQryQuote(self, pQuote:CThostFtdcQuoteField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        pass
    def OnRspQryOptionSelfClose(self, pOptionSelfClose:CThostFtdcOptionSelfCloseField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        pass
    def OnRspQryInvestUnit(self, pInvestUnit:CThostFtdcInvestUnitField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        pass
    def OnRspQryCombInstrumentGuard(self, pCombInstrumentGuard:CThostFtdcCombInstrumentGuardField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        pass
    def OnRspQryCombAction(self, pCombAction:CThostFtdcCombActionField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        pass
    def OnRspQryTransferSerial(self, pTransferSerial:CThostFtdcTransferSerialField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        pass
    def OnRspQryAccountregister(self, pAccountregister:CThostFtdcAccountregisterField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        pass
    def OnRspError(self, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        pass
    def OnRtnOrder(self, pOrder:CThostFtdcOrderField):
        pass
    def OnRtnTrade(self, pTrade:CThostFtdcTradeField):
        pass
    def OnErrRtnOrderInsert(self, pInputOrder:CThostFtdcInputOrderField, pRspInfo:CThostFtdcRspInfoField):
        pass
    def OnErrRtnOrderAction(self, pOrderAction:CThostFtdcOrderActionField, pRspInfo:CThostFtdcRspInfoField):
        pass
    def OnRtnInstrumentStatus(self, pInstrumentStatus:CThostFtdcInstrumentStatusField):
        pass
    def OnRtnBulletin(self, pBulletin:CThostFtdcBulletinField):
        pass
    def OnRtnTradingNotice(self, pTradingNoticeInfo:CThostFtdcTradingNoticeInfoField):
        pass
    def OnRtnErrorConditionalOrder(self, pErrorConditionalOrder:CThostFtdcErrorConditionalOrderField):
        pass
    def OnRtnExecOrder(self, pExecOrder:CThostFtdcExecOrderField):
        pass
    def OnErrRtnExecOrderInsert(self, pInputExecOrder:CThostFtdcInputExecOrderField, pRspInfo:CThostFtdcRspInfoField):
        pass
    def OnErrRtnExecOrderAction(self, pExecOrderAction:CThostFtdcExecOrderActionField, pRspInfo:CThostFtdcRspInfoField):
        pass
    def OnErrRtnForQuoteInsert(self, pInputForQuote:CThostFtdcInputForQuoteField, pRspInfo:CThostFtdcRspInfoField):
        pass
    def OnRtnQuote(self, pQuote:CThostFtdcQuoteField):
        pass
    def OnErrRtnQuoteInsert(self, pInputQuote:CThostFtdcInputQuoteField, pRspInfo:CThostFtdcRspInfoField):
        pass
    def OnErrRtnQuoteAction(self, pQuoteAction:CThostFtdcQuoteActionField, pRspInfo:CThostFtdcRspInfoField):
        pass
    def OnRtnForQuoteRsp(self, pForQuoteRsp:CThostFtdcForQuoteRspField):
        pass
    def OnRtnCFMMCTradingAccountToken(self, pCFMMCTradingAccountToken:CThostFtdcCFMMCTradingAccountTokenField):
        pass
    def OnErrRtnBatchOrderAction(self, pBatchOrderAction:CThostFtdcBatchOrderActionField, pRspInfo:CThostFtdcRspInfoField):
        pass
    def OnRtnOptionSelfClose(self, pOptionSelfClose:CThostFtdcOptionSelfCloseField):
        pass
    def OnErrRtnOptionSelfCloseInsert(self, pInputOptionSelfClose:CThostFtdcInputOptionSelfCloseField, pRspInfo:CThostFtdcRspInfoField):
        pass
    def OnErrRtnOptionSelfCloseAction(self, pOptionSelfCloseAction:CThostFtdcOptionSelfCloseActionField, pRspInfo:CThostFtdcRspInfoField):
        pass
    def OnRtnCombAction(self, pCombAction:CThostFtdcCombActionField):
        pass
    def OnErrRtnCombActionInsert(self, pInputCombAction:CThostFtdcInputCombActionField, pRspInfo:CThostFtdcRspInfoField):
        pass
    def OnRspQryContractBank(self, pContractBank:CThostFtdcContractBankField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        pass
    def OnRspQryParkedOrder(self, pParkedOrder:CThostFtdcParkedOrderField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        pass
    def OnRspQryParkedOrderAction(self, pParkedOrderAction:CThostFtdcParkedOrderActionField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        pass
    def OnRspQryTradingNotice(self, pTradingNotice:CThostFtdcTradingNoticeField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        pass
    def OnRspQryBrokerTradingParams(self, pBrokerTradingParams:CThostFtdcBrokerTradingParamsField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        pass
    def OnRspQryBrokerTradingAlgos(self, pBrokerTradingAlgos:CThostFtdcBrokerTradingAlgosField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        pass
    def OnRspQueryCFMMCTradingAccountToken(self, pQueryCFMMCTradingAccountToken:CThostFtdcQueryCFMMCTradingAccountTokenField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        pass
    def OnRtnFromBankToFutureByBank(self, pRspTransfer:CThostFtdcRspTransferField):
        pass
    def OnRtnFromFutureToBankByBank(self, pRspTransfer:CThostFtdcRspTransferField):
        pass
    def OnRtnRepealFromBankToFutureByBank(self, pRspRepeal:CThostFtdcRspRepealField):
        pass
    def OnRtnRepealFromFutureToBankByBank(self, pRspRepeal:CThostFtdcRspRepealField):
        pass
    def OnRtnFromBankToFutureByFuture(self, pRspTransfer:CThostFtdcRspTransferField):
        pass
    def OnRtnFromFutureToBankByFuture(self, pRspTransfer:CThostFtdcRspTransferField):
        pass
    def OnRtnRepealFromBankToFutureByFutureManual(self, pRspRepeal:CThostFtdcRspRepealField):
        pass
    def OnRtnRepealFromFutureToBankByFutureManual(self, pRspRepeal:CThostFtdcRspRepealField):
        pass
    def OnRtnQueryBankBalanceByFuture(self, pNotifyQueryAccount:CThostFtdcNotifyQueryAccountField):
        pass
    def OnErrRtnBankToFutureByFuture(self, pReqTransfer:CThostFtdcReqTransferField, pRspInfo:CThostFtdcRspInfoField):
        pass
    def OnErrRtnFutureToBankByFuture(self, pReqTransfer:CThostFtdcReqTransferField, pRspInfo:CThostFtdcRspInfoField):
        pass
    def OnErrRtnRepealBankToFutureByFutureManual(self, pReqRepeal:CThostFtdcReqRepealField, pRspInfo:CThostFtdcRspInfoField):
        pass
    def OnErrRtnRepealFutureToBankByFutureManual(self, pReqRepeal:CThostFtdcReqRepealField, pRspInfo:CThostFtdcRspInfoField):
        pass
    def OnErrRtnQueryBankBalanceByFuture(self, pReqQueryAccount:CThostFtdcReqQueryAccountField, pRspInfo:CThostFtdcRspInfoField):
        pass
    def OnRtnRepealFromBankToFutureByFuture(self, pRspRepeal:CThostFtdcRspRepealField):
        pass
    def OnRtnRepealFromFutureToBankByFuture(self, pRspRepeal:CThostFtdcRspRepealField):
        pass
    def OnRspFromBankToFutureByFuture(self, pReqTransfer:CThostFtdcReqTransferField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        pass
    def OnRspFromFutureToBankByFuture(self, pReqTransfer:CThostFtdcReqTransferField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        pass
    def OnRspQueryBankAccountMoneyByFuture(self, pReqQueryAccount:CThostFtdcReqQueryAccountField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        pass
    def OnRtnOpenAccountByBank(self, pOpenAccount:CThostFtdcOpenAccountField):
        pass
    def OnRtnCancelAccountByBank(self, pCancelAccount:CThostFtdcCancelAccountField):
        pass
    def OnRtnChangeAccountByBank(self, pChangeAccount:CThostFtdcChangeAccountField):
        pass
    def OnRspQryClassifiedInstrument(self, pInstrument:CThostFtdcInstrumentField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        pass
    def OnRspQryCombPromotionParam(self, pCombPromotionParam:CThostFtdcCombPromotionParamField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        pass
    def rsp_handler(self, rsp):
        rsp_cmd_type = rsp['cmd_type']
        if rsp_cmd_type != 'td':
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
        elif m == 'OnRspAuthenticate':
            rsp_method(CThostFtdcRspAuthenticateField(rsp['pRspAuthenticateField']), CThostFtdcRspInfoField(rsp['pRspInfo']), rsp['nRequestID'], rsp['bIsLast'])
        elif m == 'OnRspUserLogin':
            rsp_method(CThostFtdcRspUserLoginField(rsp['pRspUserLogin']), CThostFtdcRspInfoField(rsp['pRspInfo']), rsp['nRequestID'], rsp['bIsLast'])
        elif m == 'OnRspUserLogout':
            rsp_method(CThostFtdcUserLogoutField(rsp['pUserLogout']), CThostFtdcRspInfoField(rsp['pRspInfo']), rsp['nRequestID'], rsp['bIsLast'])
        elif m == 'OnRspUserPasswordUpdate':
            rsp_method(CThostFtdcUserPasswordUpdateField(rsp['pUserPasswordUpdate']), CThostFtdcRspInfoField(rsp['pRspInfo']), rsp['nRequestID'], rsp['bIsLast'])
        elif m == 'OnRspTradingAccountPasswordUpdate':
            rsp_method(CThostFtdcTradingAccountPasswordUpdateField(rsp['pTradingAccountPasswordUpdate']), CThostFtdcRspInfoField(rsp['pRspInfo']), rsp['nRequestID'], rsp['bIsLast'])
        elif m == 'OnRspUserAuthMethod':
            rsp_method(CThostFtdcRspUserAuthMethodField(rsp['pRspUserAuthMethod']), CThostFtdcRspInfoField(rsp['pRspInfo']), rsp['nRequestID'], rsp['bIsLast'])
        elif m == 'OnRspGenUserCaptcha':
            rsp_method(CThostFtdcRspGenUserCaptchaField(rsp['pRspGenUserCaptcha']), CThostFtdcRspInfoField(rsp['pRspInfo']), rsp['nRequestID'], rsp['bIsLast'])
        elif m == 'OnRspGenUserText':
            rsp_method(CThostFtdcRspGenUserTextField(rsp['pRspGenUserText']), CThostFtdcRspInfoField(rsp['pRspInfo']), rsp['nRequestID'], rsp['bIsLast'])
        elif m == 'OnRspOrderInsert':
            rsp_method(CThostFtdcInputOrderField(rsp['pInputOrder']), CThostFtdcRspInfoField(rsp['pRspInfo']), rsp['nRequestID'], rsp['bIsLast'])
        elif m == 'OnRspParkedOrderInsert':
            rsp_method(CThostFtdcParkedOrderField(rsp['pParkedOrder']), CThostFtdcRspInfoField(rsp['pRspInfo']), rsp['nRequestID'], rsp['bIsLast'])
        elif m == 'OnRspParkedOrderAction':
            rsp_method(CThostFtdcParkedOrderActionField(rsp['pParkedOrderAction']), CThostFtdcRspInfoField(rsp['pRspInfo']), rsp['nRequestID'], rsp['bIsLast'])
        elif m == 'OnRspOrderAction':
            rsp_method(CThostFtdcInputOrderActionField(rsp['pInputOrderAction']), CThostFtdcRspInfoField(rsp['pRspInfo']), rsp['nRequestID'], rsp['bIsLast'])
        elif m == 'OnRspQryMaxOrderVolume':
            rsp_method(CThostFtdcQryMaxOrderVolumeField(rsp['pQryMaxOrderVolume']), CThostFtdcRspInfoField(rsp['pRspInfo']), rsp['nRequestID'], rsp['bIsLast'])
        elif m == 'OnRspSettlementInfoConfirm':
            rsp_method(CThostFtdcSettlementInfoConfirmField(rsp['pSettlementInfoConfirm']), CThostFtdcRspInfoField(rsp['pRspInfo']), rsp['nRequestID'], rsp['bIsLast'])
        elif m == 'OnRspRemoveParkedOrder':
            rsp_method(CThostFtdcRemoveParkedOrderField(rsp['pRemoveParkedOrder']), CThostFtdcRspInfoField(rsp['pRspInfo']), rsp['nRequestID'], rsp['bIsLast'])
        elif m == 'OnRspRemoveParkedOrderAction':
            rsp_method(CThostFtdcRemoveParkedOrderActionField(rsp['pRemoveParkedOrderAction']), CThostFtdcRspInfoField(rsp['pRspInfo']), rsp['nRequestID'], rsp['bIsLast'])
        elif m == 'OnRspExecOrderInsert':
            rsp_method(CThostFtdcInputExecOrderField(rsp['pInputExecOrder']), CThostFtdcRspInfoField(rsp['pRspInfo']), rsp['nRequestID'], rsp['bIsLast'])
        elif m == 'OnRspExecOrderAction':
            rsp_method(CThostFtdcInputExecOrderActionField(rsp['pInputExecOrderAction']), CThostFtdcRspInfoField(rsp['pRspInfo']), rsp['nRequestID'], rsp['bIsLast'])
        elif m == 'OnRspForQuoteInsert':
            rsp_method(CThostFtdcInputForQuoteField(rsp['pInputForQuote']), CThostFtdcRspInfoField(rsp['pRspInfo']), rsp['nRequestID'], rsp['bIsLast'])
        elif m == 'OnRspQuoteInsert':
            rsp_method(CThostFtdcInputQuoteField(rsp['pInputQuote']), CThostFtdcRspInfoField(rsp['pRspInfo']), rsp['nRequestID'], rsp['bIsLast'])
        elif m == 'OnRspQuoteAction':
            rsp_method(CThostFtdcInputQuoteActionField(rsp['pInputQuoteAction']), CThostFtdcRspInfoField(rsp['pRspInfo']), rsp['nRequestID'], rsp['bIsLast'])
        elif m == 'OnRspBatchOrderAction':
            rsp_method(CThostFtdcInputBatchOrderActionField(rsp['pInputBatchOrderAction']), CThostFtdcRspInfoField(rsp['pRspInfo']), rsp['nRequestID'], rsp['bIsLast'])
        elif m == 'OnRspOptionSelfCloseInsert':
            rsp_method(CThostFtdcInputOptionSelfCloseField(rsp['pInputOptionSelfClose']), CThostFtdcRspInfoField(rsp['pRspInfo']), rsp['nRequestID'], rsp['bIsLast'])
        elif m == 'OnRspOptionSelfCloseAction':
            rsp_method(CThostFtdcInputOptionSelfCloseActionField(rsp['pInputOptionSelfCloseAction']), CThostFtdcRspInfoField(rsp['pRspInfo']), rsp['nRequestID'], rsp['bIsLast'])
        elif m == 'OnRspCombActionInsert':
            rsp_method(CThostFtdcInputCombActionField(rsp['pInputCombAction']), CThostFtdcRspInfoField(rsp['pRspInfo']), rsp['nRequestID'], rsp['bIsLast'])
        elif m == 'OnRspQryOrder':
            rsp_method(CThostFtdcOrderField(rsp['pOrder']), CThostFtdcRspInfoField(rsp['pRspInfo']), rsp['nRequestID'], rsp['bIsLast'])
        elif m == 'OnRspQryTrade':
            rsp_method(CThostFtdcTradeField(rsp['pTrade']), CThostFtdcRspInfoField(rsp['pRspInfo']), rsp['nRequestID'], rsp['bIsLast'])
        elif m == 'OnRspQryInvestorPosition':
            rsp_method(CThostFtdcInvestorPositionField(rsp['pInvestorPosition']), CThostFtdcRspInfoField(rsp['pRspInfo']), rsp['nRequestID'], rsp['bIsLast'])
        elif m == 'OnRspQryTradingAccount':
            rsp_method(CThostFtdcTradingAccountField(rsp['pTradingAccount']), CThostFtdcRspInfoField(rsp['pRspInfo']), rsp['nRequestID'], rsp['bIsLast'])
        elif m == 'OnRspQryInvestor':
            rsp_method(CThostFtdcInvestorField(rsp['pInvestor']), CThostFtdcRspInfoField(rsp['pRspInfo']), rsp['nRequestID'], rsp['bIsLast'])
        elif m == 'OnRspQryTradingCode':
            rsp_method(CThostFtdcTradingCodeField(rsp['pTradingCode']), CThostFtdcRspInfoField(rsp['pRspInfo']), rsp['nRequestID'], rsp['bIsLast'])
        elif m == 'OnRspQryInstrumentMarginRate':
            rsp_method(CThostFtdcInstrumentMarginRateField(rsp['pInstrumentMarginRate']), CThostFtdcRspInfoField(rsp['pRspInfo']), rsp['nRequestID'], rsp['bIsLast'])
        elif m == 'OnRspQryInstrumentCommissionRate':
            rsp_method(CThostFtdcInstrumentCommissionRateField(rsp['pInstrumentCommissionRate']), CThostFtdcRspInfoField(rsp['pRspInfo']), rsp['nRequestID'], rsp['bIsLast'])
        elif m == 'OnRspQryExchange':
            rsp_method(CThostFtdcExchangeField(rsp['pExchange']), CThostFtdcRspInfoField(rsp['pRspInfo']), rsp['nRequestID'], rsp['bIsLast'])
        elif m == 'OnRspQryProduct':
            rsp_method(CThostFtdcProductField(rsp['pProduct']), CThostFtdcRspInfoField(rsp['pRspInfo']), rsp['nRequestID'], rsp['bIsLast'])
        elif m == 'OnRspQryInstrument':
            rsp_method(CThostFtdcInstrumentField(rsp['pInstrument']), CThostFtdcRspInfoField(rsp['pRspInfo']), rsp['nRequestID'], rsp['bIsLast'])
        elif m == 'OnRspQryDepthMarketData':
            rsp_method(CThostFtdcDepthMarketDataField(rsp['pDepthMarketData']), CThostFtdcRspInfoField(rsp['pRspInfo']), rsp['nRequestID'], rsp['bIsLast'])
        elif m == 'OnRspQrySettlementInfo':
            rsp_method(CThostFtdcSettlementInfoField(rsp['pSettlementInfo']), CThostFtdcRspInfoField(rsp['pRspInfo']), rsp['nRequestID'], rsp['bIsLast'])
        elif m == 'OnRspQryTransferBank':
            rsp_method(CThostFtdcTransferBankField(rsp['pTransferBank']), CThostFtdcRspInfoField(rsp['pRspInfo']), rsp['nRequestID'], rsp['bIsLast'])
        elif m == 'OnRspQryInvestorPositionDetail':
            rsp_method(CThostFtdcInvestorPositionDetailField(rsp['pInvestorPositionDetail']), CThostFtdcRspInfoField(rsp['pRspInfo']), rsp['nRequestID'], rsp['bIsLast'])
        elif m == 'OnRspQryNotice':
            rsp_method(CThostFtdcNoticeField(rsp['pNotice']), CThostFtdcRspInfoField(rsp['pRspInfo']), rsp['nRequestID'], rsp['bIsLast'])
        elif m == 'OnRspQrySettlementInfoConfirm':
            rsp_method(CThostFtdcSettlementInfoConfirmField(rsp['pSettlementInfoConfirm']), CThostFtdcRspInfoField(rsp['pRspInfo']), rsp['nRequestID'], rsp['bIsLast'])
        elif m == 'OnRspQryInvestorPositionCombineDetail':
            rsp_method(CThostFtdcInvestorPositionCombineDetailField(rsp['pInvestorPositionCombineDetail']), CThostFtdcRspInfoField(rsp['pRspInfo']), rsp['nRequestID'], rsp['bIsLast'])
        elif m == 'OnRspQryCFMMCTradingAccountKey':
            rsp_method(CThostFtdcCFMMCTradingAccountKeyField(rsp['pCFMMCTradingAccountKey']), CThostFtdcRspInfoField(rsp['pRspInfo']), rsp['nRequestID'], rsp['bIsLast'])
        elif m == 'OnRspQryEWarrantOffset':
            rsp_method(CThostFtdcEWarrantOffsetField(rsp['pEWarrantOffset']), CThostFtdcRspInfoField(rsp['pRspInfo']), rsp['nRequestID'], rsp['bIsLast'])
        elif m == 'OnRspQryInvestorProductGroupMargin':
            rsp_method(CThostFtdcInvestorProductGroupMarginField(rsp['pInvestorProductGroupMargin']), CThostFtdcRspInfoField(rsp['pRspInfo']), rsp['nRequestID'], rsp['bIsLast'])
        elif m == 'OnRspQryExchangeMarginRate':
            rsp_method(CThostFtdcExchangeMarginRateField(rsp['pExchangeMarginRate']), CThostFtdcRspInfoField(rsp['pRspInfo']), rsp['nRequestID'], rsp['bIsLast'])
        elif m == 'OnRspQryExchangeMarginRateAdjust':
            rsp_method(CThostFtdcExchangeMarginRateAdjustField(rsp['pExchangeMarginRateAdjust']), CThostFtdcRspInfoField(rsp['pRspInfo']), rsp['nRequestID'], rsp['bIsLast'])
        elif m == 'OnRspQryExchangeRate':
            rsp_method(CThostFtdcExchangeRateField(rsp['pExchangeRate']), CThostFtdcRspInfoField(rsp['pRspInfo']), rsp['nRequestID'], rsp['bIsLast'])
        elif m == 'OnRspQrySecAgentACIDMap':
            rsp_method(CThostFtdcSecAgentACIDMapField(rsp['pSecAgentACIDMap']), CThostFtdcRspInfoField(rsp['pRspInfo']), rsp['nRequestID'], rsp['bIsLast'])
        elif m == 'OnRspQryProductExchRate':
            rsp_method(CThostFtdcProductExchRateField(rsp['pProductExchRate']), CThostFtdcRspInfoField(rsp['pRspInfo']), rsp['nRequestID'], rsp['bIsLast'])
        elif m == 'OnRspQryProductGroup':
            rsp_method(CThostFtdcProductGroupField(rsp['pProductGroup']), CThostFtdcRspInfoField(rsp['pRspInfo']), rsp['nRequestID'], rsp['bIsLast'])
        elif m == 'OnRspQryMMInstrumentCommissionRate':
            rsp_method(CThostFtdcMMInstrumentCommissionRateField(rsp['pMMInstrumentCommissionRate']), CThostFtdcRspInfoField(rsp['pRspInfo']), rsp['nRequestID'], rsp['bIsLast'])
        elif m == 'OnRspQryMMOptionInstrCommRate':
            rsp_method(CThostFtdcMMOptionInstrCommRateField(rsp['pMMOptionInstrCommRate']), CThostFtdcRspInfoField(rsp['pRspInfo']), rsp['nRequestID'], rsp['bIsLast'])
        elif m == 'OnRspQryInstrumentOrderCommRate':
            rsp_method(CThostFtdcInstrumentOrderCommRateField(rsp['pInstrumentOrderCommRate']), CThostFtdcRspInfoField(rsp['pRspInfo']), rsp['nRequestID'], rsp['bIsLast'])
        elif m == 'OnRspQrySecAgentTradingAccount':
            rsp_method(CThostFtdcTradingAccountField(rsp['pTradingAccount']), CThostFtdcRspInfoField(rsp['pRspInfo']), rsp['nRequestID'], rsp['bIsLast'])
        elif m == 'OnRspQrySecAgentCheckMode':
            rsp_method(CThostFtdcSecAgentCheckModeField(rsp['pSecAgentCheckMode']), CThostFtdcRspInfoField(rsp['pRspInfo']), rsp['nRequestID'], rsp['bIsLast'])
        elif m == 'OnRspQrySecAgentTradeInfo':
            rsp_method(CThostFtdcSecAgentTradeInfoField(rsp['pSecAgentTradeInfo']), CThostFtdcRspInfoField(rsp['pRspInfo']), rsp['nRequestID'], rsp['bIsLast'])
        elif m == 'OnRspQryOptionInstrTradeCost':
            rsp_method(CThostFtdcOptionInstrTradeCostField(rsp['pOptionInstrTradeCost']), CThostFtdcRspInfoField(rsp['pRspInfo']), rsp['nRequestID'], rsp['bIsLast'])
        elif m == 'OnRspQryOptionInstrCommRate':
            rsp_method(CThostFtdcOptionInstrCommRateField(rsp['pOptionInstrCommRate']), CThostFtdcRspInfoField(rsp['pRspInfo']), rsp['nRequestID'], rsp['bIsLast'])
        elif m == 'OnRspQryExecOrder':
            rsp_method(CThostFtdcExecOrderField(rsp['pExecOrder']), CThostFtdcRspInfoField(rsp['pRspInfo']), rsp['nRequestID'], rsp['bIsLast'])
        elif m == 'OnRspQryForQuote':
            rsp_method(CThostFtdcForQuoteField(rsp['pForQuote']), CThostFtdcRspInfoField(rsp['pRspInfo']), rsp['nRequestID'], rsp['bIsLast'])
        elif m == 'OnRspQryQuote':
            rsp_method(CThostFtdcQuoteField(rsp['pQuote']), CThostFtdcRspInfoField(rsp['pRspInfo']), rsp['nRequestID'], rsp['bIsLast'])
        elif m == 'OnRspQryOptionSelfClose':
            rsp_method(CThostFtdcOptionSelfCloseField(rsp['pOptionSelfClose']), CThostFtdcRspInfoField(rsp['pRspInfo']), rsp['nRequestID'], rsp['bIsLast'])
        elif m == 'OnRspQryInvestUnit':
            rsp_method(CThostFtdcInvestUnitField(rsp['pInvestUnit']), CThostFtdcRspInfoField(rsp['pRspInfo']), rsp['nRequestID'], rsp['bIsLast'])
        elif m == 'OnRspQryCombInstrumentGuard':
            rsp_method(CThostFtdcCombInstrumentGuardField(rsp['pCombInstrumentGuard']), CThostFtdcRspInfoField(rsp['pRspInfo']), rsp['nRequestID'], rsp['bIsLast'])
        elif m == 'OnRspQryCombAction':
            rsp_method(CThostFtdcCombActionField(rsp['pCombAction']), CThostFtdcRspInfoField(rsp['pRspInfo']), rsp['nRequestID'], rsp['bIsLast'])
        elif m == 'OnRspQryTransferSerial':
            rsp_method(CThostFtdcTransferSerialField(rsp['pTransferSerial']), CThostFtdcRspInfoField(rsp['pRspInfo']), rsp['nRequestID'], rsp['bIsLast'])
        elif m == 'OnRspQryAccountregister':
            rsp_method(CThostFtdcAccountregisterField(rsp['pAccountregister']), CThostFtdcRspInfoField(rsp['pRspInfo']), rsp['nRequestID'], rsp['bIsLast'])
        elif m == 'OnRspError':
            rsp_method(CThostFtdcRspInfoField(rsp['pRspInfo']), rsp['nRequestID'], rsp['bIsLast'])
        elif m == 'OnRtnOrder':
            rsp_method(CThostFtdcOrderField(rsp['pOrder']))
        elif m == 'OnRtnTrade':
            rsp_method(CThostFtdcTradeField(rsp['pTrade']))
        elif m == 'OnErrRtnOrderInsert':
            rsp_method(CThostFtdcInputOrderField(rsp['pInputOrder']), CThostFtdcRspInfoField(rsp['pRspInfo']))
        elif m == 'OnErrRtnOrderAction':
            rsp_method(CThostFtdcOrderActionField(rsp['pOrderAction']), CThostFtdcRspInfoField(rsp['pRspInfo']))
        elif m == 'OnRtnInstrumentStatus':
            rsp_method(CThostFtdcInstrumentStatusField(rsp['pInstrumentStatus']))
        elif m == 'OnRtnBulletin':
            rsp_method(CThostFtdcBulletinField(rsp['pBulletin']))
        elif m == 'OnRtnTradingNotice':
            rsp_method(CThostFtdcTradingNoticeInfoField(rsp['pTradingNoticeInfo']))
        elif m == 'OnRtnErrorConditionalOrder':
            rsp_method(CThostFtdcErrorConditionalOrderField(rsp['pErrorConditionalOrder']))
        elif m == 'OnRtnExecOrder':
            rsp_method(CThostFtdcExecOrderField(rsp['pExecOrder']))
        elif m == 'OnErrRtnExecOrderInsert':
            rsp_method(CThostFtdcInputExecOrderField(rsp['pInputExecOrder']), CThostFtdcRspInfoField(rsp['pRspInfo']))
        elif m == 'OnErrRtnExecOrderAction':
            rsp_method(CThostFtdcExecOrderActionField(rsp['pExecOrderAction']), CThostFtdcRspInfoField(rsp['pRspInfo']))
        elif m == 'OnErrRtnForQuoteInsert':
            rsp_method(CThostFtdcInputForQuoteField(rsp['pInputForQuote']), CThostFtdcRspInfoField(rsp['pRspInfo']))
        elif m == 'OnRtnQuote':
            rsp_method(CThostFtdcQuoteField(rsp['pQuote']))
        elif m == 'OnErrRtnQuoteInsert':
            rsp_method(CThostFtdcInputQuoteField(rsp['pInputQuote']), CThostFtdcRspInfoField(rsp['pRspInfo']))
        elif m == 'OnErrRtnQuoteAction':
            rsp_method(CThostFtdcQuoteActionField(rsp['pQuoteAction']), CThostFtdcRspInfoField(rsp['pRspInfo']))
        elif m == 'OnRtnForQuoteRsp':
            rsp_method(CThostFtdcForQuoteRspField(rsp['pForQuoteRsp']))
        elif m == 'OnRtnCFMMCTradingAccountToken':
            rsp_method(CThostFtdcCFMMCTradingAccountTokenField(rsp['pCFMMCTradingAccountToken']))
        elif m == 'OnErrRtnBatchOrderAction':
            rsp_method(CThostFtdcBatchOrderActionField(rsp['pBatchOrderAction']), CThostFtdcRspInfoField(rsp['pRspInfo']))
        elif m == 'OnRtnOptionSelfClose':
            rsp_method(CThostFtdcOptionSelfCloseField(rsp['pOptionSelfClose']))
        elif m == 'OnErrRtnOptionSelfCloseInsert':
            rsp_method(CThostFtdcInputOptionSelfCloseField(rsp['pInputOptionSelfClose']), CThostFtdcRspInfoField(rsp['pRspInfo']))
        elif m == 'OnErrRtnOptionSelfCloseAction':
            rsp_method(CThostFtdcOptionSelfCloseActionField(rsp['pOptionSelfCloseAction']), CThostFtdcRspInfoField(rsp['pRspInfo']))
        elif m == 'OnRtnCombAction':
            rsp_method(CThostFtdcCombActionField(rsp['pCombAction']))
        elif m == 'OnErrRtnCombActionInsert':
            rsp_method(CThostFtdcInputCombActionField(rsp['pInputCombAction']), CThostFtdcRspInfoField(rsp['pRspInfo']))
        elif m == 'OnRspQryContractBank':
            rsp_method(CThostFtdcContractBankField(rsp['pContractBank']), CThostFtdcRspInfoField(rsp['pRspInfo']), rsp['nRequestID'], rsp['bIsLast'])
        elif m == 'OnRspQryParkedOrder':
            rsp_method(CThostFtdcParkedOrderField(rsp['pParkedOrder']), CThostFtdcRspInfoField(rsp['pRspInfo']), rsp['nRequestID'], rsp['bIsLast'])
        elif m == 'OnRspQryParkedOrderAction':
            rsp_method(CThostFtdcParkedOrderActionField(rsp['pParkedOrderAction']), CThostFtdcRspInfoField(rsp['pRspInfo']), rsp['nRequestID'], rsp['bIsLast'])
        elif m == 'OnRspQryTradingNotice':
            rsp_method(CThostFtdcTradingNoticeField(rsp['pTradingNotice']), CThostFtdcRspInfoField(rsp['pRspInfo']), rsp['nRequestID'], rsp['bIsLast'])
        elif m == 'OnRspQryBrokerTradingParams':
            rsp_method(CThostFtdcBrokerTradingParamsField(rsp['pBrokerTradingParams']), CThostFtdcRspInfoField(rsp['pRspInfo']), rsp['nRequestID'], rsp['bIsLast'])
        elif m == 'OnRspQryBrokerTradingAlgos':
            rsp_method(CThostFtdcBrokerTradingAlgosField(rsp['pBrokerTradingAlgos']), CThostFtdcRspInfoField(rsp['pRspInfo']), rsp['nRequestID'], rsp['bIsLast'])
        elif m == 'OnRspQueryCFMMCTradingAccountToken':
            rsp_method(CThostFtdcQueryCFMMCTradingAccountTokenField(rsp['pQueryCFMMCTradingAccountToken']), CThostFtdcRspInfoField(rsp['pRspInfo']), rsp['nRequestID'], rsp['bIsLast'])
        elif m == 'OnRtnFromBankToFutureByBank':
            rsp_method(CThostFtdcRspTransferField(rsp['pRspTransfer']))
        elif m == 'OnRtnFromFutureToBankByBank':
            rsp_method(CThostFtdcRspTransferField(rsp['pRspTransfer']))
        elif m == 'OnRtnRepealFromBankToFutureByBank':
            rsp_method(CThostFtdcRspRepealField(rsp['pRspRepeal']))
        elif m == 'OnRtnRepealFromFutureToBankByBank':
            rsp_method(CThostFtdcRspRepealField(rsp['pRspRepeal']))
        elif m == 'OnRtnFromBankToFutureByFuture':
            rsp_method(CThostFtdcRspTransferField(rsp['pRspTransfer']))
        elif m == 'OnRtnFromFutureToBankByFuture':
            rsp_method(CThostFtdcRspTransferField(rsp['pRspTransfer']))
        elif m == 'OnRtnRepealFromBankToFutureByFutureManual':
            rsp_method(CThostFtdcRspRepealField(rsp['pRspRepeal']))
        elif m == 'OnRtnRepealFromFutureToBankByFutureManual':
            rsp_method(CThostFtdcRspRepealField(rsp['pRspRepeal']))
        elif m == 'OnRtnQueryBankBalanceByFuture':
            rsp_method(CThostFtdcNotifyQueryAccountField(rsp['pNotifyQueryAccount']))
        elif m == 'OnErrRtnBankToFutureByFuture':
            rsp_method(CThostFtdcReqTransferField(rsp['pReqTransfer']), CThostFtdcRspInfoField(rsp['pRspInfo']))
        elif m == 'OnErrRtnFutureToBankByFuture':
            rsp_method(CThostFtdcReqTransferField(rsp['pReqTransfer']), CThostFtdcRspInfoField(rsp['pRspInfo']))
        elif m == 'OnErrRtnRepealBankToFutureByFutureManual':
            rsp_method(CThostFtdcReqRepealField(rsp['pReqRepeal']), CThostFtdcRspInfoField(rsp['pRspInfo']))
        elif m == 'OnErrRtnRepealFutureToBankByFutureManual':
            rsp_method(CThostFtdcReqRepealField(rsp['pReqRepeal']), CThostFtdcRspInfoField(rsp['pRspInfo']))
        elif m == 'OnErrRtnQueryBankBalanceByFuture':
            rsp_method(CThostFtdcReqQueryAccountField(rsp['pReqQueryAccount']), CThostFtdcRspInfoField(rsp['pRspInfo']))
        elif m == 'OnRtnRepealFromBankToFutureByFuture':
            rsp_method(CThostFtdcRspRepealField(rsp['pRspRepeal']))
        elif m == 'OnRtnRepealFromFutureToBankByFuture':
            rsp_method(CThostFtdcRspRepealField(rsp['pRspRepeal']))
        elif m == 'OnRspFromBankToFutureByFuture':
            rsp_method(CThostFtdcReqTransferField(rsp['pReqTransfer']), CThostFtdcRspInfoField(rsp['pRspInfo']), rsp['nRequestID'], rsp['bIsLast'])
        elif m == 'OnRspFromFutureToBankByFuture':
            rsp_method(CThostFtdcReqTransferField(rsp['pReqTransfer']), CThostFtdcRspInfoField(rsp['pRspInfo']), rsp['nRequestID'], rsp['bIsLast'])
        elif m == 'OnRspQueryBankAccountMoneyByFuture':
            rsp_method(CThostFtdcReqQueryAccountField(rsp['pReqQueryAccount']), CThostFtdcRspInfoField(rsp['pRspInfo']), rsp['nRequestID'], rsp['bIsLast'])
        elif m == 'OnRtnOpenAccountByBank':
            rsp_method(CThostFtdcOpenAccountField(rsp['pOpenAccount']))
        elif m == 'OnRtnCancelAccountByBank':
            rsp_method(CThostFtdcCancelAccountField(rsp['pCancelAccount']))
        elif m == 'OnRtnChangeAccountByBank':
            rsp_method(CThostFtdcChangeAccountField(rsp['pChangeAccount']))
        elif m == 'OnRspQryClassifiedInstrument':
            rsp_method(CThostFtdcInstrumentField(rsp['pInstrument']), CThostFtdcRspInfoField(rsp['pRspInfo']), rsp['nRequestID'], rsp['bIsLast'])
        elif m == 'OnRspQryCombPromotionParam':
            rsp_method(CThostFtdcCombPromotionParamField(rsp['pCombPromotionParam']), CThostFtdcRspInfoField(rsp['pRspInfo']), rsp['nRequestID'], rsp['bIsLast'])

class CThostFtdcTraderApi:
    def __init__(self, api_ptr, sock_client):
        self.api_ptr = api_ptr
        self.sock_client = sock_client

    @staticmethod
    def CreateFtdcTraderApi(pszFlowPath:str,sock_client:Py_sock_ctp):
        req = {'req_id':str(uuid.uuid4()),'cmd':'CreateFtdcTraderApi','cmd_type':'td','ptr':None,'pszFlowPath':pszFlowPath}
        req_ret = sock_client.send_req(req)
        return CThostFtdcTraderApi(int(req_ret), sock_client)
    @staticmethod
    def GetApiVersion(sock_client:Py_sock_ctp):
        req = {'req_id':str(uuid.uuid4()),'cmd':'GetApiVersion','cmd_type':'td','ptr':None}
        req_ret = sock_client.send_req(req)
        return req_ret
    def Release(self):
        req = {'cmd':'Release','cmd_type':'td','ptr':self.api_ptr}
        self.sock_client.send_req(req)
    def Init(self):
        req = {'cmd':'Init','cmd_type':'td','ptr':self.api_ptr}
        self.sock_client.send_req(req)
    def Join(self):
        req = {'req_id':str(uuid.uuid4()),'cmd':'Join','cmd_type':'td','ptr':self.api_ptr}
        req_ret = self.sock_client.send_req(req)
        return req_ret
    def GetTradingDay(self):
        req = {'req_id':str(uuid.uuid4()),'cmd':'GetTradingDay','cmd_type':'td','ptr':self.api_ptr}
        req_ret = self.sock_client.send_req(req)
        return req_ret
    def RegisterFront(self,pszFrontAddress:str):
        req = {'cmd':'RegisterFront','cmd_type':'td','ptr':self.api_ptr,'pszFrontAddress':pszFrontAddress}
        self.sock_client.send_req(req)
    def RegisterNameServer(self,pszNsAddress:str):
        req = {'cmd':'RegisterNameServer','cmd_type':'td','ptr':self.api_ptr,'pszNsAddress':pszNsAddress}
        self.sock_client.send_req(req)
    def RegisterFensUserInfo(self,pFensUserInfo:CThostFtdcFensUserInfoField):
        req = {'cmd':'RegisterFensUserInfo','cmd_type':'td','ptr':self.api_ptr,'pFensUserInfo':vars(pFensUserInfo)}
        self.sock_client.send_req(req)
    def RegisterSpi(self,pSpi:CThostFtdcTraderSpi):
        req = {'cmd':'RegisterSpi','cmd_type':'td','ptr':self.api_ptr,'pSpi':pSpi}
        self.sock_client.send_req(req)
    def SubscribePrivateTopic(self,nResumeType:int):
        req = {'cmd':'SubscribePrivateTopic','cmd_type':'td','ptr':self.api_ptr,'nResumeType':nResumeType}
        self.sock_client.send_req(req)
    def SubscribePublicTopic(self,nResumeType:int):
        req = {'cmd':'SubscribePublicTopic','cmd_type':'td','ptr':self.api_ptr,'nResumeType':nResumeType}
        self.sock_client.send_req(req)
    def ReqAuthenticate(self,pReqAuthenticateField:CThostFtdcReqAuthenticateField,nRequestID:int):
        req = {'req_id':str(uuid.uuid4()),'cmd':'ReqAuthenticate','cmd_type':'td','ptr':self.api_ptr,'pReqAuthenticateField':vars(pReqAuthenticateField),'nRequestID':nRequestID}
        req_ret = self.sock_client.send_req(req)
        return req_ret
    def RegisterUserSystemInfo(self,pUserSystemInfo:CThostFtdcUserSystemInfoField):
        req = {'req_id':str(uuid.uuid4()),'cmd':'RegisterUserSystemInfo','cmd_type':'td','ptr':self.api_ptr,'pUserSystemInfo':vars(pUserSystemInfo)}
        req_ret = self.sock_client.send_req(req)
        return req_ret
    def SubmitUserSystemInfo(self,pUserSystemInfo:CThostFtdcUserSystemInfoField):
        req = {'req_id':str(uuid.uuid4()),'cmd':'SubmitUserSystemInfo','cmd_type':'td','ptr':self.api_ptr,'pUserSystemInfo':vars(pUserSystemInfo)}
        req_ret = self.sock_client.send_req(req)
        return req_ret
    def ReqUserLogin(self,pReqUserLoginField:CThostFtdcReqUserLoginField,nRequestID:int):
        req = {'req_id':str(uuid.uuid4()),'cmd':'ReqUserLogin','cmd_type':'td','ptr':self.api_ptr,'pReqUserLoginField':vars(pReqUserLoginField),'nRequestID':nRequestID}
        req_ret = self.sock_client.send_req(req)
        return req_ret
    def ReqUserLogout(self,pUserLogout:CThostFtdcUserLogoutField,nRequestID:int):
        req = {'req_id':str(uuid.uuid4()),'cmd':'ReqUserLogout','cmd_type':'td','ptr':self.api_ptr,'pUserLogout':vars(pUserLogout),'nRequestID':nRequestID}
        req_ret = self.sock_client.send_req(req)
        return req_ret
    def ReqUserPasswordUpdate(self,pUserPasswordUpdate:CThostFtdcUserPasswordUpdateField,nRequestID:int):
        req = {'req_id':str(uuid.uuid4()),'cmd':'ReqUserPasswordUpdate','cmd_type':'td','ptr':self.api_ptr,'pUserPasswordUpdate':vars(pUserPasswordUpdate),'nRequestID':nRequestID}
        req_ret = self.sock_client.send_req(req)
        return req_ret
    def ReqTradingAccountPasswordUpdate(self,pTradingAccountPasswordUpdate:CThostFtdcTradingAccountPasswordUpdateField,nRequestID:int):
        req = {'req_id':str(uuid.uuid4()),'cmd':'ReqTradingAccountPasswordUpdate','cmd_type':'td','ptr':self.api_ptr,'pTradingAccountPasswordUpdate':vars(pTradingAccountPasswordUpdate),'nRequestID':nRequestID}
        req_ret = self.sock_client.send_req(req)
        return req_ret
    def ReqUserAuthMethod(self,pReqUserAuthMethod:CThostFtdcReqUserAuthMethodField,nRequestID:int):
        req = {'req_id':str(uuid.uuid4()),'cmd':'ReqUserAuthMethod','cmd_type':'td','ptr':self.api_ptr,'pReqUserAuthMethod':vars(pReqUserAuthMethod),'nRequestID':nRequestID}
        req_ret = self.sock_client.send_req(req)
        return req_ret
    def ReqGenUserCaptcha(self,pReqGenUserCaptcha:CThostFtdcReqGenUserCaptchaField,nRequestID:int):
        req = {'req_id':str(uuid.uuid4()),'cmd':'ReqGenUserCaptcha','cmd_type':'td','ptr':self.api_ptr,'pReqGenUserCaptcha':vars(pReqGenUserCaptcha),'nRequestID':nRequestID}
        req_ret = self.sock_client.send_req(req)
        return req_ret
    def ReqGenUserText(self,pReqGenUserText:CThostFtdcReqGenUserTextField,nRequestID:int):
        req = {'req_id':str(uuid.uuid4()),'cmd':'ReqGenUserText','cmd_type':'td','ptr':self.api_ptr,'pReqGenUserText':vars(pReqGenUserText),'nRequestID':nRequestID}
        req_ret = self.sock_client.send_req(req)
        return req_ret
    def ReqUserLoginWithCaptcha(self,pReqUserLoginWithCaptcha:CThostFtdcReqUserLoginWithCaptchaField,nRequestID:int):
        req = {'req_id':str(uuid.uuid4()),'cmd':'ReqUserLoginWithCaptcha','cmd_type':'td','ptr':self.api_ptr,'pReqUserLoginWithCaptcha':vars(pReqUserLoginWithCaptcha),'nRequestID':nRequestID}
        req_ret = self.sock_client.send_req(req)
        return req_ret
    def ReqUserLoginWithText(self,pReqUserLoginWithText:CThostFtdcReqUserLoginWithTextField,nRequestID:int):
        req = {'req_id':str(uuid.uuid4()),'cmd':'ReqUserLoginWithText','cmd_type':'td','ptr':self.api_ptr,'pReqUserLoginWithText':vars(pReqUserLoginWithText),'nRequestID':nRequestID}
        req_ret = self.sock_client.send_req(req)
        return req_ret
    def ReqUserLoginWithOTP(self,pReqUserLoginWithOTP:CThostFtdcReqUserLoginWithOTPField,nRequestID:int):
        req = {'req_id':str(uuid.uuid4()),'cmd':'ReqUserLoginWithOTP','cmd_type':'td','ptr':self.api_ptr,'pReqUserLoginWithOTP':vars(pReqUserLoginWithOTP),'nRequestID':nRequestID}
        req_ret = self.sock_client.send_req(req)
        return req_ret
    def ReqOrderInsert(self,pInputOrder:CThostFtdcInputOrderField,nRequestID:int):
        req = {'req_id':str(uuid.uuid4()),'cmd':'ReqOrderInsert','cmd_type':'td','ptr':self.api_ptr,'pInputOrder':vars(pInputOrder),'nRequestID':nRequestID}
        req_ret = self.sock_client.send_req(req)
        return req_ret
    def ReqParkedOrderInsert(self,pParkedOrder:CThostFtdcParkedOrderField,nRequestID:int):
        req = {'req_id':str(uuid.uuid4()),'cmd':'ReqParkedOrderInsert','cmd_type':'td','ptr':self.api_ptr,'pParkedOrder':vars(pParkedOrder),'nRequestID':nRequestID}
        req_ret = self.sock_client.send_req(req)
        return req_ret
    def ReqParkedOrderAction(self,pParkedOrderAction:CThostFtdcParkedOrderActionField,nRequestID:int):
        req = {'req_id':str(uuid.uuid4()),'cmd':'ReqParkedOrderAction','cmd_type':'td','ptr':self.api_ptr,'pParkedOrderAction':vars(pParkedOrderAction),'nRequestID':nRequestID}
        req_ret = self.sock_client.send_req(req)
        return req_ret
    def ReqOrderAction(self,pInputOrderAction:CThostFtdcInputOrderActionField,nRequestID:int):
        req = {'req_id':str(uuid.uuid4()),'cmd':'ReqOrderAction','cmd_type':'td','ptr':self.api_ptr,'pInputOrderAction':vars(pInputOrderAction),'nRequestID':nRequestID}
        req_ret = self.sock_client.send_req(req)
        return req_ret
    def ReqQryMaxOrderVolume(self,pQryMaxOrderVolume:CThostFtdcQryMaxOrderVolumeField,nRequestID:int):
        req = {'req_id':str(uuid.uuid4()),'cmd':'ReqQryMaxOrderVolume','cmd_type':'td','ptr':self.api_ptr,'pQryMaxOrderVolume':vars(pQryMaxOrderVolume),'nRequestID':nRequestID}
        req_ret = self.sock_client.send_req(req)
        return req_ret
    def ReqSettlementInfoConfirm(self,pSettlementInfoConfirm:CThostFtdcSettlementInfoConfirmField,nRequestID:int):
        req = {'req_id':str(uuid.uuid4()),'cmd':'ReqSettlementInfoConfirm','cmd_type':'td','ptr':self.api_ptr,'pSettlementInfoConfirm':vars(pSettlementInfoConfirm),'nRequestID':nRequestID}
        req_ret = self.sock_client.send_req(req)
        return req_ret
    def ReqRemoveParkedOrder(self,pRemoveParkedOrder:CThostFtdcRemoveParkedOrderField,nRequestID:int):
        req = {'req_id':str(uuid.uuid4()),'cmd':'ReqRemoveParkedOrder','cmd_type':'td','ptr':self.api_ptr,'pRemoveParkedOrder':vars(pRemoveParkedOrder),'nRequestID':nRequestID}
        req_ret = self.sock_client.send_req(req)
        return req_ret
    def ReqRemoveParkedOrderAction(self,pRemoveParkedOrderAction:CThostFtdcRemoveParkedOrderActionField,nRequestID:int):
        req = {'req_id':str(uuid.uuid4()),'cmd':'ReqRemoveParkedOrderAction','cmd_type':'td','ptr':self.api_ptr,'pRemoveParkedOrderAction':vars(pRemoveParkedOrderAction),'nRequestID':nRequestID}
        req_ret = self.sock_client.send_req(req)
        return req_ret
    def ReqExecOrderInsert(self,pInputExecOrder:CThostFtdcInputExecOrderField,nRequestID:int):
        req = {'req_id':str(uuid.uuid4()),'cmd':'ReqExecOrderInsert','cmd_type':'td','ptr':self.api_ptr,'pInputExecOrder':vars(pInputExecOrder),'nRequestID':nRequestID}
        req_ret = self.sock_client.send_req(req)
        return req_ret
    def ReqExecOrderAction(self,pInputExecOrderAction:CThostFtdcInputExecOrderActionField,nRequestID:int):
        req = {'req_id':str(uuid.uuid4()),'cmd':'ReqExecOrderAction','cmd_type':'td','ptr':self.api_ptr,'pInputExecOrderAction':vars(pInputExecOrderAction),'nRequestID':nRequestID}
        req_ret = self.sock_client.send_req(req)
        return req_ret
    def ReqForQuoteInsert(self,pInputForQuote:CThostFtdcInputForQuoteField,nRequestID:int):
        req = {'req_id':str(uuid.uuid4()),'cmd':'ReqForQuoteInsert','cmd_type':'td','ptr':self.api_ptr,'pInputForQuote':vars(pInputForQuote),'nRequestID':nRequestID}
        req_ret = self.sock_client.send_req(req)
        return req_ret
    def ReqQuoteInsert(self,pInputQuote:CThostFtdcInputQuoteField,nRequestID:int):
        req = {'req_id':str(uuid.uuid4()),'cmd':'ReqQuoteInsert','cmd_type':'td','ptr':self.api_ptr,'pInputQuote':vars(pInputQuote),'nRequestID':nRequestID}
        req_ret = self.sock_client.send_req(req)
        return req_ret
    def ReqQuoteAction(self,pInputQuoteAction:CThostFtdcInputQuoteActionField,nRequestID:int):
        req = {'req_id':str(uuid.uuid4()),'cmd':'ReqQuoteAction','cmd_type':'td','ptr':self.api_ptr,'pInputQuoteAction':vars(pInputQuoteAction),'nRequestID':nRequestID}
        req_ret = self.sock_client.send_req(req)
        return req_ret
    def ReqBatchOrderAction(self,pInputBatchOrderAction:CThostFtdcInputBatchOrderActionField,nRequestID:int):
        req = {'req_id':str(uuid.uuid4()),'cmd':'ReqBatchOrderAction','cmd_type':'td','ptr':self.api_ptr,'pInputBatchOrderAction':vars(pInputBatchOrderAction),'nRequestID':nRequestID}
        req_ret = self.sock_client.send_req(req)
        return req_ret
    def ReqOptionSelfCloseInsert(self,pInputOptionSelfClose:CThostFtdcInputOptionSelfCloseField,nRequestID:int):
        req = {'req_id':str(uuid.uuid4()),'cmd':'ReqOptionSelfCloseInsert','cmd_type':'td','ptr':self.api_ptr,'pInputOptionSelfClose':vars(pInputOptionSelfClose),'nRequestID':nRequestID}
        req_ret = self.sock_client.send_req(req)
        return req_ret
    def ReqOptionSelfCloseAction(self,pInputOptionSelfCloseAction:CThostFtdcInputOptionSelfCloseActionField,nRequestID:int):
        req = {'req_id':str(uuid.uuid4()),'cmd':'ReqOptionSelfCloseAction','cmd_type':'td','ptr':self.api_ptr,'pInputOptionSelfCloseAction':vars(pInputOptionSelfCloseAction),'nRequestID':nRequestID}
        req_ret = self.sock_client.send_req(req)
        return req_ret
    def ReqCombActionInsert(self,pInputCombAction:CThostFtdcInputCombActionField,nRequestID:int):
        req = {'req_id':str(uuid.uuid4()),'cmd':'ReqCombActionInsert','cmd_type':'td','ptr':self.api_ptr,'pInputCombAction':vars(pInputCombAction),'nRequestID':nRequestID}
        req_ret = self.sock_client.send_req(req)
        return req_ret
    def ReqQryOrder(self,pQryOrder:CThostFtdcQryOrderField,nRequestID:int):
        req = {'req_id':str(uuid.uuid4()),'cmd':'ReqQryOrder','cmd_type':'td','ptr':self.api_ptr,'pQryOrder':vars(pQryOrder),'nRequestID':nRequestID}
        req_ret = self.sock_client.send_req(req)
        return req_ret
    def ReqQryTrade(self,pQryTrade:CThostFtdcQryTradeField,nRequestID:int):
        req = {'req_id':str(uuid.uuid4()),'cmd':'ReqQryTrade','cmd_type':'td','ptr':self.api_ptr,'pQryTrade':vars(pQryTrade),'nRequestID':nRequestID}
        req_ret = self.sock_client.send_req(req)
        return req_ret
    def ReqQryInvestorPosition(self,pQryInvestorPosition:CThostFtdcQryInvestorPositionField,nRequestID:int):
        req = {'req_id':str(uuid.uuid4()),'cmd':'ReqQryInvestorPosition','cmd_type':'td','ptr':self.api_ptr,'pQryInvestorPosition':vars(pQryInvestorPosition),'nRequestID':nRequestID}
        req_ret = self.sock_client.send_req(req)
        return req_ret
    def ReqQryTradingAccount(self,pQryTradingAccount:CThostFtdcQryTradingAccountField,nRequestID:int):
        req = {'req_id':str(uuid.uuid4()),'cmd':'ReqQryTradingAccount','cmd_type':'td','ptr':self.api_ptr,'pQryTradingAccount':vars(pQryTradingAccount),'nRequestID':nRequestID}
        req_ret = self.sock_client.send_req(req)
        return req_ret
    def ReqQryInvestor(self,pQryInvestor:CThostFtdcQryInvestorField,nRequestID:int):
        req = {'req_id':str(uuid.uuid4()),'cmd':'ReqQryInvestor','cmd_type':'td','ptr':self.api_ptr,'pQryInvestor':vars(pQryInvestor),'nRequestID':nRequestID}
        req_ret = self.sock_client.send_req(req)
        return req_ret
    def ReqQryTradingCode(self,pQryTradingCode:CThostFtdcQryTradingCodeField,nRequestID:int):
        req = {'req_id':str(uuid.uuid4()),'cmd':'ReqQryTradingCode','cmd_type':'td','ptr':self.api_ptr,'pQryTradingCode':vars(pQryTradingCode),'nRequestID':nRequestID}
        req_ret = self.sock_client.send_req(req)
        return req_ret
    def ReqQryInstrumentMarginRate(self,pQryInstrumentMarginRate:CThostFtdcQryInstrumentMarginRateField,nRequestID:int):
        req = {'req_id':str(uuid.uuid4()),'cmd':'ReqQryInstrumentMarginRate','cmd_type':'td','ptr':self.api_ptr,'pQryInstrumentMarginRate':vars(pQryInstrumentMarginRate),'nRequestID':nRequestID}
        req_ret = self.sock_client.send_req(req)
        return req_ret
    def ReqQryInstrumentCommissionRate(self,pQryInstrumentCommissionRate:CThostFtdcQryInstrumentCommissionRateField,nRequestID:int):
        req = {'req_id':str(uuid.uuid4()),'cmd':'ReqQryInstrumentCommissionRate','cmd_type':'td','ptr':self.api_ptr,'pQryInstrumentCommissionRate':vars(pQryInstrumentCommissionRate),'nRequestID':nRequestID}
        req_ret = self.sock_client.send_req(req)
        return req_ret
    def ReqQryExchange(self,pQryExchange:CThostFtdcQryExchangeField,nRequestID:int):
        req = {'req_id':str(uuid.uuid4()),'cmd':'ReqQryExchange','cmd_type':'td','ptr':self.api_ptr,'pQryExchange':vars(pQryExchange),'nRequestID':nRequestID}
        req_ret = self.sock_client.send_req(req)
        return req_ret
    def ReqQryProduct(self,pQryProduct:CThostFtdcQryProductField,nRequestID:int):
        req = {'req_id':str(uuid.uuid4()),'cmd':'ReqQryProduct','cmd_type':'td','ptr':self.api_ptr,'pQryProduct':vars(pQryProduct),'nRequestID':nRequestID}
        req_ret = self.sock_client.send_req(req)
        return req_ret
    def ReqQryInstrument(self,pQryInstrument:CThostFtdcQryInstrumentField,nRequestID:int):
        req = {'req_id':str(uuid.uuid4()),'cmd':'ReqQryInstrument','cmd_type':'td','ptr':self.api_ptr,'pQryInstrument':vars(pQryInstrument),'nRequestID':nRequestID}
        req_ret = self.sock_client.send_req(req)
        return req_ret
    def ReqQryDepthMarketData(self,pQryDepthMarketData:CThostFtdcQryDepthMarketDataField,nRequestID:int):
        req = {'req_id':str(uuid.uuid4()),'cmd':'ReqQryDepthMarketData','cmd_type':'td','ptr':self.api_ptr,'pQryDepthMarketData':vars(pQryDepthMarketData),'nRequestID':nRequestID}
        req_ret = self.sock_client.send_req(req)
        return req_ret
    def ReqQrySettlementInfo(self,pQrySettlementInfo:CThostFtdcQrySettlementInfoField,nRequestID:int):
        req = {'req_id':str(uuid.uuid4()),'cmd':'ReqQrySettlementInfo','cmd_type':'td','ptr':self.api_ptr,'pQrySettlementInfo':vars(pQrySettlementInfo),'nRequestID':nRequestID}
        req_ret = self.sock_client.send_req(req)
        return req_ret
    def ReqQryTransferBank(self,pQryTransferBank:CThostFtdcQryTransferBankField,nRequestID:int):
        req = {'req_id':str(uuid.uuid4()),'cmd':'ReqQryTransferBank','cmd_type':'td','ptr':self.api_ptr,'pQryTransferBank':vars(pQryTransferBank),'nRequestID':nRequestID}
        req_ret = self.sock_client.send_req(req)
        return req_ret
    def ReqQryInvestorPositionDetail(self,pQryInvestorPositionDetail:CThostFtdcQryInvestorPositionDetailField,nRequestID:int):
        req = {'req_id':str(uuid.uuid4()),'cmd':'ReqQryInvestorPositionDetail','cmd_type':'td','ptr':self.api_ptr,'pQryInvestorPositionDetail':vars(pQryInvestorPositionDetail),'nRequestID':nRequestID}
        req_ret = self.sock_client.send_req(req)
        return req_ret
    def ReqQryNotice(self,pQryNotice:CThostFtdcQryNoticeField,nRequestID:int):
        req = {'req_id':str(uuid.uuid4()),'cmd':'ReqQryNotice','cmd_type':'td','ptr':self.api_ptr,'pQryNotice':vars(pQryNotice),'nRequestID':nRequestID}
        req_ret = self.sock_client.send_req(req)
        return req_ret
    def ReqQrySettlementInfoConfirm(self,pQrySettlementInfoConfirm:CThostFtdcQrySettlementInfoConfirmField,nRequestID:int):
        req = {'req_id':str(uuid.uuid4()),'cmd':'ReqQrySettlementInfoConfirm','cmd_type':'td','ptr':self.api_ptr,'pQrySettlementInfoConfirm':vars(pQrySettlementInfoConfirm),'nRequestID':nRequestID}
        req_ret = self.sock_client.send_req(req)
        return req_ret
    def ReqQryInvestorPositionCombineDetail(self,pQryInvestorPositionCombineDetail:CThostFtdcQryInvestorPositionCombineDetailField,nRequestID:int):
        req = {'req_id':str(uuid.uuid4()),'cmd':'ReqQryInvestorPositionCombineDetail','cmd_type':'td','ptr':self.api_ptr,'pQryInvestorPositionCombineDetail':vars(pQryInvestorPositionCombineDetail),'nRequestID':nRequestID}
        req_ret = self.sock_client.send_req(req)
        return req_ret
    def ReqQryCFMMCTradingAccountKey(self,pQryCFMMCTradingAccountKey:CThostFtdcQryCFMMCTradingAccountKeyField,nRequestID:int):
        req = {'req_id':str(uuid.uuid4()),'cmd':'ReqQryCFMMCTradingAccountKey','cmd_type':'td','ptr':self.api_ptr,'pQryCFMMCTradingAccountKey':vars(pQryCFMMCTradingAccountKey),'nRequestID':nRequestID}
        req_ret = self.sock_client.send_req(req)
        return req_ret
    def ReqQryEWarrantOffset(self,pQryEWarrantOffset:CThostFtdcQryEWarrantOffsetField,nRequestID:int):
        req = {'req_id':str(uuid.uuid4()),'cmd':'ReqQryEWarrantOffset','cmd_type':'td','ptr':self.api_ptr,'pQryEWarrantOffset':vars(pQryEWarrantOffset),'nRequestID':nRequestID}
        req_ret = self.sock_client.send_req(req)
        return req_ret
    def ReqQryInvestorProductGroupMargin(self,pQryInvestorProductGroupMargin:CThostFtdcQryInvestorProductGroupMarginField,nRequestID:int):
        req = {'req_id':str(uuid.uuid4()),'cmd':'ReqQryInvestorProductGroupMargin','cmd_type':'td','ptr':self.api_ptr,'pQryInvestorProductGroupMargin':vars(pQryInvestorProductGroupMargin),'nRequestID':nRequestID}
        req_ret = self.sock_client.send_req(req)
        return req_ret
    def ReqQryExchangeMarginRate(self,pQryExchangeMarginRate:CThostFtdcQryExchangeMarginRateField,nRequestID:int):
        req = {'req_id':str(uuid.uuid4()),'cmd':'ReqQryExchangeMarginRate','cmd_type':'td','ptr':self.api_ptr,'pQryExchangeMarginRate':vars(pQryExchangeMarginRate),'nRequestID':nRequestID}
        req_ret = self.sock_client.send_req(req)
        return req_ret
    def ReqQryExchangeMarginRateAdjust(self,pQryExchangeMarginRateAdjust:CThostFtdcQryExchangeMarginRateAdjustField,nRequestID:int):
        req = {'req_id':str(uuid.uuid4()),'cmd':'ReqQryExchangeMarginRateAdjust','cmd_type':'td','ptr':self.api_ptr,'pQryExchangeMarginRateAdjust':vars(pQryExchangeMarginRateAdjust),'nRequestID':nRequestID}
        req_ret = self.sock_client.send_req(req)
        return req_ret
    def ReqQryExchangeRate(self,pQryExchangeRate:CThostFtdcQryExchangeRateField,nRequestID:int):
        req = {'req_id':str(uuid.uuid4()),'cmd':'ReqQryExchangeRate','cmd_type':'td','ptr':self.api_ptr,'pQryExchangeRate':vars(pQryExchangeRate),'nRequestID':nRequestID}
        req_ret = self.sock_client.send_req(req)
        return req_ret
    def ReqQrySecAgentACIDMap(self,pQrySecAgentACIDMap:CThostFtdcQrySecAgentACIDMapField,nRequestID:int):
        req = {'req_id':str(uuid.uuid4()),'cmd':'ReqQrySecAgentACIDMap','cmd_type':'td','ptr':self.api_ptr,'pQrySecAgentACIDMap':vars(pQrySecAgentACIDMap),'nRequestID':nRequestID}
        req_ret = self.sock_client.send_req(req)
        return req_ret
    def ReqQryProductExchRate(self,pQryProductExchRate:CThostFtdcQryProductExchRateField,nRequestID:int):
        req = {'req_id':str(uuid.uuid4()),'cmd':'ReqQryProductExchRate','cmd_type':'td','ptr':self.api_ptr,'pQryProductExchRate':vars(pQryProductExchRate),'nRequestID':nRequestID}
        req_ret = self.sock_client.send_req(req)
        return req_ret
    def ReqQryProductGroup(self,pQryProductGroup:CThostFtdcQryProductGroupField,nRequestID:int):
        req = {'req_id':str(uuid.uuid4()),'cmd':'ReqQryProductGroup','cmd_type':'td','ptr':self.api_ptr,'pQryProductGroup':vars(pQryProductGroup),'nRequestID':nRequestID}
        req_ret = self.sock_client.send_req(req)
        return req_ret
    def ReqQryMMInstrumentCommissionRate(self,pQryMMInstrumentCommissionRate:CThostFtdcQryMMInstrumentCommissionRateField,nRequestID:int):
        req = {'req_id':str(uuid.uuid4()),'cmd':'ReqQryMMInstrumentCommissionRate','cmd_type':'td','ptr':self.api_ptr,'pQryMMInstrumentCommissionRate':vars(pQryMMInstrumentCommissionRate),'nRequestID':nRequestID}
        req_ret = self.sock_client.send_req(req)
        return req_ret
    def ReqQryMMOptionInstrCommRate(self,pQryMMOptionInstrCommRate:CThostFtdcQryMMOptionInstrCommRateField,nRequestID:int):
        req = {'req_id':str(uuid.uuid4()),'cmd':'ReqQryMMOptionInstrCommRate','cmd_type':'td','ptr':self.api_ptr,'pQryMMOptionInstrCommRate':vars(pQryMMOptionInstrCommRate),'nRequestID':nRequestID}
        req_ret = self.sock_client.send_req(req)
        return req_ret
    def ReqQryInstrumentOrderCommRate(self,pQryInstrumentOrderCommRate:CThostFtdcQryInstrumentOrderCommRateField,nRequestID:int):
        req = {'req_id':str(uuid.uuid4()),'cmd':'ReqQryInstrumentOrderCommRate','cmd_type':'td','ptr':self.api_ptr,'pQryInstrumentOrderCommRate':vars(pQryInstrumentOrderCommRate),'nRequestID':nRequestID}
        req_ret = self.sock_client.send_req(req)
        return req_ret
    def ReqQrySecAgentTradingAccount(self,pQryTradingAccount:CThostFtdcQryTradingAccountField,nRequestID:int):
        req = {'req_id':str(uuid.uuid4()),'cmd':'ReqQrySecAgentTradingAccount','cmd_type':'td','ptr':self.api_ptr,'pQryTradingAccount':vars(pQryTradingAccount),'nRequestID':nRequestID}
        req_ret = self.sock_client.send_req(req)
        return req_ret
    def ReqQrySecAgentCheckMode(self,pQrySecAgentCheckMode:CThostFtdcQrySecAgentCheckModeField,nRequestID:int):
        req = {'req_id':str(uuid.uuid4()),'cmd':'ReqQrySecAgentCheckMode','cmd_type':'td','ptr':self.api_ptr,'pQrySecAgentCheckMode':vars(pQrySecAgentCheckMode),'nRequestID':nRequestID}
        req_ret = self.sock_client.send_req(req)
        return req_ret
    def ReqQrySecAgentTradeInfo(self,pQrySecAgentTradeInfo:CThostFtdcQrySecAgentTradeInfoField,nRequestID:int):
        req = {'req_id':str(uuid.uuid4()),'cmd':'ReqQrySecAgentTradeInfo','cmd_type':'td','ptr':self.api_ptr,'pQrySecAgentTradeInfo':vars(pQrySecAgentTradeInfo),'nRequestID':nRequestID}
        req_ret = self.sock_client.send_req(req)
        return req_ret
    def ReqQryOptionInstrTradeCost(self,pQryOptionInstrTradeCost:CThostFtdcQryOptionInstrTradeCostField,nRequestID:int):
        req = {'req_id':str(uuid.uuid4()),'cmd':'ReqQryOptionInstrTradeCost','cmd_type':'td','ptr':self.api_ptr,'pQryOptionInstrTradeCost':vars(pQryOptionInstrTradeCost),'nRequestID':nRequestID}
        req_ret = self.sock_client.send_req(req)
        return req_ret
    def ReqQryOptionInstrCommRate(self,pQryOptionInstrCommRate:CThostFtdcQryOptionInstrCommRateField,nRequestID:int):
        req = {'req_id':str(uuid.uuid4()),'cmd':'ReqQryOptionInstrCommRate','cmd_type':'td','ptr':self.api_ptr,'pQryOptionInstrCommRate':vars(pQryOptionInstrCommRate),'nRequestID':nRequestID}
        req_ret = self.sock_client.send_req(req)
        return req_ret
    def ReqQryExecOrder(self,pQryExecOrder:CThostFtdcQryExecOrderField,nRequestID:int):
        req = {'req_id':str(uuid.uuid4()),'cmd':'ReqQryExecOrder','cmd_type':'td','ptr':self.api_ptr,'pQryExecOrder':vars(pQryExecOrder),'nRequestID':nRequestID}
        req_ret = self.sock_client.send_req(req)
        return req_ret
    def ReqQryForQuote(self,pQryForQuote:CThostFtdcQryForQuoteField,nRequestID:int):
        req = {'req_id':str(uuid.uuid4()),'cmd':'ReqQryForQuote','cmd_type':'td','ptr':self.api_ptr,'pQryForQuote':vars(pQryForQuote),'nRequestID':nRequestID}
        req_ret = self.sock_client.send_req(req)
        return req_ret
    def ReqQryQuote(self,pQryQuote:CThostFtdcQryQuoteField,nRequestID:int):
        req = {'req_id':str(uuid.uuid4()),'cmd':'ReqQryQuote','cmd_type':'td','ptr':self.api_ptr,'pQryQuote':vars(pQryQuote),'nRequestID':nRequestID}
        req_ret = self.sock_client.send_req(req)
        return req_ret
    def ReqQryOptionSelfClose(self,pQryOptionSelfClose:CThostFtdcQryOptionSelfCloseField,nRequestID:int):
        req = {'req_id':str(uuid.uuid4()),'cmd':'ReqQryOptionSelfClose','cmd_type':'td','ptr':self.api_ptr,'pQryOptionSelfClose':vars(pQryOptionSelfClose),'nRequestID':nRequestID}
        req_ret = self.sock_client.send_req(req)
        return req_ret
    def ReqQryInvestUnit(self,pQryInvestUnit:CThostFtdcQryInvestUnitField,nRequestID:int):
        req = {'req_id':str(uuid.uuid4()),'cmd':'ReqQryInvestUnit','cmd_type':'td','ptr':self.api_ptr,'pQryInvestUnit':vars(pQryInvestUnit),'nRequestID':nRequestID}
        req_ret = self.sock_client.send_req(req)
        return req_ret
    def ReqQryCombInstrumentGuard(self,pQryCombInstrumentGuard:CThostFtdcQryCombInstrumentGuardField,nRequestID:int):
        req = {'req_id':str(uuid.uuid4()),'cmd':'ReqQryCombInstrumentGuard','cmd_type':'td','ptr':self.api_ptr,'pQryCombInstrumentGuard':vars(pQryCombInstrumentGuard),'nRequestID':nRequestID}
        req_ret = self.sock_client.send_req(req)
        return req_ret
    def ReqQryCombAction(self,pQryCombAction:CThostFtdcQryCombActionField,nRequestID:int):
        req = {'req_id':str(uuid.uuid4()),'cmd':'ReqQryCombAction','cmd_type':'td','ptr':self.api_ptr,'pQryCombAction':vars(pQryCombAction),'nRequestID':nRequestID}
        req_ret = self.sock_client.send_req(req)
        return req_ret
    def ReqQryTransferSerial(self,pQryTransferSerial:CThostFtdcQryTransferSerialField,nRequestID:int):
        req = {'req_id':str(uuid.uuid4()),'cmd':'ReqQryTransferSerial','cmd_type':'td','ptr':self.api_ptr,'pQryTransferSerial':vars(pQryTransferSerial),'nRequestID':nRequestID}
        req_ret = self.sock_client.send_req(req)
        return req_ret
    def ReqQryAccountregister(self,pQryAccountregister:CThostFtdcQryAccountregisterField,nRequestID:int):
        req = {'req_id':str(uuid.uuid4()),'cmd':'ReqQryAccountregister','cmd_type':'td','ptr':self.api_ptr,'pQryAccountregister':vars(pQryAccountregister),'nRequestID':nRequestID}
        req_ret = self.sock_client.send_req(req)
        return req_ret
    def ReqQryContractBank(self,pQryContractBank:CThostFtdcQryContractBankField,nRequestID:int):
        req = {'req_id':str(uuid.uuid4()),'cmd':'ReqQryContractBank','cmd_type':'td','ptr':self.api_ptr,'pQryContractBank':vars(pQryContractBank),'nRequestID':nRequestID}
        req_ret = self.sock_client.send_req(req)
        return req_ret
    def ReqQryParkedOrder(self,pQryParkedOrder:CThostFtdcQryParkedOrderField,nRequestID:int):
        req = {'req_id':str(uuid.uuid4()),'cmd':'ReqQryParkedOrder','cmd_type':'td','ptr':self.api_ptr,'pQryParkedOrder':vars(pQryParkedOrder),'nRequestID':nRequestID}
        req_ret = self.sock_client.send_req(req)
        return req_ret
    def ReqQryParkedOrderAction(self,pQryParkedOrderAction:CThostFtdcQryParkedOrderActionField,nRequestID:int):
        req = {'req_id':str(uuid.uuid4()),'cmd':'ReqQryParkedOrderAction','cmd_type':'td','ptr':self.api_ptr,'pQryParkedOrderAction':vars(pQryParkedOrderAction),'nRequestID':nRequestID}
        req_ret = self.sock_client.send_req(req)
        return req_ret
    def ReqQryTradingNotice(self,pQryTradingNotice:CThostFtdcQryTradingNoticeField,nRequestID:int):
        req = {'req_id':str(uuid.uuid4()),'cmd':'ReqQryTradingNotice','cmd_type':'td','ptr':self.api_ptr,'pQryTradingNotice':vars(pQryTradingNotice),'nRequestID':nRequestID}
        req_ret = self.sock_client.send_req(req)
        return req_ret
    def ReqQryBrokerTradingParams(self,pQryBrokerTradingParams:CThostFtdcQryBrokerTradingParamsField,nRequestID:int):
        req = {'req_id':str(uuid.uuid4()),'cmd':'ReqQryBrokerTradingParams','cmd_type':'td','ptr':self.api_ptr,'pQryBrokerTradingParams':vars(pQryBrokerTradingParams),'nRequestID':nRequestID}
        req_ret = self.sock_client.send_req(req)
        return req_ret
    def ReqQryBrokerTradingAlgos(self,pQryBrokerTradingAlgos:CThostFtdcQryBrokerTradingAlgosField,nRequestID:int):
        req = {'req_id':str(uuid.uuid4()),'cmd':'ReqQryBrokerTradingAlgos','cmd_type':'td','ptr':self.api_ptr,'pQryBrokerTradingAlgos':vars(pQryBrokerTradingAlgos),'nRequestID':nRequestID}
        req_ret = self.sock_client.send_req(req)
        return req_ret
    def ReqQueryCFMMCTradingAccountToken(self,pQueryCFMMCTradingAccountToken:CThostFtdcQueryCFMMCTradingAccountTokenField,nRequestID:int):
        req = {'req_id':str(uuid.uuid4()),'cmd':'ReqQueryCFMMCTradingAccountToken','cmd_type':'td','ptr':self.api_ptr,'pQueryCFMMCTradingAccountToken':vars(pQueryCFMMCTradingAccountToken),'nRequestID':nRequestID}
        req_ret = self.sock_client.send_req(req)
        return req_ret
    def ReqFromBankToFutureByFuture(self,pReqTransfer:CThostFtdcReqTransferField,nRequestID:int):
        req = {'req_id':str(uuid.uuid4()),'cmd':'ReqFromBankToFutureByFuture','cmd_type':'td','ptr':self.api_ptr,'pReqTransfer':vars(pReqTransfer),'nRequestID':nRequestID}
        req_ret = self.sock_client.send_req(req)
        return req_ret
    def ReqFromFutureToBankByFuture(self,pReqTransfer:CThostFtdcReqTransferField,nRequestID:int):
        req = {'req_id':str(uuid.uuid4()),'cmd':'ReqFromFutureToBankByFuture','cmd_type':'td','ptr':self.api_ptr,'pReqTransfer':vars(pReqTransfer),'nRequestID':nRequestID}
        req_ret = self.sock_client.send_req(req)
        return req_ret
    def ReqQueryBankAccountMoneyByFuture(self,pReqQueryAccount:CThostFtdcReqQueryAccountField,nRequestID:int):
        req = {'req_id':str(uuid.uuid4()),'cmd':'ReqQueryBankAccountMoneyByFuture','cmd_type':'td','ptr':self.api_ptr,'pReqQueryAccount':vars(pReqQueryAccount),'nRequestID':nRequestID}
        req_ret = self.sock_client.send_req(req)
        return req_ret
    def ReqQryClassifiedInstrument(self,pQryClassifiedInstrument:CThostFtdcQryClassifiedInstrumentField,nRequestID:int):
        req = {'req_id':str(uuid.uuid4()),'cmd':'ReqQryClassifiedInstrument','cmd_type':'td','ptr':self.api_ptr,'pQryClassifiedInstrument':vars(pQryClassifiedInstrument),'nRequestID':nRequestID}
        req_ret = self.sock_client.send_req(req)
        return req_ret
    def ReqQryCombPromotionParam(self,pQryCombPromotionParam:CThostFtdcQryCombPromotionParamField,nRequestID:int):
        req = {'req_id':str(uuid.uuid4()),'cmd':'ReqQryCombPromotionParam','cmd_type':'td','ptr':self.api_ptr,'pQryCombPromotionParam':vars(pQryCombPromotionParam),'nRequestID':nRequestID}
        req_ret = self.sock_client.send_req(req)
        return req_ret
