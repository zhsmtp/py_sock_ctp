#ifndef CPP_CTP_MD_H
#define CPP_CTP_MD_H
#include "ThostFtdcMdApi.h"

#include "socket_wrapper.h"

#include "rapidjson/document.h"
#include "rapidjson/writer.h"
#include "rapidjson/stringbuffer.h"

using namespace std;
using namespace rapidjson;


class MdSpi : public CThostFtdcMdSpi
{
    public:
    Sock_Wrapper *socks = NULL;
    MdSpi(Sock_Wrapper *socks)
    {
        this->socks = socks;
    }
    void OnFrontConnected()
    {
        StringBuffer s;
        Writer<StringBuffer> writer(s);
        writer.StartObject();
        writer.Key("cmd");
        writer.String("OnFrontConnected");
        writer.Key("cmd_type");
        writer.String("md");
        writer.Key("ptr");
        writer.Uint64((uint64_t)this);
        writer.EndObject();
        this->socks->send_rsp(s.GetString());
    }

    void OnFrontDisconnected(int nReason)
    {
        StringBuffer s;
        Writer<StringBuffer> writer(s);
        writer.StartObject();
        writer.Key("cmd");
        writer.String("OnFrontDisconnected");
        writer.Key("cmd_type");
        writer.String("md");
        writer.Key("ptr");
        writer.Uint64((uint64_t)this);
        writer.Key("nReason");
        writer.Int(nReason);
        writer.EndObject();
        this->socks->send_rsp(s.GetString());
    }

    void OnHeartBeatWarning(int nTimeLapse)
    {
        StringBuffer s;
        Writer<StringBuffer> writer(s);
        writer.StartObject();
        writer.Key("cmd");
        writer.String("OnHeartBeatWarning");
        writer.Key("cmd_type");
        writer.String("md");
        writer.Key("ptr");
        writer.Uint64((uint64_t)this);
        writer.Key("nTimeLapse");
        writer.Int(nTimeLapse);
        writer.EndObject();
        this->socks->send_rsp(s.GetString());
    }

    void OnRspUserLogin(CThostFtdcRspUserLoginField * pRspUserLogin, CThostFtdcRspInfoField * pRspInfo, int nRequestID, bool bIsLast)
    {
        StringBuffer s;
        Writer<StringBuffer> writer(s);
        writer.StartObject();
        writer.Key("cmd");
        writer.String("OnRspUserLogin");
        writer.Key("cmd_type");
        writer.String("md");
        writer.Key("ptr");
        writer.Uint64((uint64_t)this);
        CThostFtdcRspUserLoginField local_pRspUserLogin = { 0 };
        if(pRspUserLogin)
        {
            memcpy(&local_pRspUserLogin, pRspUserLogin, sizeof(CThostFtdcRspUserLoginField));
        }
        writer.Key("pRspUserLogin");
        writer.StartObject();
        writer.Key("TradingDay");
        writer.String(g2u(local_pRspUserLogin.TradingDay).c_str());
        writer.Key("LoginTime");
        writer.String(g2u(local_pRspUserLogin.LoginTime).c_str());
        writer.Key("BrokerID");
        writer.String(g2u(local_pRspUserLogin.BrokerID).c_str());
        writer.Key("UserID");
        writer.String(g2u(local_pRspUserLogin.UserID).c_str());
        writer.Key("SystemName");
        writer.String(g2u(local_pRspUserLogin.SystemName).c_str());
        writer.Key("FrontID");
        writer.Int(local_pRspUserLogin.FrontID);
        writer.Key("SessionID");
        writer.Int(local_pRspUserLogin.SessionID);
        writer.Key("MaxOrderRef");
        writer.String(g2u(local_pRspUserLogin.MaxOrderRef).c_str());
        writer.Key("SHFETime");
        writer.String(g2u(local_pRspUserLogin.SHFETime).c_str());
        writer.Key("DCETime");
        writer.String(g2u(local_pRspUserLogin.DCETime).c_str());
        writer.Key("CZCETime");
        writer.String(g2u(local_pRspUserLogin.CZCETime).c_str());
        writer.Key("FFEXTime");
        writer.String(g2u(local_pRspUserLogin.FFEXTime).c_str());
        writer.Key("INETime");
        writer.String(g2u(local_pRspUserLogin.INETime).c_str());
        writer.EndObject();
        CThostFtdcRspInfoField local_pRspInfo = { 0 };
        if(pRspInfo)
        {
            memcpy(&local_pRspInfo, pRspInfo, sizeof(CThostFtdcRspInfoField));
        }
        writer.Key("pRspInfo");
        writer.StartObject();
        writer.Key("ErrorID");
        writer.Int(local_pRspInfo.ErrorID);
        writer.Key("ErrorMsg");
        writer.String(g2u(local_pRspInfo.ErrorMsg).c_str());
        writer.EndObject();
        writer.Key("nRequestID");
        writer.Int(nRequestID);
        writer.Key("bIsLast");
        writer.Bool(bIsLast);
        writer.EndObject();
        this->socks->send_rsp(s.GetString());
    }

    void OnRspUserLogout(CThostFtdcUserLogoutField * pUserLogout, CThostFtdcRspInfoField * pRspInfo, int nRequestID, bool bIsLast)
    {
        StringBuffer s;
        Writer<StringBuffer> writer(s);
        writer.StartObject();
        writer.Key("cmd");
        writer.String("OnRspUserLogout");
        writer.Key("cmd_type");
        writer.String("md");
        writer.Key("ptr");
        writer.Uint64((uint64_t)this);
        CThostFtdcUserLogoutField local_pUserLogout = { 0 };
        if(pUserLogout)
        {
            memcpy(&local_pUserLogout, pUserLogout, sizeof(CThostFtdcUserLogoutField));
        }
        writer.Key("pUserLogout");
        writer.StartObject();
        writer.Key("BrokerID");
        writer.String(g2u(local_pUserLogout.BrokerID).c_str());
        writer.Key("UserID");
        writer.String(g2u(local_pUserLogout.UserID).c_str());
        writer.EndObject();
        CThostFtdcRspInfoField local_pRspInfo = { 0 };
        if(pRspInfo)
        {
            memcpy(&local_pRspInfo, pRspInfo, sizeof(CThostFtdcRspInfoField));
        }
        writer.Key("pRspInfo");
        writer.StartObject();
        writer.Key("ErrorID");
        writer.Int(local_pRspInfo.ErrorID);
        writer.Key("ErrorMsg");
        writer.String(g2u(local_pRspInfo.ErrorMsg).c_str());
        writer.EndObject();
        writer.Key("nRequestID");
        writer.Int(nRequestID);
        writer.Key("bIsLast");
        writer.Bool(bIsLast);
        writer.EndObject();
        this->socks->send_rsp(s.GetString());
    }

    void OnRspQryMulticastInstrument(CThostFtdcMulticastInstrumentField * pMulticastInstrument, CThostFtdcRspInfoField * pRspInfo, int nRequestID, bool bIsLast)
    {
        StringBuffer s;
        Writer<StringBuffer> writer(s);
        writer.StartObject();
        writer.Key("cmd");
        writer.String("OnRspQryMulticastInstrument");
        writer.Key("cmd_type");
        writer.String("md");
        writer.Key("ptr");
        writer.Uint64((uint64_t)this);
        CThostFtdcMulticastInstrumentField local_pMulticastInstrument = { 0 };
        if(pMulticastInstrument)
        {
            memcpy(&local_pMulticastInstrument, pMulticastInstrument, sizeof(CThostFtdcMulticastInstrumentField));
        }
        writer.Key("pMulticastInstrument");
        writer.StartObject();
        writer.Key("TopicID");
        writer.Int(local_pMulticastInstrument.TopicID);
        writer.Key("reserve1");
        writer.String(g2u(local_pMulticastInstrument.reserve1).c_str());
        writer.Key("InstrumentNo");
        writer.Int(local_pMulticastInstrument.InstrumentNo);
        writer.Key("CodePrice");
        writer.Double(local_pMulticastInstrument.CodePrice);
        writer.Key("VolumeMultiple");
        writer.Int(local_pMulticastInstrument.VolumeMultiple);
        writer.Key("PriceTick");
        writer.Double(local_pMulticastInstrument.PriceTick);
        writer.Key("InstrumentID");
        writer.String(g2u(local_pMulticastInstrument.InstrumentID).c_str());
        writer.EndObject();
        CThostFtdcRspInfoField local_pRspInfo = { 0 };
        if(pRspInfo)
        {
            memcpy(&local_pRspInfo, pRspInfo, sizeof(CThostFtdcRspInfoField));
        }
        writer.Key("pRspInfo");
        writer.StartObject();
        writer.Key("ErrorID");
        writer.Int(local_pRspInfo.ErrorID);
        writer.Key("ErrorMsg");
        writer.String(g2u(local_pRspInfo.ErrorMsg).c_str());
        writer.EndObject();
        writer.Key("nRequestID");
        writer.Int(nRequestID);
        writer.Key("bIsLast");
        writer.Bool(bIsLast);
        writer.EndObject();
        this->socks->send_rsp(s.GetString());
    }

    void OnRspError(CThostFtdcRspInfoField * pRspInfo, int nRequestID, bool bIsLast)
    {
        StringBuffer s;
        Writer<StringBuffer> writer(s);
        writer.StartObject();
        writer.Key("cmd");
        writer.String("OnRspError");
        writer.Key("cmd_type");
        writer.String("md");
        writer.Key("ptr");
        writer.Uint64((uint64_t)this);
        CThostFtdcRspInfoField local_pRspInfo = { 0 };
        if(pRspInfo)
        {
            memcpy(&local_pRspInfo, pRspInfo, sizeof(CThostFtdcRspInfoField));
        }
        writer.Key("pRspInfo");
        writer.StartObject();
        writer.Key("ErrorID");
        writer.Int(local_pRspInfo.ErrorID);
        writer.Key("ErrorMsg");
        writer.String(g2u(local_pRspInfo.ErrorMsg).c_str());
        writer.EndObject();
        writer.Key("nRequestID");
        writer.Int(nRequestID);
        writer.Key("bIsLast");
        writer.Bool(bIsLast);
        writer.EndObject();
        this->socks->send_rsp(s.GetString());
    }

    void OnRspSubMarketData(CThostFtdcSpecificInstrumentField * pSpecificInstrument, CThostFtdcRspInfoField * pRspInfo, int nRequestID, bool bIsLast)
    {
        StringBuffer s;
        Writer<StringBuffer> writer(s);
        writer.StartObject();
        writer.Key("cmd");
        writer.String("OnRspSubMarketData");
        writer.Key("cmd_type");
        writer.String("md");
        writer.Key("ptr");
        writer.Uint64((uint64_t)this);
        CThostFtdcSpecificInstrumentField local_pSpecificInstrument = { 0 };
        if(pSpecificInstrument)
        {
            memcpy(&local_pSpecificInstrument, pSpecificInstrument, sizeof(CThostFtdcSpecificInstrumentField));
        }
        writer.Key("pSpecificInstrument");
        writer.StartObject();
        writer.Key("reserve1");
        writer.String(g2u(local_pSpecificInstrument.reserve1).c_str());
        writer.Key("InstrumentID");
        writer.String(g2u(local_pSpecificInstrument.InstrumentID).c_str());
        writer.EndObject();
        CThostFtdcRspInfoField local_pRspInfo = { 0 };
        if(pRspInfo)
        {
            memcpy(&local_pRspInfo, pRspInfo, sizeof(CThostFtdcRspInfoField));
        }
        writer.Key("pRspInfo");
        writer.StartObject();
        writer.Key("ErrorID");
        writer.Int(local_pRspInfo.ErrorID);
        writer.Key("ErrorMsg");
        writer.String(g2u(local_pRspInfo.ErrorMsg).c_str());
        writer.EndObject();
        writer.Key("nRequestID");
        writer.Int(nRequestID);
        writer.Key("bIsLast");
        writer.Bool(bIsLast);
        writer.EndObject();
        this->socks->send_rsp(s.GetString());
    }

    void OnRspUnSubMarketData(CThostFtdcSpecificInstrumentField * pSpecificInstrument, CThostFtdcRspInfoField * pRspInfo, int nRequestID, bool bIsLast)
    {
        StringBuffer s;
        Writer<StringBuffer> writer(s);
        writer.StartObject();
        writer.Key("cmd");
        writer.String("OnRspUnSubMarketData");
        writer.Key("cmd_type");
        writer.String("md");
        writer.Key("ptr");
        writer.Uint64((uint64_t)this);
        CThostFtdcSpecificInstrumentField local_pSpecificInstrument = { 0 };
        if(pSpecificInstrument)
        {
            memcpy(&local_pSpecificInstrument, pSpecificInstrument, sizeof(CThostFtdcSpecificInstrumentField));
        }
        writer.Key("pSpecificInstrument");
        writer.StartObject();
        writer.Key("reserve1");
        writer.String(g2u(local_pSpecificInstrument.reserve1).c_str());
        writer.Key("InstrumentID");
        writer.String(g2u(local_pSpecificInstrument.InstrumentID).c_str());
        writer.EndObject();
        CThostFtdcRspInfoField local_pRspInfo = { 0 };
        if(pRspInfo)
        {
            memcpy(&local_pRspInfo, pRspInfo, sizeof(CThostFtdcRspInfoField));
        }
        writer.Key("pRspInfo");
        writer.StartObject();
        writer.Key("ErrorID");
        writer.Int(local_pRspInfo.ErrorID);
        writer.Key("ErrorMsg");
        writer.String(g2u(local_pRspInfo.ErrorMsg).c_str());
        writer.EndObject();
        writer.Key("nRequestID");
        writer.Int(nRequestID);
        writer.Key("bIsLast");
        writer.Bool(bIsLast);
        writer.EndObject();
        this->socks->send_rsp(s.GetString());
    }

    void OnRspSubForQuoteRsp(CThostFtdcSpecificInstrumentField * pSpecificInstrument, CThostFtdcRspInfoField * pRspInfo, int nRequestID, bool bIsLast)
    {
        StringBuffer s;
        Writer<StringBuffer> writer(s);
        writer.StartObject();
        writer.Key("cmd");
        writer.String("OnRspSubForQuoteRsp");
        writer.Key("cmd_type");
        writer.String("md");
        writer.Key("ptr");
        writer.Uint64((uint64_t)this);
        CThostFtdcSpecificInstrumentField local_pSpecificInstrument = { 0 };
        if(pSpecificInstrument)
        {
            memcpy(&local_pSpecificInstrument, pSpecificInstrument, sizeof(CThostFtdcSpecificInstrumentField));
        }
        writer.Key("pSpecificInstrument");
        writer.StartObject();
        writer.Key("reserve1");
        writer.String(g2u(local_pSpecificInstrument.reserve1).c_str());
        writer.Key("InstrumentID");
        writer.String(g2u(local_pSpecificInstrument.InstrumentID).c_str());
        writer.EndObject();
        CThostFtdcRspInfoField local_pRspInfo = { 0 };
        if(pRspInfo)
        {
            memcpy(&local_pRspInfo, pRspInfo, sizeof(CThostFtdcRspInfoField));
        }
        writer.Key("pRspInfo");
        writer.StartObject();
        writer.Key("ErrorID");
        writer.Int(local_pRspInfo.ErrorID);
        writer.Key("ErrorMsg");
        writer.String(g2u(local_pRspInfo.ErrorMsg).c_str());
        writer.EndObject();
        writer.Key("nRequestID");
        writer.Int(nRequestID);
        writer.Key("bIsLast");
        writer.Bool(bIsLast);
        writer.EndObject();
        this->socks->send_rsp(s.GetString());
    }

    void OnRspUnSubForQuoteRsp(CThostFtdcSpecificInstrumentField * pSpecificInstrument, CThostFtdcRspInfoField * pRspInfo, int nRequestID, bool bIsLast)
    {
        StringBuffer s;
        Writer<StringBuffer> writer(s);
        writer.StartObject();
        writer.Key("cmd");
        writer.String("OnRspUnSubForQuoteRsp");
        writer.Key("cmd_type");
        writer.String("md");
        writer.Key("ptr");
        writer.Uint64((uint64_t)this);
        CThostFtdcSpecificInstrumentField local_pSpecificInstrument = { 0 };
        if(pSpecificInstrument)
        {
            memcpy(&local_pSpecificInstrument, pSpecificInstrument, sizeof(CThostFtdcSpecificInstrumentField));
        }
        writer.Key("pSpecificInstrument");
        writer.StartObject();
        writer.Key("reserve1");
        writer.String(g2u(local_pSpecificInstrument.reserve1).c_str());
        writer.Key("InstrumentID");
        writer.String(g2u(local_pSpecificInstrument.InstrumentID).c_str());
        writer.EndObject();
        CThostFtdcRspInfoField local_pRspInfo = { 0 };
        if(pRspInfo)
        {
            memcpy(&local_pRspInfo, pRspInfo, sizeof(CThostFtdcRspInfoField));
        }
        writer.Key("pRspInfo");
        writer.StartObject();
        writer.Key("ErrorID");
        writer.Int(local_pRspInfo.ErrorID);
        writer.Key("ErrorMsg");
        writer.String(g2u(local_pRspInfo.ErrorMsg).c_str());
        writer.EndObject();
        writer.Key("nRequestID");
        writer.Int(nRequestID);
        writer.Key("bIsLast");
        writer.Bool(bIsLast);
        writer.EndObject();
        this->socks->send_rsp(s.GetString());
    }

    void OnRtnDepthMarketData(CThostFtdcDepthMarketDataField * pDepthMarketData)
    {
        StringBuffer s;
        Writer<StringBuffer> writer(s);
        writer.StartObject();
        writer.Key("cmd");
        writer.String("OnRtnDepthMarketData");
        writer.Key("cmd_type");
        writer.String("md");
        writer.Key("ptr");
        writer.Uint64((uint64_t)this);
        CThostFtdcDepthMarketDataField local_pDepthMarketData = { 0 };
        if(pDepthMarketData)
        {
            memcpy(&local_pDepthMarketData, pDepthMarketData, sizeof(CThostFtdcDepthMarketDataField));
        }
        writer.Key("pDepthMarketData");
        writer.StartObject();
        writer.Key("TradingDay");
        writer.String(g2u(local_pDepthMarketData.TradingDay).c_str());
        writer.Key("reserve1");
        writer.String(g2u(local_pDepthMarketData.reserve1).c_str());
        writer.Key("ExchangeID");
        writer.String(g2u(local_pDepthMarketData.ExchangeID).c_str());
        writer.Key("reserve2");
        writer.String(g2u(local_pDepthMarketData.reserve2).c_str());
        writer.Key("LastPrice");
        writer.Double(local_pDepthMarketData.LastPrice);
        writer.Key("PreSettlementPrice");
        writer.Double(local_pDepthMarketData.PreSettlementPrice);
        writer.Key("PreClosePrice");
        writer.Double(local_pDepthMarketData.PreClosePrice);
        writer.Key("PreOpenInterest");
        writer.Double(local_pDepthMarketData.PreOpenInterest);
        writer.Key("OpenPrice");
        writer.Double(local_pDepthMarketData.OpenPrice);
        writer.Key("HighestPrice");
        writer.Double(local_pDepthMarketData.HighestPrice);
        writer.Key("LowestPrice");
        writer.Double(local_pDepthMarketData.LowestPrice);
        writer.Key("Volume");
        writer.Int(local_pDepthMarketData.Volume);
        writer.Key("Turnover");
        writer.Double(local_pDepthMarketData.Turnover);
        writer.Key("OpenInterest");
        writer.Double(local_pDepthMarketData.OpenInterest);
        writer.Key("ClosePrice");
        writer.Double(local_pDepthMarketData.ClosePrice);
        writer.Key("SettlementPrice");
        writer.Double(local_pDepthMarketData.SettlementPrice);
        writer.Key("UpperLimitPrice");
        writer.Double(local_pDepthMarketData.UpperLimitPrice);
        writer.Key("LowerLimitPrice");
        writer.Double(local_pDepthMarketData.LowerLimitPrice);
        writer.Key("PreDelta");
        writer.Double(local_pDepthMarketData.PreDelta);
        writer.Key("CurrDelta");
        writer.Double(local_pDepthMarketData.CurrDelta);
        writer.Key("UpdateTime");
        writer.String(g2u(local_pDepthMarketData.UpdateTime).c_str());
        writer.Key("UpdateMillisec");
        writer.Int(local_pDepthMarketData.UpdateMillisec);
        writer.Key("BidPrice1");
        writer.Double(local_pDepthMarketData.BidPrice1);
        writer.Key("BidVolume1");
        writer.Int(local_pDepthMarketData.BidVolume1);
        writer.Key("AskPrice1");
        writer.Double(local_pDepthMarketData.AskPrice1);
        writer.Key("AskVolume1");
        writer.Int(local_pDepthMarketData.AskVolume1);
        writer.Key("BidPrice2");
        writer.Double(local_pDepthMarketData.BidPrice2);
        writer.Key("BidVolume2");
        writer.Int(local_pDepthMarketData.BidVolume2);
        writer.Key("AskPrice2");
        writer.Double(local_pDepthMarketData.AskPrice2);
        writer.Key("AskVolume2");
        writer.Int(local_pDepthMarketData.AskVolume2);
        writer.Key("BidPrice3");
        writer.Double(local_pDepthMarketData.BidPrice3);
        writer.Key("BidVolume3");
        writer.Int(local_pDepthMarketData.BidVolume3);
        writer.Key("AskPrice3");
        writer.Double(local_pDepthMarketData.AskPrice3);
        writer.Key("AskVolume3");
        writer.Int(local_pDepthMarketData.AskVolume3);
        writer.Key("BidPrice4");
        writer.Double(local_pDepthMarketData.BidPrice4);
        writer.Key("BidVolume4");
        writer.Int(local_pDepthMarketData.BidVolume4);
        writer.Key("AskPrice4");
        writer.Double(local_pDepthMarketData.AskPrice4);
        writer.Key("AskVolume4");
        writer.Int(local_pDepthMarketData.AskVolume4);
        writer.Key("BidPrice5");
        writer.Double(local_pDepthMarketData.BidPrice5);
        writer.Key("BidVolume5");
        writer.Int(local_pDepthMarketData.BidVolume5);
        writer.Key("AskPrice5");
        writer.Double(local_pDepthMarketData.AskPrice5);
        writer.Key("AskVolume5");
        writer.Int(local_pDepthMarketData.AskVolume5);
        writer.Key("AveragePrice");
        writer.Double(local_pDepthMarketData.AveragePrice);
        writer.Key("ActionDay");
        writer.String(g2u(local_pDepthMarketData.ActionDay).c_str());
        writer.Key("InstrumentID");
        writer.String(g2u(local_pDepthMarketData.InstrumentID).c_str());
        writer.Key("ExchangeInstID");
        writer.String(g2u(local_pDepthMarketData.ExchangeInstID).c_str());
        writer.EndObject();
        writer.EndObject();
        this->socks->send_rsp(s.GetString());
    }

    void OnRtnForQuoteRsp(CThostFtdcForQuoteRspField * pForQuoteRsp)
    {
        StringBuffer s;
        Writer<StringBuffer> writer(s);
        writer.StartObject();
        writer.Key("cmd");
        writer.String("OnRtnForQuoteRsp");
        writer.Key("cmd_type");
        writer.String("md");
        writer.Key("ptr");
        writer.Uint64((uint64_t)this);
        CThostFtdcForQuoteRspField local_pForQuoteRsp = { 0 };
        if(pForQuoteRsp)
        {
            memcpy(&local_pForQuoteRsp, pForQuoteRsp, sizeof(CThostFtdcForQuoteRspField));
        }
        writer.Key("pForQuoteRsp");
        writer.StartObject();
        writer.Key("TradingDay");
        writer.String(g2u(local_pForQuoteRsp.TradingDay).c_str());
        writer.Key("reserve1");
        writer.String(g2u(local_pForQuoteRsp.reserve1).c_str());
        writer.Key("ForQuoteSysID");
        writer.String(g2u(local_pForQuoteRsp.ForQuoteSysID).c_str());
        writer.Key("ForQuoteTime");
        writer.String(g2u(local_pForQuoteRsp.ForQuoteTime).c_str());
        writer.Key("ActionDay");
        writer.String(g2u(local_pForQuoteRsp.ActionDay).c_str());
        writer.Key("ExchangeID");
        writer.String(g2u(local_pForQuoteRsp.ExchangeID).c_str());
        writer.Key("InstrumentID");
        writer.String(g2u(local_pForQuoteRsp.InstrumentID).c_str());
        writer.EndObject();
        writer.EndObject();
        this->socks->send_rsp(s.GetString());
    }

};
#endif
