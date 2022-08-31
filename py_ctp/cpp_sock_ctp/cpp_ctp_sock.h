#ifndef CPP_CTP_SOCK_H
#define CPP_CTP_SOCK_H

#include <mutex>
#include <thread>
#include <vector>

#ifdef _WIN32
#include <winsock2.h>
#define SOCK_TYPE SOCKET
#else
#include <sys/types.h>
#include <sys/socket.h>
#define SOCK_TYPE int
#endif

#include "cpp_ctp_md.h"
#include "cpp_ctp_td.h"
#include "socket_wrapper.h"

#include "rapidjson/document.h"
#include "rapidjson/writer.h"
#include "rapidjson/stringbuffer.h"

using namespace std;
using namespace rapidjson;

class CppCtpSock
{
    public:
    Sock_Wrapper *socks;
    bool bRunning = true;
    
    vector<MdSpi*> mdspi_array;
    vector<TraderSpi*> tdspi_array;
    vector<CThostFtdcMdApi*> mdapi_array;
    vector<CThostFtdcTraderApi*> tdapi_array;
    
    thread recv_thread;
    
    void recv_req_loop()
    {
        while(bRunning)
        {
            if(socks->bConnected)
                recv_req();
        }
        cout << "recv_req_loop() is terminated!" << endl;
    }
    
    CppCtpSock(int port)
    {
        socks = new Sock_Wrapper(port);
        recv_thread = thread(&CppCtpSock::recv_req_loop, this);
        recv_thread.detach();
    }
    
    void clean_up()
    {
        bRunning = false;
        for(auto pMdApi : mdapi_array)
        {
            if(pMdApi)
            {
                cout << "release Md API @ " << (uint64_t) pMdApi<<endl;
                pMdApi->Release();
                pMdApi = NULL;
            }
        }
        mdapi_array.clear();
        for(auto pMdSpi : mdspi_array)
        {
            if(pMdSpi)
            {
                cout << "delete Md SPI @ " << (uint64_t) pMdSpi<<endl;
                delete pMdSpi;
                pMdSpi = NULL;
            }
        }
        mdapi_array.clear();
        for(auto pTdApi : tdapi_array)
        {
            if(pTdApi)
            {
                cout << "release Td API @ " << (uint64_t) pTdApi<<endl;
                pTdApi->Release();
                pTdApi = NULL;
            }
        }
        tdapi_array.clear();
        for(auto pTdSpi : tdspi_array)
        {
            if(pTdSpi)
            {
                cout << "delete Td SPI @ " << (uint64_t) pTdSpi<<endl;
                delete pTdSpi;
                pTdSpi = NULL;
            }
        }
        tdspi_array.clear();
    }
    
    ~CppCtpSock()
    {
        bRunning = false;
        thread clean_up_thread = thread(&CppCtpSock::clean_up, this);
        clean_up_thread.join();
        delete socks;
        socks = NULL;
    }
    
    void recv_req()
    {
        char* req = socks->recv_req();
        if(NULL != req)
            if(strlen(req))
                do_req(req);
    }
    
    void do_req(const char* req)
    {
        StringBuffer s;
        Writer<StringBuffer> writer(s);
        Document d;

        d.Parse(req);

        if(d["ptr"].IsNull())
        {// create spi or static api function
            writer.StartObject();
            writer.Key("req_id");
            writer.String(d["req_id"].GetString());
            writer.Key("value");
            if (0 == strcmp("create_spi", d["cmd"].GetString()))
            {// create spi                
                if (0 == strcmp("md", d["cmd_type"].GetString()))
                {
                    MdSpi* pMdSpi = new MdSpi(this->socks);
                    writer.Uint64((uint64_t)pMdSpi);
                    mdspi_array.push_back(pMdSpi);
                }
                else
                {
                    TraderSpi* pTdSpi = new TraderSpi(this->socks);
                    writer.Uint64((uint64_t)pTdSpi);
                    tdspi_array.push_back(pTdSpi);
                }
            }
            else
            {// call class static function
                if (0 == strcmp("md", d["cmd_type"].GetString()))
                {
                    if (0 == strcmp("CreateFtdcMdApi", d["cmd"].GetString()))
                    {                        
                        CThostFtdcMdApi* pMdApi = CThostFtdcMdApi::CreateFtdcMdApi(d["pszFlowPath"].GetString(),d["bIsUsingUdp"].GetBool(),d["bIsMulticast"].GetBool());
                        writer.Uint64((uint64_t)pMdApi);
                        mdapi_array.push_back(pMdApi);
                    }
                    else if(0 == strcmp("GetApiVersion", d["cmd"].GetString()))
                    {
                        writer.String(CThostFtdcMdApi::GetApiVersion());
                    }
                }
                else
                {
                    if (0 == strcmp("CreateFtdcTraderApi", d["cmd"].GetString()))
                    {
                        CThostFtdcTraderApi* pTdApi = CThostFtdcTraderApi::CreateFtdcTraderApi(d["pszFlowPath"].GetString());
                        writer.Uint64((uint64_t)pTdApi);
                        tdapi_array.push_back(pTdApi);
                    }
                    else if(0 == strcmp("GetApiVersion", d["cmd"].GetString()))
                    {
                        writer.String(CThostFtdcTraderApi::GetApiVersion());
                    }
                }
            }
            writer.EndObject();
        }
        else
        {
            if (0 == strcmp("md", d["cmd_type"].GetString()))
            {
                                if (0 == strcmp("Release", d["cmd"].GetString()))
                {
                    CThostFtdcMdApi* ptr = (CThostFtdcMdApi*)d["ptr"].GetUint64();
                    ptr->Release();
                }
                else if (0 == strcmp("Init", d["cmd"].GetString()))
                {
                    CThostFtdcMdApi* ptr = (CThostFtdcMdApi*)d["ptr"].GetUint64();
                    ptr->Init();
                }
                else if (0 == strcmp("Join", d["cmd"].GetString()))
                {
                    CThostFtdcMdApi* ptr = (CThostFtdcMdApi*)d["ptr"].GetUint64();
                    writer.StartObject();
                    writer.Key("req_id");
                    writer.String(d["req_id"].GetString());
                    writer.Key("value");
                    writer.Int(ptr->Join());
                    writer.EndObject();
                }
                else if (0 == strcmp("GetTradingDay", d["cmd"].GetString()))
                {
                    CThostFtdcMdApi* ptr = (CThostFtdcMdApi*)d["ptr"].GetUint64();
                    writer.StartObject();
                    writer.Key("req_id");
                    writer.String(d["req_id"].GetString());
                    writer.Key("value");
                    writer.String(ptr->GetTradingDay());
                    writer.EndObject();
                }
                else if (0 == strcmp("RegisterFront", d["cmd"].GetString()))
                {
                    CThostFtdcMdApi* ptr = (CThostFtdcMdApi*)d["ptr"].GetUint64();
                    ptr->RegisterFront((char*)d["pszFrontAddress"].GetString());
                }
                else if (0 == strcmp("RegisterNameServer", d["cmd"].GetString()))
                {
                    CThostFtdcMdApi* ptr = (CThostFtdcMdApi*)d["ptr"].GetUint64();
                    ptr->RegisterNameServer((char*)d["pszNsAddress"].GetString());
                }
                else if (0 == strcmp("RegisterFensUserInfo", d["cmd"].GetString()))
                {
                    CThostFtdcMdApi* ptr = (CThostFtdcMdApi*)d["ptr"].GetUint64();
                    CThostFtdcFensUserInfoField cfd = { 0 };
                    auto pObj = d["pFensUserInfo"].GetObject();
                    strcpy(cfd.BrokerID, pObj["BrokerID"].GetString());
                    strcpy(cfd.UserID, pObj["UserID"].GetString());
                    cfd.LoginMode = pObj["LoginMode"].GetString()[0];
                    ptr->RegisterFensUserInfo(&cfd);
                }
                else if (0 == strcmp("RegisterSpi", d["cmd"].GetString()))
                {
                    CThostFtdcMdApi* ptr = (CThostFtdcMdApi*)d["ptr"].GetUint64();
                    ptr->RegisterSpi((CThostFtdcMdSpi *)d["pSpi"].GetUint64());
                }
                else if (0 == strcmp("SubscribeMarketData", d["cmd"].GetString()))
                {
                    CThostFtdcMdApi* ptr = (CThostFtdcMdApi*)d["ptr"].GetUint64();
                    const Value &a = d["ppInstrumentID"].GetArray();
                    int nCount = a.Size();
                    char ** ppList = new char* [nCount];
                    for (int i = 0; i < nCount; i++)
                    {
                        ppList[i] = new char[31];
                        strcpy(ppList[i], a[i].GetString());
                    }
                    writer.StartObject();
                    writer.Key("req_id");
                    writer.String(d["req_id"].GetString());
                    writer.Key("value");
                    writer.Int(ptr->SubscribeMarketData(ppList, d["nCount"].GetInt()));
                    writer.EndObject();
                    for (int i = 0; i < nCount; i++)
                    {
                        delete ppList[i];
                    }
                    delete[] ppList;
                }
                else if (0 == strcmp("UnSubscribeMarketData", d["cmd"].GetString()))
                {
                    CThostFtdcMdApi* ptr = (CThostFtdcMdApi*)d["ptr"].GetUint64();
                    const Value &a = d["ppInstrumentID"].GetArray();
                    int nCount = a.Size();
                    char ** ppList = new char* [nCount];
                    for (int i = 0; i < nCount; i++)
                    {
                        ppList[i] = new char[31];
                        strcpy(ppList[i], a[i].GetString());
                    }
                    writer.StartObject();
                    writer.Key("req_id");
                    writer.String(d["req_id"].GetString());
                    writer.Key("value");
                    writer.Int(ptr->UnSubscribeMarketData(ppList, d["nCount"].GetInt()));
                    writer.EndObject();
                    for (int i = 0; i < nCount; i++)
                    {
                        delete ppList[i];
                    }
                    delete[] ppList;
                }
                else if (0 == strcmp("SubscribeForQuoteRsp", d["cmd"].GetString()))
                {
                    CThostFtdcMdApi* ptr = (CThostFtdcMdApi*)d["ptr"].GetUint64();
                    const Value &a = d["ppInstrumentID"].GetArray();
                    int nCount = a.Size();
                    char ** ppList = new char* [nCount];
                    for (int i = 0; i < nCount; i++)
                    {
                        ppList[i] = new char[31];
                        strcpy(ppList[i], a[i].GetString());
                    }
                    writer.StartObject();
                    writer.Key("req_id");
                    writer.String(d["req_id"].GetString());
                    writer.Key("value");
                    writer.Int(ptr->SubscribeForQuoteRsp(ppList, d["nCount"].GetInt()));
                    writer.EndObject();
                    for (int i = 0; i < nCount; i++)
                    {
                        delete ppList[i];
                    }
                    delete[] ppList;
                }
                else if (0 == strcmp("UnSubscribeForQuoteRsp", d["cmd"].GetString()))
                {
                    CThostFtdcMdApi* ptr = (CThostFtdcMdApi*)d["ptr"].GetUint64();
                    const Value &a = d["ppInstrumentID"].GetArray();
                    int nCount = a.Size();
                    char ** ppList = new char* [nCount];
                    for (int i = 0; i < nCount; i++)
                    {
                        ppList[i] = new char[31];
                        strcpy(ppList[i], a[i].GetString());
                    }
                    writer.StartObject();
                    writer.Key("req_id");
                    writer.String(d["req_id"].GetString());
                    writer.Key("value");
                    writer.Int(ptr->UnSubscribeForQuoteRsp(ppList, d["nCount"].GetInt()));
                    writer.EndObject();
                    for (int i = 0; i < nCount; i++)
                    {
                        delete ppList[i];
                    }
                    delete[] ppList;
                }
                else if (0 == strcmp("ReqUserLogin", d["cmd"].GetString()))
                {
                    CThostFtdcMdApi* ptr = (CThostFtdcMdApi*)d["ptr"].GetUint64();
                    CThostFtdcReqUserLoginField cfd = { 0 };
                    auto pObj = d["pReqUserLoginField"].GetObject();
                    strcpy(cfd.TradingDay, pObj["TradingDay"].GetString());
                    strcpy(cfd.BrokerID, pObj["BrokerID"].GetString());
                    strcpy(cfd.UserID, pObj["UserID"].GetString());
                    strcpy(cfd.Password, pObj["Password"].GetString());
                    strcpy(cfd.UserProductInfo, pObj["UserProductInfo"].GetString());
                    strcpy(cfd.InterfaceProductInfo, pObj["InterfaceProductInfo"].GetString());
                    strcpy(cfd.ProtocolInfo, pObj["ProtocolInfo"].GetString());
                    strcpy(cfd.MacAddress, pObj["MacAddress"].GetString());
                    strcpy(cfd.OneTimePassword, pObj["OneTimePassword"].GetString());
                    strcpy(cfd.reserve1, pObj["reserve1"].GetString());
                    strcpy(cfd.LoginRemark, pObj["LoginRemark"].GetString());
                    cfd.ClientIPPort = pObj["ClientIPPort"].GetInt();
                    strcpy(cfd.ClientIPAddress, pObj["ClientIPAddress"].GetString());
                    writer.StartObject();
                    writer.Key("req_id");
                    writer.String(d["req_id"].GetString());
                    writer.Key("value");
                    writer.Int(ptr->ReqUserLogin(&cfd, d["nRequestID"].GetInt()));
                    writer.EndObject();
                }
                else if (0 == strcmp("ReqUserLogout", d["cmd"].GetString()))
                {
                    CThostFtdcMdApi* ptr = (CThostFtdcMdApi*)d["ptr"].GetUint64();
                    CThostFtdcUserLogoutField cfd = { 0 };
                    auto pObj = d["pUserLogout"].GetObject();
                    strcpy(cfd.BrokerID, pObj["BrokerID"].GetString());
                    strcpy(cfd.UserID, pObj["UserID"].GetString());
                    writer.StartObject();
                    writer.Key("req_id");
                    writer.String(d["req_id"].GetString());
                    writer.Key("value");
                    writer.Int(ptr->ReqUserLogout(&cfd, d["nRequestID"].GetInt()));
                    writer.EndObject();
                }
                else if (0 == strcmp("ReqQryMulticastInstrument", d["cmd"].GetString()))
                {
                    CThostFtdcMdApi* ptr = (CThostFtdcMdApi*)d["ptr"].GetUint64();
                    CThostFtdcQryMulticastInstrumentField cfd = { 0 };
                    auto pObj = d["pQryMulticastInstrument"].GetObject();
                    cfd.TopicID = pObj["TopicID"].GetInt();
                    strcpy(cfd.reserve1, pObj["reserve1"].GetString());
                    strcpy(cfd.InstrumentID, pObj["InstrumentID"].GetString());
                    writer.StartObject();
                    writer.Key("req_id");
                    writer.String(d["req_id"].GetString());
                    writer.Key("value");
                    writer.Int(ptr->ReqQryMulticastInstrument(&cfd, d["nRequestID"].GetInt()));
                    writer.EndObject();
                }
            }
            else
            {
                                if (0 == strcmp("Release", d["cmd"].GetString()))
                {
                    CThostFtdcTraderApi* ptr = (CThostFtdcTraderApi*)d["ptr"].GetUint64();
                    ptr->Release();
                }
                else if (0 == strcmp("Init", d["cmd"].GetString()))
                {
                    CThostFtdcTraderApi* ptr = (CThostFtdcTraderApi*)d["ptr"].GetUint64();
                    ptr->Init();
                }
                else if (0 == strcmp("Join", d["cmd"].GetString()))
                {
                    CThostFtdcTraderApi* ptr = (CThostFtdcTraderApi*)d["ptr"].GetUint64();
                    writer.StartObject();
                    writer.Key("req_id");
                    writer.String(d["req_id"].GetString());
                    writer.Key("value");
                    writer.Int(ptr->Join());
                    writer.EndObject();
                }
                else if (0 == strcmp("GetTradingDay", d["cmd"].GetString()))
                {
                    CThostFtdcTraderApi* ptr = (CThostFtdcTraderApi*)d["ptr"].GetUint64();
                    writer.StartObject();
                    writer.Key("req_id");
                    writer.String(d["req_id"].GetString());
                    writer.Key("value");
                    writer.String(ptr->GetTradingDay());
                    writer.EndObject();
                }
                else if (0 == strcmp("RegisterFront", d["cmd"].GetString()))
                {
                    CThostFtdcTraderApi* ptr = (CThostFtdcTraderApi*)d["ptr"].GetUint64();
                    ptr->RegisterFront((char*)d["pszFrontAddress"].GetString());
                }
                else if (0 == strcmp("RegisterNameServer", d["cmd"].GetString()))
                {
                    CThostFtdcTraderApi* ptr = (CThostFtdcTraderApi*)d["ptr"].GetUint64();
                    ptr->RegisterNameServer((char*)d["pszNsAddress"].GetString());
                }
                else if (0 == strcmp("RegisterFensUserInfo", d["cmd"].GetString()))
                {
                    CThostFtdcTraderApi* ptr = (CThostFtdcTraderApi*)d["ptr"].GetUint64();
                    CThostFtdcFensUserInfoField cfd = { 0 };
                    auto pObj = d["pFensUserInfo"].GetObject();
                    strcpy(cfd.BrokerID, pObj["BrokerID"].GetString());
                    strcpy(cfd.UserID, pObj["UserID"].GetString());
                    cfd.LoginMode = pObj["LoginMode"].GetString()[0];
                    ptr->RegisterFensUserInfo(&cfd);
                }
                else if (0 == strcmp("RegisterSpi", d["cmd"].GetString()))
                {
                    CThostFtdcTraderApi* ptr = (CThostFtdcTraderApi*)d["ptr"].GetUint64();
                    ptr->RegisterSpi((CThostFtdcTraderSpi *)d["pSpi"].GetUint64());
                }
                else if (0 == strcmp("SubscribePrivateTopic", d["cmd"].GetString()))
                {
                    CThostFtdcTraderApi* ptr = (CThostFtdcTraderApi*)d["ptr"].GetUint64();
                    ptr->SubscribePrivateTopic((THOST_TE_RESUME_TYPE)d["nResumeType"].GetInt());
                }
                else if (0 == strcmp("SubscribePublicTopic", d["cmd"].GetString()))
                {
                    CThostFtdcTraderApi* ptr = (CThostFtdcTraderApi*)d["ptr"].GetUint64();
                    ptr->SubscribePublicTopic((THOST_TE_RESUME_TYPE)d["nResumeType"].GetInt());
                }
                else if (0 == strcmp("ReqAuthenticate", d["cmd"].GetString()))
                {
                    CThostFtdcTraderApi* ptr = (CThostFtdcTraderApi*)d["ptr"].GetUint64();
                    CThostFtdcReqAuthenticateField cfd = { 0 };
                    auto pObj = d["pReqAuthenticateField"].GetObject();
                    strcpy(cfd.BrokerID, pObj["BrokerID"].GetString());
                    strcpy(cfd.UserID, pObj["UserID"].GetString());
                    strcpy(cfd.UserProductInfo, pObj["UserProductInfo"].GetString());
                    strcpy(cfd.AuthCode, pObj["AuthCode"].GetString());
                    strcpy(cfd.AppID, pObj["AppID"].GetString());
                    writer.StartObject();
                    writer.Key("req_id");
                    writer.String(d["req_id"].GetString());
                    writer.Key("value");
                    writer.Int(ptr->ReqAuthenticate(&cfd, d["nRequestID"].GetInt()));
                    writer.EndObject();
                }
                else if (0 == strcmp("RegisterUserSystemInfo", d["cmd"].GetString()))
                {
                    CThostFtdcTraderApi* ptr = (CThostFtdcTraderApi*)d["ptr"].GetUint64();
                    CThostFtdcUserSystemInfoField cfd = { 0 };
                    auto pObj = d["pUserSystemInfo"].GetObject();
                    strcpy(cfd.BrokerID, pObj["BrokerID"].GetString());
                    strcpy(cfd.UserID, pObj["UserID"].GetString());
                    cfd.ClientSystemInfoLen = pObj["ClientSystemInfoLen"].GetInt();
                    strcpy(cfd.ClientSystemInfo, pObj["ClientSystemInfo"].GetString());
                    strcpy(cfd.reserve1, pObj["reserve1"].GetString());
                    cfd.ClientIPPort = pObj["ClientIPPort"].GetInt();
                    strcpy(cfd.ClientLoginTime, pObj["ClientLoginTime"].GetString());
                    strcpy(cfd.ClientAppID, pObj["ClientAppID"].GetString());
                    strcpy(cfd.ClientPublicIP, pObj["ClientPublicIP"].GetString());
                    writer.StartObject();
                    writer.Key("req_id");
                    writer.String(d["req_id"].GetString());
                    writer.Key("value");
                    writer.Int(ptr->RegisterUserSystemInfo(&cfd));
                    writer.EndObject();
                }
                else if (0 == strcmp("SubmitUserSystemInfo", d["cmd"].GetString()))
                {
                    CThostFtdcTraderApi* ptr = (CThostFtdcTraderApi*)d["ptr"].GetUint64();
                    CThostFtdcUserSystemInfoField cfd = { 0 };
                    auto pObj = d["pUserSystemInfo"].GetObject();
                    strcpy(cfd.BrokerID, pObj["BrokerID"].GetString());
                    strcpy(cfd.UserID, pObj["UserID"].GetString());
                    cfd.ClientSystemInfoLen = pObj["ClientSystemInfoLen"].GetInt();
                    strcpy(cfd.ClientSystemInfo, pObj["ClientSystemInfo"].GetString());
                    strcpy(cfd.reserve1, pObj["reserve1"].GetString());
                    cfd.ClientIPPort = pObj["ClientIPPort"].GetInt();
                    strcpy(cfd.ClientLoginTime, pObj["ClientLoginTime"].GetString());
                    strcpy(cfd.ClientAppID, pObj["ClientAppID"].GetString());
                    strcpy(cfd.ClientPublicIP, pObj["ClientPublicIP"].GetString());
                    writer.StartObject();
                    writer.Key("req_id");
                    writer.String(d["req_id"].GetString());
                    writer.Key("value");
                    writer.Int(ptr->SubmitUserSystemInfo(&cfd));
                    writer.EndObject();
                }
                else if (0 == strcmp("ReqUserLogin", d["cmd"].GetString()))
                {
                    CThostFtdcTraderApi* ptr = (CThostFtdcTraderApi*)d["ptr"].GetUint64();
                    CThostFtdcReqUserLoginField cfd = { 0 };
                    auto pObj = d["pReqUserLoginField"].GetObject();
                    strcpy(cfd.TradingDay, pObj["TradingDay"].GetString());
                    strcpy(cfd.BrokerID, pObj["BrokerID"].GetString());
                    strcpy(cfd.UserID, pObj["UserID"].GetString());
                    strcpy(cfd.Password, pObj["Password"].GetString());
                    strcpy(cfd.UserProductInfo, pObj["UserProductInfo"].GetString());
                    strcpy(cfd.InterfaceProductInfo, pObj["InterfaceProductInfo"].GetString());
                    strcpy(cfd.ProtocolInfo, pObj["ProtocolInfo"].GetString());
                    strcpy(cfd.MacAddress, pObj["MacAddress"].GetString());
                    strcpy(cfd.OneTimePassword, pObj["OneTimePassword"].GetString());
                    strcpy(cfd.reserve1, pObj["reserve1"].GetString());
                    strcpy(cfd.LoginRemark, pObj["LoginRemark"].GetString());
                    cfd.ClientIPPort = pObj["ClientIPPort"].GetInt();
                    strcpy(cfd.ClientIPAddress, pObj["ClientIPAddress"].GetString());
                    writer.StartObject();
                    writer.Key("req_id");
                    writer.String(d["req_id"].GetString());
                    writer.Key("value");
                    writer.Int(ptr->ReqUserLogin(&cfd, d["nRequestID"].GetInt()));
                    writer.EndObject();
                }
                else if (0 == strcmp("ReqUserLogout", d["cmd"].GetString()))
                {
                    CThostFtdcTraderApi* ptr = (CThostFtdcTraderApi*)d["ptr"].GetUint64();
                    CThostFtdcUserLogoutField cfd = { 0 };
                    auto pObj = d["pUserLogout"].GetObject();
                    strcpy(cfd.BrokerID, pObj["BrokerID"].GetString());
                    strcpy(cfd.UserID, pObj["UserID"].GetString());
                    writer.StartObject();
                    writer.Key("req_id");
                    writer.String(d["req_id"].GetString());
                    writer.Key("value");
                    writer.Int(ptr->ReqUserLogout(&cfd, d["nRequestID"].GetInt()));
                    writer.EndObject();
                }
                else if (0 == strcmp("ReqUserPasswordUpdate", d["cmd"].GetString()))
                {
                    CThostFtdcTraderApi* ptr = (CThostFtdcTraderApi*)d["ptr"].GetUint64();
                    CThostFtdcUserPasswordUpdateField cfd = { 0 };
                    auto pObj = d["pUserPasswordUpdate"].GetObject();
                    strcpy(cfd.BrokerID, pObj["BrokerID"].GetString());
                    strcpy(cfd.UserID, pObj["UserID"].GetString());
                    strcpy(cfd.OldPassword, pObj["OldPassword"].GetString());
                    strcpy(cfd.NewPassword, pObj["NewPassword"].GetString());
                    writer.StartObject();
                    writer.Key("req_id");
                    writer.String(d["req_id"].GetString());
                    writer.Key("value");
                    writer.Int(ptr->ReqUserPasswordUpdate(&cfd, d["nRequestID"].GetInt()));
                    writer.EndObject();
                }
                else if (0 == strcmp("ReqTradingAccountPasswordUpdate", d["cmd"].GetString()))
                {
                    CThostFtdcTraderApi* ptr = (CThostFtdcTraderApi*)d["ptr"].GetUint64();
                    CThostFtdcTradingAccountPasswordUpdateField cfd = { 0 };
                    auto pObj = d["pTradingAccountPasswordUpdate"].GetObject();
                    strcpy(cfd.BrokerID, pObj["BrokerID"].GetString());
                    strcpy(cfd.AccountID, pObj["AccountID"].GetString());
                    strcpy(cfd.OldPassword, pObj["OldPassword"].GetString());
                    strcpy(cfd.NewPassword, pObj["NewPassword"].GetString());
                    strcpy(cfd.CurrencyID, pObj["CurrencyID"].GetString());
                    writer.StartObject();
                    writer.Key("req_id");
                    writer.String(d["req_id"].GetString());
                    writer.Key("value");
                    writer.Int(ptr->ReqTradingAccountPasswordUpdate(&cfd, d["nRequestID"].GetInt()));
                    writer.EndObject();
                }
                else if (0 == strcmp("ReqUserAuthMethod", d["cmd"].GetString()))
                {
                    CThostFtdcTraderApi* ptr = (CThostFtdcTraderApi*)d["ptr"].GetUint64();
                    CThostFtdcReqUserAuthMethodField cfd = { 0 };
                    auto pObj = d["pReqUserAuthMethod"].GetObject();
                    strcpy(cfd.TradingDay, pObj["TradingDay"].GetString());
                    strcpy(cfd.BrokerID, pObj["BrokerID"].GetString());
                    strcpy(cfd.UserID, pObj["UserID"].GetString());
                    writer.StartObject();
                    writer.Key("req_id");
                    writer.String(d["req_id"].GetString());
                    writer.Key("value");
                    writer.Int(ptr->ReqUserAuthMethod(&cfd, d["nRequestID"].GetInt()));
                    writer.EndObject();
                }
                else if (0 == strcmp("ReqGenUserCaptcha", d["cmd"].GetString()))
                {
                    CThostFtdcTraderApi* ptr = (CThostFtdcTraderApi*)d["ptr"].GetUint64();
                    CThostFtdcReqGenUserCaptchaField cfd = { 0 };
                    auto pObj = d["pReqGenUserCaptcha"].GetObject();
                    strcpy(cfd.TradingDay, pObj["TradingDay"].GetString());
                    strcpy(cfd.BrokerID, pObj["BrokerID"].GetString());
                    strcpy(cfd.UserID, pObj["UserID"].GetString());
                    writer.StartObject();
                    writer.Key("req_id");
                    writer.String(d["req_id"].GetString());
                    writer.Key("value");
                    writer.Int(ptr->ReqGenUserCaptcha(&cfd, d["nRequestID"].GetInt()));
                    writer.EndObject();
                }
                else if (0 == strcmp("ReqGenUserText", d["cmd"].GetString()))
                {
                    CThostFtdcTraderApi* ptr = (CThostFtdcTraderApi*)d["ptr"].GetUint64();
                    CThostFtdcReqGenUserTextField cfd = { 0 };
                    auto pObj = d["pReqGenUserText"].GetObject();
                    strcpy(cfd.TradingDay, pObj["TradingDay"].GetString());
                    strcpy(cfd.BrokerID, pObj["BrokerID"].GetString());
                    strcpy(cfd.UserID, pObj["UserID"].GetString());
                    writer.StartObject();
                    writer.Key("req_id");
                    writer.String(d["req_id"].GetString());
                    writer.Key("value");
                    writer.Int(ptr->ReqGenUserText(&cfd, d["nRequestID"].GetInt()));
                    writer.EndObject();
                }
                else if (0 == strcmp("ReqUserLoginWithCaptcha", d["cmd"].GetString()))
                {
                    CThostFtdcTraderApi* ptr = (CThostFtdcTraderApi*)d["ptr"].GetUint64();
                    CThostFtdcReqUserLoginWithCaptchaField cfd = { 0 };
                    auto pObj = d["pReqUserLoginWithCaptcha"].GetObject();
                    strcpy(cfd.TradingDay, pObj["TradingDay"].GetString());
                    strcpy(cfd.BrokerID, pObj["BrokerID"].GetString());
                    strcpy(cfd.UserID, pObj["UserID"].GetString());
                    strcpy(cfd.Password, pObj["Password"].GetString());
                    strcpy(cfd.UserProductInfo, pObj["UserProductInfo"].GetString());
                    strcpy(cfd.InterfaceProductInfo, pObj["InterfaceProductInfo"].GetString());
                    strcpy(cfd.ProtocolInfo, pObj["ProtocolInfo"].GetString());
                    strcpy(cfd.MacAddress, pObj["MacAddress"].GetString());
                    strcpy(cfd.reserve1, pObj["reserve1"].GetString());
                    strcpy(cfd.LoginRemark, pObj["LoginRemark"].GetString());
                    strcpy(cfd.Captcha, pObj["Captcha"].GetString());
                    cfd.ClientIPPort = pObj["ClientIPPort"].GetInt();
                    strcpy(cfd.ClientIPAddress, pObj["ClientIPAddress"].GetString());
                    writer.StartObject();
                    writer.Key("req_id");
                    writer.String(d["req_id"].GetString());
                    writer.Key("value");
                    writer.Int(ptr->ReqUserLoginWithCaptcha(&cfd, d["nRequestID"].GetInt()));
                    writer.EndObject();
                }
                else if (0 == strcmp("ReqUserLoginWithText", d["cmd"].GetString()))
                {
                    CThostFtdcTraderApi* ptr = (CThostFtdcTraderApi*)d["ptr"].GetUint64();
                    CThostFtdcReqUserLoginWithTextField cfd = { 0 };
                    auto pObj = d["pReqUserLoginWithText"].GetObject();
                    strcpy(cfd.TradingDay, pObj["TradingDay"].GetString());
                    strcpy(cfd.BrokerID, pObj["BrokerID"].GetString());
                    strcpy(cfd.UserID, pObj["UserID"].GetString());
                    strcpy(cfd.Password, pObj["Password"].GetString());
                    strcpy(cfd.UserProductInfo, pObj["UserProductInfo"].GetString());
                    strcpy(cfd.InterfaceProductInfo, pObj["InterfaceProductInfo"].GetString());
                    strcpy(cfd.ProtocolInfo, pObj["ProtocolInfo"].GetString());
                    strcpy(cfd.MacAddress, pObj["MacAddress"].GetString());
                    strcpy(cfd.reserve1, pObj["reserve1"].GetString());
                    strcpy(cfd.LoginRemark, pObj["LoginRemark"].GetString());
                    strcpy(cfd.Text, pObj["Text"].GetString());
                    cfd.ClientIPPort = pObj["ClientIPPort"].GetInt();
                    strcpy(cfd.ClientIPAddress, pObj["ClientIPAddress"].GetString());
                    writer.StartObject();
                    writer.Key("req_id");
                    writer.String(d["req_id"].GetString());
                    writer.Key("value");
                    writer.Int(ptr->ReqUserLoginWithText(&cfd, d["nRequestID"].GetInt()));
                    writer.EndObject();
                }
                else if (0 == strcmp("ReqUserLoginWithOTP", d["cmd"].GetString()))
                {
                    CThostFtdcTraderApi* ptr = (CThostFtdcTraderApi*)d["ptr"].GetUint64();
                    CThostFtdcReqUserLoginWithOTPField cfd = { 0 };
                    auto pObj = d["pReqUserLoginWithOTP"].GetObject();
                    strcpy(cfd.TradingDay, pObj["TradingDay"].GetString());
                    strcpy(cfd.BrokerID, pObj["BrokerID"].GetString());
                    strcpy(cfd.UserID, pObj["UserID"].GetString());
                    strcpy(cfd.Password, pObj["Password"].GetString());
                    strcpy(cfd.UserProductInfo, pObj["UserProductInfo"].GetString());
                    strcpy(cfd.InterfaceProductInfo, pObj["InterfaceProductInfo"].GetString());
                    strcpy(cfd.ProtocolInfo, pObj["ProtocolInfo"].GetString());
                    strcpy(cfd.MacAddress, pObj["MacAddress"].GetString());
                    strcpy(cfd.reserve1, pObj["reserve1"].GetString());
                    strcpy(cfd.LoginRemark, pObj["LoginRemark"].GetString());
                    strcpy(cfd.OTPPassword, pObj["OTPPassword"].GetString());
                    cfd.ClientIPPort = pObj["ClientIPPort"].GetInt();
                    strcpy(cfd.ClientIPAddress, pObj["ClientIPAddress"].GetString());
                    writer.StartObject();
                    writer.Key("req_id");
                    writer.String(d["req_id"].GetString());
                    writer.Key("value");
                    writer.Int(ptr->ReqUserLoginWithOTP(&cfd, d["nRequestID"].GetInt()));
                    writer.EndObject();
                }
                else if (0 == strcmp("ReqOrderInsert", d["cmd"].GetString()))
                {
                    CThostFtdcTraderApi* ptr = (CThostFtdcTraderApi*)d["ptr"].GetUint64();
                    CThostFtdcInputOrderField cfd = { 0 };
                    auto pObj = d["pInputOrder"].GetObject();
                    strcpy(cfd.BrokerID, pObj["BrokerID"].GetString());
                    strcpy(cfd.InvestorID, pObj["InvestorID"].GetString());
                    strcpy(cfd.reserve1, pObj["reserve1"].GetString());
                    strcpy(cfd.OrderRef, pObj["OrderRef"].GetString());
                    strcpy(cfd.UserID, pObj["UserID"].GetString());
                    cfd.OrderPriceType = pObj["OrderPriceType"].GetString()[0];
                    cfd.Direction = pObj["Direction"].GetString()[0];
                    strcpy(cfd.CombOffsetFlag, pObj["CombOffsetFlag"].GetString());
                    strcpy(cfd.CombHedgeFlag, pObj["CombHedgeFlag"].GetString());
                    cfd.LimitPrice = pObj["LimitPrice"].GetDouble();
                    cfd.VolumeTotalOriginal = pObj["VolumeTotalOriginal"].GetInt();
                    cfd.TimeCondition = pObj["TimeCondition"].GetString()[0];
                    strcpy(cfd.GTDDate, pObj["GTDDate"].GetString());
                    cfd.VolumeCondition = pObj["VolumeCondition"].GetString()[0];
                    cfd.MinVolume = pObj["MinVolume"].GetInt();
                    cfd.ContingentCondition = pObj["ContingentCondition"].GetString()[0];
                    cfd.StopPrice = pObj["StopPrice"].GetDouble();
                    cfd.ForceCloseReason = pObj["ForceCloseReason"].GetString()[0];
                    cfd.IsAutoSuspend = pObj["IsAutoSuspend"].GetInt();
                    strcpy(cfd.BusinessUnit, pObj["BusinessUnit"].GetString());
                    cfd.RequestID = pObj["RequestID"].GetInt();
                    cfd.UserForceClose = pObj["UserForceClose"].GetInt();
                    cfd.IsSwapOrder = pObj["IsSwapOrder"].GetInt();
                    strcpy(cfd.ExchangeID, pObj["ExchangeID"].GetString());
                    strcpy(cfd.InvestUnitID, pObj["InvestUnitID"].GetString());
                    strcpy(cfd.AccountID, pObj["AccountID"].GetString());
                    strcpy(cfd.CurrencyID, pObj["CurrencyID"].GetString());
                    strcpy(cfd.ClientID, pObj["ClientID"].GetString());
                    strcpy(cfd.reserve2, pObj["reserve2"].GetString());
                    strcpy(cfd.MacAddress, pObj["MacAddress"].GetString());
                    strcpy(cfd.InstrumentID, pObj["InstrumentID"].GetString());
                    strcpy(cfd.IPAddress, pObj["IPAddress"].GetString());
                    writer.StartObject();
                    writer.Key("req_id");
                    writer.String(d["req_id"].GetString());
                    writer.Key("value");
                    writer.Int(ptr->ReqOrderInsert(&cfd, d["nRequestID"].GetInt()));
                    writer.EndObject();
                }
                else if (0 == strcmp("ReqParkedOrderInsert", d["cmd"].GetString()))
                {
                    CThostFtdcTraderApi* ptr = (CThostFtdcTraderApi*)d["ptr"].GetUint64();
                    CThostFtdcParkedOrderField cfd = { 0 };
                    auto pObj = d["pParkedOrder"].GetObject();
                    strcpy(cfd.BrokerID, pObj["BrokerID"].GetString());
                    strcpy(cfd.InvestorID, pObj["InvestorID"].GetString());
                    strcpy(cfd.reserve1, pObj["reserve1"].GetString());
                    strcpy(cfd.OrderRef, pObj["OrderRef"].GetString());
                    strcpy(cfd.UserID, pObj["UserID"].GetString());
                    cfd.OrderPriceType = pObj["OrderPriceType"].GetString()[0];
                    cfd.Direction = pObj["Direction"].GetString()[0];
                    strcpy(cfd.CombOffsetFlag, pObj["CombOffsetFlag"].GetString());
                    strcpy(cfd.CombHedgeFlag, pObj["CombHedgeFlag"].GetString());
                    cfd.LimitPrice = pObj["LimitPrice"].GetDouble();
                    cfd.VolumeTotalOriginal = pObj["VolumeTotalOriginal"].GetInt();
                    cfd.TimeCondition = pObj["TimeCondition"].GetString()[0];
                    strcpy(cfd.GTDDate, pObj["GTDDate"].GetString());
                    cfd.VolumeCondition = pObj["VolumeCondition"].GetString()[0];
                    cfd.MinVolume = pObj["MinVolume"].GetInt();
                    cfd.ContingentCondition = pObj["ContingentCondition"].GetString()[0];
                    cfd.StopPrice = pObj["StopPrice"].GetDouble();
                    cfd.ForceCloseReason = pObj["ForceCloseReason"].GetString()[0];
                    cfd.IsAutoSuspend = pObj["IsAutoSuspend"].GetInt();
                    strcpy(cfd.BusinessUnit, pObj["BusinessUnit"].GetString());
                    cfd.RequestID = pObj["RequestID"].GetInt();
                    cfd.UserForceClose = pObj["UserForceClose"].GetInt();
                    strcpy(cfd.ExchangeID, pObj["ExchangeID"].GetString());
                    strcpy(cfd.ParkedOrderID, pObj["ParkedOrderID"].GetString());
                    cfd.UserType = pObj["UserType"].GetString()[0];
                    cfd.Status = pObj["Status"].GetString()[0];
                    cfd.ErrorID = pObj["ErrorID"].GetInt();
                    strcpy(cfd.ErrorMsg, pObj["ErrorMsg"].GetString());
                    cfd.IsSwapOrder = pObj["IsSwapOrder"].GetInt();
                    strcpy(cfd.AccountID, pObj["AccountID"].GetString());
                    strcpy(cfd.CurrencyID, pObj["CurrencyID"].GetString());
                    strcpy(cfd.ClientID, pObj["ClientID"].GetString());
                    strcpy(cfd.InvestUnitID, pObj["InvestUnitID"].GetString());
                    strcpy(cfd.reserve2, pObj["reserve2"].GetString());
                    strcpy(cfd.MacAddress, pObj["MacAddress"].GetString());
                    strcpy(cfd.InstrumentID, pObj["InstrumentID"].GetString());
                    strcpy(cfd.IPAddress, pObj["IPAddress"].GetString());
                    writer.StartObject();
                    writer.Key("req_id");
                    writer.String(d["req_id"].GetString());
                    writer.Key("value");
                    writer.Int(ptr->ReqParkedOrderInsert(&cfd, d["nRequestID"].GetInt()));
                    writer.EndObject();
                }
                else if (0 == strcmp("ReqParkedOrderAction", d["cmd"].GetString()))
                {
                    CThostFtdcTraderApi* ptr = (CThostFtdcTraderApi*)d["ptr"].GetUint64();
                    CThostFtdcParkedOrderActionField cfd = { 0 };
                    auto pObj = d["pParkedOrderAction"].GetObject();
                    strcpy(cfd.BrokerID, pObj["BrokerID"].GetString());
                    strcpy(cfd.InvestorID, pObj["InvestorID"].GetString());
                    cfd.OrderActionRef = pObj["OrderActionRef"].GetInt();
                    strcpy(cfd.OrderRef, pObj["OrderRef"].GetString());
                    cfd.RequestID = pObj["RequestID"].GetInt();
                    cfd.FrontID = pObj["FrontID"].GetInt();
                    cfd.SessionID = pObj["SessionID"].GetInt();
                    strcpy(cfd.ExchangeID, pObj["ExchangeID"].GetString());
                    strcpy(cfd.OrderSysID, pObj["OrderSysID"].GetString());
                    cfd.ActionFlag = pObj["ActionFlag"].GetString()[0];
                    cfd.LimitPrice = pObj["LimitPrice"].GetDouble();
                    cfd.VolumeChange = pObj["VolumeChange"].GetInt();
                    strcpy(cfd.UserID, pObj["UserID"].GetString());
                    strcpy(cfd.reserve1, pObj["reserve1"].GetString());
                    strcpy(cfd.ParkedOrderActionID, pObj["ParkedOrderActionID"].GetString());
                    cfd.UserType = pObj["UserType"].GetString()[0];
                    cfd.Status = pObj["Status"].GetString()[0];
                    cfd.ErrorID = pObj["ErrorID"].GetInt();
                    strcpy(cfd.ErrorMsg, pObj["ErrorMsg"].GetString());
                    strcpy(cfd.InvestUnitID, pObj["InvestUnitID"].GetString());
                    strcpy(cfd.reserve2, pObj["reserve2"].GetString());
                    strcpy(cfd.MacAddress, pObj["MacAddress"].GetString());
                    strcpy(cfd.InstrumentID, pObj["InstrumentID"].GetString());
                    strcpy(cfd.IPAddress, pObj["IPAddress"].GetString());
                    writer.StartObject();
                    writer.Key("req_id");
                    writer.String(d["req_id"].GetString());
                    writer.Key("value");
                    writer.Int(ptr->ReqParkedOrderAction(&cfd, d["nRequestID"].GetInt()));
                    writer.EndObject();
                }
                else if (0 == strcmp("ReqOrderAction", d["cmd"].GetString()))
                {
                    CThostFtdcTraderApi* ptr = (CThostFtdcTraderApi*)d["ptr"].GetUint64();
                    CThostFtdcInputOrderActionField cfd = { 0 };
                    auto pObj = d["pInputOrderAction"].GetObject();
                    strcpy(cfd.BrokerID, pObj["BrokerID"].GetString());
                    strcpy(cfd.InvestorID, pObj["InvestorID"].GetString());
                    cfd.OrderActionRef = pObj["OrderActionRef"].GetInt();
                    strcpy(cfd.OrderRef, pObj["OrderRef"].GetString());
                    cfd.RequestID = pObj["RequestID"].GetInt();
                    cfd.FrontID = pObj["FrontID"].GetInt();
                    cfd.SessionID = pObj["SessionID"].GetInt();
                    strcpy(cfd.ExchangeID, pObj["ExchangeID"].GetString());
                    strcpy(cfd.OrderSysID, pObj["OrderSysID"].GetString());
                    cfd.ActionFlag = pObj["ActionFlag"].GetString()[0];
                    cfd.LimitPrice = pObj["LimitPrice"].GetDouble();
                    cfd.VolumeChange = pObj["VolumeChange"].GetInt();
                    strcpy(cfd.UserID, pObj["UserID"].GetString());
                    strcpy(cfd.reserve1, pObj["reserve1"].GetString());
                    strcpy(cfd.InvestUnitID, pObj["InvestUnitID"].GetString());
                    strcpy(cfd.reserve2, pObj["reserve2"].GetString());
                    strcpy(cfd.MacAddress, pObj["MacAddress"].GetString());
                    strcpy(cfd.InstrumentID, pObj["InstrumentID"].GetString());
                    strcpy(cfd.IPAddress, pObj["IPAddress"].GetString());
                    writer.StartObject();
                    writer.Key("req_id");
                    writer.String(d["req_id"].GetString());
                    writer.Key("value");
                    writer.Int(ptr->ReqOrderAction(&cfd, d["nRequestID"].GetInt()));
                    writer.EndObject();
                }
                else if (0 == strcmp("ReqQryMaxOrderVolume", d["cmd"].GetString()))
                {
                    CThostFtdcTraderApi* ptr = (CThostFtdcTraderApi*)d["ptr"].GetUint64();
                    CThostFtdcQryMaxOrderVolumeField cfd = { 0 };
                    auto pObj = d["pQryMaxOrderVolume"].GetObject();
                    strcpy(cfd.BrokerID, pObj["BrokerID"].GetString());
                    strcpy(cfd.InvestorID, pObj["InvestorID"].GetString());
                    strcpy(cfd.reserve1, pObj["reserve1"].GetString());
                    cfd.Direction = pObj["Direction"].GetString()[0];
                    cfd.OffsetFlag = pObj["OffsetFlag"].GetString()[0];
                    cfd.HedgeFlag = pObj["HedgeFlag"].GetString()[0];
                    cfd.MaxVolume = pObj["MaxVolume"].GetInt();
                    strcpy(cfd.ExchangeID, pObj["ExchangeID"].GetString());
                    strcpy(cfd.InvestUnitID, pObj["InvestUnitID"].GetString());
                    strcpy(cfd.InstrumentID, pObj["InstrumentID"].GetString());
                    writer.StartObject();
                    writer.Key("req_id");
                    writer.String(d["req_id"].GetString());
                    writer.Key("value");
                    writer.Int(ptr->ReqQryMaxOrderVolume(&cfd, d["nRequestID"].GetInt()));
                    writer.EndObject();
                }
                else if (0 == strcmp("ReqSettlementInfoConfirm", d["cmd"].GetString()))
                {
                    CThostFtdcTraderApi* ptr = (CThostFtdcTraderApi*)d["ptr"].GetUint64();
                    CThostFtdcSettlementInfoConfirmField cfd = { 0 };
                    auto pObj = d["pSettlementInfoConfirm"].GetObject();
                    strcpy(cfd.BrokerID, pObj["BrokerID"].GetString());
                    strcpy(cfd.InvestorID, pObj["InvestorID"].GetString());
                    strcpy(cfd.ConfirmDate, pObj["ConfirmDate"].GetString());
                    strcpy(cfd.ConfirmTime, pObj["ConfirmTime"].GetString());
                    cfd.SettlementID = pObj["SettlementID"].GetInt();
                    strcpy(cfd.AccountID, pObj["AccountID"].GetString());
                    strcpy(cfd.CurrencyID, pObj["CurrencyID"].GetString());
                    writer.StartObject();
                    writer.Key("req_id");
                    writer.String(d["req_id"].GetString());
                    writer.Key("value");
                    writer.Int(ptr->ReqSettlementInfoConfirm(&cfd, d["nRequestID"].GetInt()));
                    writer.EndObject();
                }
                else if (0 == strcmp("ReqRemoveParkedOrder", d["cmd"].GetString()))
                {
                    CThostFtdcTraderApi* ptr = (CThostFtdcTraderApi*)d["ptr"].GetUint64();
                    CThostFtdcRemoveParkedOrderField cfd = { 0 };
                    auto pObj = d["pRemoveParkedOrder"].GetObject();
                    strcpy(cfd.BrokerID, pObj["BrokerID"].GetString());
                    strcpy(cfd.InvestorID, pObj["InvestorID"].GetString());
                    strcpy(cfd.ParkedOrderID, pObj["ParkedOrderID"].GetString());
                    strcpy(cfd.InvestUnitID, pObj["InvestUnitID"].GetString());
                    writer.StartObject();
                    writer.Key("req_id");
                    writer.String(d["req_id"].GetString());
                    writer.Key("value");
                    writer.Int(ptr->ReqRemoveParkedOrder(&cfd, d["nRequestID"].GetInt()));
                    writer.EndObject();
                }
                else if (0 == strcmp("ReqRemoveParkedOrderAction", d["cmd"].GetString()))
                {
                    CThostFtdcTraderApi* ptr = (CThostFtdcTraderApi*)d["ptr"].GetUint64();
                    CThostFtdcRemoveParkedOrderActionField cfd = { 0 };
                    auto pObj = d["pRemoveParkedOrderAction"].GetObject();
                    strcpy(cfd.BrokerID, pObj["BrokerID"].GetString());
                    strcpy(cfd.InvestorID, pObj["InvestorID"].GetString());
                    strcpy(cfd.ParkedOrderActionID, pObj["ParkedOrderActionID"].GetString());
                    strcpy(cfd.InvestUnitID, pObj["InvestUnitID"].GetString());
                    writer.StartObject();
                    writer.Key("req_id");
                    writer.String(d["req_id"].GetString());
                    writer.Key("value");
                    writer.Int(ptr->ReqRemoveParkedOrderAction(&cfd, d["nRequestID"].GetInt()));
                    writer.EndObject();
                }
                else if (0 == strcmp("ReqExecOrderInsert", d["cmd"].GetString()))
                {
                    CThostFtdcTraderApi* ptr = (CThostFtdcTraderApi*)d["ptr"].GetUint64();
                    CThostFtdcInputExecOrderField cfd = { 0 };
                    auto pObj = d["pInputExecOrder"].GetObject();
                    strcpy(cfd.BrokerID, pObj["BrokerID"].GetString());
                    strcpy(cfd.InvestorID, pObj["InvestorID"].GetString());
                    strcpy(cfd.reserve1, pObj["reserve1"].GetString());
                    strcpy(cfd.ExecOrderRef, pObj["ExecOrderRef"].GetString());
                    strcpy(cfd.UserID, pObj["UserID"].GetString());
                    cfd.Volume = pObj["Volume"].GetInt();
                    cfd.RequestID = pObj["RequestID"].GetInt();
                    strcpy(cfd.BusinessUnit, pObj["BusinessUnit"].GetString());
                    cfd.OffsetFlag = pObj["OffsetFlag"].GetString()[0];
                    cfd.HedgeFlag = pObj["HedgeFlag"].GetString()[0];
                    cfd.ActionType = pObj["ActionType"].GetString()[0];
                    cfd.PosiDirection = pObj["PosiDirection"].GetString()[0];
                    cfd.ReservePositionFlag = pObj["ReservePositionFlag"].GetString()[0];
                    cfd.CloseFlag = pObj["CloseFlag"].GetString()[0];
                    strcpy(cfd.ExchangeID, pObj["ExchangeID"].GetString());
                    strcpy(cfd.InvestUnitID, pObj["InvestUnitID"].GetString());
                    strcpy(cfd.AccountID, pObj["AccountID"].GetString());
                    strcpy(cfd.CurrencyID, pObj["CurrencyID"].GetString());
                    strcpy(cfd.ClientID, pObj["ClientID"].GetString());
                    strcpy(cfd.reserve2, pObj["reserve2"].GetString());
                    strcpy(cfd.MacAddress, pObj["MacAddress"].GetString());
                    strcpy(cfd.InstrumentID, pObj["InstrumentID"].GetString());
                    strcpy(cfd.IPAddress, pObj["IPAddress"].GetString());
                    writer.StartObject();
                    writer.Key("req_id");
                    writer.String(d["req_id"].GetString());
                    writer.Key("value");
                    writer.Int(ptr->ReqExecOrderInsert(&cfd, d["nRequestID"].GetInt()));
                    writer.EndObject();
                }
                else if (0 == strcmp("ReqExecOrderAction", d["cmd"].GetString()))
                {
                    CThostFtdcTraderApi* ptr = (CThostFtdcTraderApi*)d["ptr"].GetUint64();
                    CThostFtdcInputExecOrderActionField cfd = { 0 };
                    auto pObj = d["pInputExecOrderAction"].GetObject();
                    strcpy(cfd.BrokerID, pObj["BrokerID"].GetString());
                    strcpy(cfd.InvestorID, pObj["InvestorID"].GetString());
                    cfd.ExecOrderActionRef = pObj["ExecOrderActionRef"].GetInt();
                    strcpy(cfd.ExecOrderRef, pObj["ExecOrderRef"].GetString());
                    cfd.RequestID = pObj["RequestID"].GetInt();
                    cfd.FrontID = pObj["FrontID"].GetInt();
                    cfd.SessionID = pObj["SessionID"].GetInt();
                    strcpy(cfd.ExchangeID, pObj["ExchangeID"].GetString());
                    strcpy(cfd.ExecOrderSysID, pObj["ExecOrderSysID"].GetString());
                    cfd.ActionFlag = pObj["ActionFlag"].GetString()[0];
                    strcpy(cfd.UserID, pObj["UserID"].GetString());
                    strcpy(cfd.reserve1, pObj["reserve1"].GetString());
                    strcpy(cfd.InvestUnitID, pObj["InvestUnitID"].GetString());
                    strcpy(cfd.reserve2, pObj["reserve2"].GetString());
                    strcpy(cfd.MacAddress, pObj["MacAddress"].GetString());
                    strcpy(cfd.InstrumentID, pObj["InstrumentID"].GetString());
                    strcpy(cfd.IPAddress, pObj["IPAddress"].GetString());
                    writer.StartObject();
                    writer.Key("req_id");
                    writer.String(d["req_id"].GetString());
                    writer.Key("value");
                    writer.Int(ptr->ReqExecOrderAction(&cfd, d["nRequestID"].GetInt()));
                    writer.EndObject();
                }
                else if (0 == strcmp("ReqForQuoteInsert", d["cmd"].GetString()))
                {
                    CThostFtdcTraderApi* ptr = (CThostFtdcTraderApi*)d["ptr"].GetUint64();
                    CThostFtdcInputForQuoteField cfd = { 0 };
                    auto pObj = d["pInputForQuote"].GetObject();
                    strcpy(cfd.BrokerID, pObj["BrokerID"].GetString());
                    strcpy(cfd.InvestorID, pObj["InvestorID"].GetString());
                    strcpy(cfd.reserve1, pObj["reserve1"].GetString());
                    strcpy(cfd.ForQuoteRef, pObj["ForQuoteRef"].GetString());
                    strcpy(cfd.UserID, pObj["UserID"].GetString());
                    strcpy(cfd.ExchangeID, pObj["ExchangeID"].GetString());
                    strcpy(cfd.InvestUnitID, pObj["InvestUnitID"].GetString());
                    strcpy(cfd.reserve2, pObj["reserve2"].GetString());
                    strcpy(cfd.MacAddress, pObj["MacAddress"].GetString());
                    strcpy(cfd.InstrumentID, pObj["InstrumentID"].GetString());
                    strcpy(cfd.IPAddress, pObj["IPAddress"].GetString());
                    writer.StartObject();
                    writer.Key("req_id");
                    writer.String(d["req_id"].GetString());
                    writer.Key("value");
                    writer.Int(ptr->ReqForQuoteInsert(&cfd, d["nRequestID"].GetInt()));
                    writer.EndObject();
                }
                else if (0 == strcmp("ReqQuoteInsert", d["cmd"].GetString()))
                {
                    CThostFtdcTraderApi* ptr = (CThostFtdcTraderApi*)d["ptr"].GetUint64();
                    CThostFtdcInputQuoteField cfd = { 0 };
                    auto pObj = d["pInputQuote"].GetObject();
                    strcpy(cfd.BrokerID, pObj["BrokerID"].GetString());
                    strcpy(cfd.InvestorID, pObj["InvestorID"].GetString());
                    strcpy(cfd.reserve1, pObj["reserve1"].GetString());
                    strcpy(cfd.QuoteRef, pObj["QuoteRef"].GetString());
                    strcpy(cfd.UserID, pObj["UserID"].GetString());
                    cfd.AskPrice = pObj["AskPrice"].GetDouble();
                    cfd.BidPrice = pObj["BidPrice"].GetDouble();
                    cfd.AskVolume = pObj["AskVolume"].GetInt();
                    cfd.BidVolume = pObj["BidVolume"].GetInt();
                    cfd.RequestID = pObj["RequestID"].GetInt();
                    strcpy(cfd.BusinessUnit, pObj["BusinessUnit"].GetString());
                    cfd.AskOffsetFlag = pObj["AskOffsetFlag"].GetString()[0];
                    cfd.BidOffsetFlag = pObj["BidOffsetFlag"].GetString()[0];
                    cfd.AskHedgeFlag = pObj["AskHedgeFlag"].GetString()[0];
                    cfd.BidHedgeFlag = pObj["BidHedgeFlag"].GetString()[0];
                    strcpy(cfd.AskOrderRef, pObj["AskOrderRef"].GetString());
                    strcpy(cfd.BidOrderRef, pObj["BidOrderRef"].GetString());
                    strcpy(cfd.ForQuoteSysID, pObj["ForQuoteSysID"].GetString());
                    strcpy(cfd.ExchangeID, pObj["ExchangeID"].GetString());
                    strcpy(cfd.InvestUnitID, pObj["InvestUnitID"].GetString());
                    strcpy(cfd.ClientID, pObj["ClientID"].GetString());
                    strcpy(cfd.reserve2, pObj["reserve2"].GetString());
                    strcpy(cfd.MacAddress, pObj["MacAddress"].GetString());
                    strcpy(cfd.InstrumentID, pObj["InstrumentID"].GetString());
                    strcpy(cfd.IPAddress, pObj["IPAddress"].GetString());
                    writer.StartObject();
                    writer.Key("req_id");
                    writer.String(d["req_id"].GetString());
                    writer.Key("value");
                    writer.Int(ptr->ReqQuoteInsert(&cfd, d["nRequestID"].GetInt()));
                    writer.EndObject();
                }
                else if (0 == strcmp("ReqQuoteAction", d["cmd"].GetString()))
                {
                    CThostFtdcTraderApi* ptr = (CThostFtdcTraderApi*)d["ptr"].GetUint64();
                    CThostFtdcInputQuoteActionField cfd = { 0 };
                    auto pObj = d["pInputQuoteAction"].GetObject();
                    strcpy(cfd.BrokerID, pObj["BrokerID"].GetString());
                    strcpy(cfd.InvestorID, pObj["InvestorID"].GetString());
                    cfd.QuoteActionRef = pObj["QuoteActionRef"].GetInt();
                    strcpy(cfd.QuoteRef, pObj["QuoteRef"].GetString());
                    cfd.RequestID = pObj["RequestID"].GetInt();
                    cfd.FrontID = pObj["FrontID"].GetInt();
                    cfd.SessionID = pObj["SessionID"].GetInt();
                    strcpy(cfd.ExchangeID, pObj["ExchangeID"].GetString());
                    strcpy(cfd.QuoteSysID, pObj["QuoteSysID"].GetString());
                    cfd.ActionFlag = pObj["ActionFlag"].GetString()[0];
                    strcpy(cfd.UserID, pObj["UserID"].GetString());
                    strcpy(cfd.reserve1, pObj["reserve1"].GetString());
                    strcpy(cfd.InvestUnitID, pObj["InvestUnitID"].GetString());
                    strcpy(cfd.ClientID, pObj["ClientID"].GetString());
                    strcpy(cfd.reserve2, pObj["reserve2"].GetString());
                    strcpy(cfd.MacAddress, pObj["MacAddress"].GetString());
                    strcpy(cfd.InstrumentID, pObj["InstrumentID"].GetString());
                    strcpy(cfd.IPAddress, pObj["IPAddress"].GetString());
                    writer.StartObject();
                    writer.Key("req_id");
                    writer.String(d["req_id"].GetString());
                    writer.Key("value");
                    writer.Int(ptr->ReqQuoteAction(&cfd, d["nRequestID"].GetInt()));
                    writer.EndObject();
                }
                else if (0 == strcmp("ReqBatchOrderAction", d["cmd"].GetString()))
                {
                    CThostFtdcTraderApi* ptr = (CThostFtdcTraderApi*)d["ptr"].GetUint64();
                    CThostFtdcInputBatchOrderActionField cfd = { 0 };
                    auto pObj = d["pInputBatchOrderAction"].GetObject();
                    strcpy(cfd.BrokerID, pObj["BrokerID"].GetString());
                    strcpy(cfd.InvestorID, pObj["InvestorID"].GetString());
                    cfd.OrderActionRef = pObj["OrderActionRef"].GetInt();
                    cfd.RequestID = pObj["RequestID"].GetInt();
                    cfd.FrontID = pObj["FrontID"].GetInt();
                    cfd.SessionID = pObj["SessionID"].GetInt();
                    strcpy(cfd.ExchangeID, pObj["ExchangeID"].GetString());
                    strcpy(cfd.UserID, pObj["UserID"].GetString());
                    strcpy(cfd.InvestUnitID, pObj["InvestUnitID"].GetString());
                    strcpy(cfd.reserve1, pObj["reserve1"].GetString());
                    strcpy(cfd.MacAddress, pObj["MacAddress"].GetString());
                    strcpy(cfd.IPAddress, pObj["IPAddress"].GetString());
                    writer.StartObject();
                    writer.Key("req_id");
                    writer.String(d["req_id"].GetString());
                    writer.Key("value");
                    writer.Int(ptr->ReqBatchOrderAction(&cfd, d["nRequestID"].GetInt()));
                    writer.EndObject();
                }
                else if (0 == strcmp("ReqOptionSelfCloseInsert", d["cmd"].GetString()))
                {
                    CThostFtdcTraderApi* ptr = (CThostFtdcTraderApi*)d["ptr"].GetUint64();
                    CThostFtdcInputOptionSelfCloseField cfd = { 0 };
                    auto pObj = d["pInputOptionSelfClose"].GetObject();
                    strcpy(cfd.BrokerID, pObj["BrokerID"].GetString());
                    strcpy(cfd.InvestorID, pObj["InvestorID"].GetString());
                    strcpy(cfd.reserve1, pObj["reserve1"].GetString());
                    strcpy(cfd.OptionSelfCloseRef, pObj["OptionSelfCloseRef"].GetString());
                    strcpy(cfd.UserID, pObj["UserID"].GetString());
                    cfd.Volume = pObj["Volume"].GetInt();
                    cfd.RequestID = pObj["RequestID"].GetInt();
                    strcpy(cfd.BusinessUnit, pObj["BusinessUnit"].GetString());
                    cfd.HedgeFlag = pObj["HedgeFlag"].GetString()[0];
                    cfd.OptSelfCloseFlag = pObj["OptSelfCloseFlag"].GetString()[0];
                    strcpy(cfd.ExchangeID, pObj["ExchangeID"].GetString());
                    strcpy(cfd.InvestUnitID, pObj["InvestUnitID"].GetString());
                    strcpy(cfd.AccountID, pObj["AccountID"].GetString());
                    strcpy(cfd.CurrencyID, pObj["CurrencyID"].GetString());
                    strcpy(cfd.ClientID, pObj["ClientID"].GetString());
                    strcpy(cfd.reserve2, pObj["reserve2"].GetString());
                    strcpy(cfd.MacAddress, pObj["MacAddress"].GetString());
                    strcpy(cfd.InstrumentID, pObj["InstrumentID"].GetString());
                    strcpy(cfd.IPAddress, pObj["IPAddress"].GetString());
                    writer.StartObject();
                    writer.Key("req_id");
                    writer.String(d["req_id"].GetString());
                    writer.Key("value");
                    writer.Int(ptr->ReqOptionSelfCloseInsert(&cfd, d["nRequestID"].GetInt()));
                    writer.EndObject();
                }
                else if (0 == strcmp("ReqOptionSelfCloseAction", d["cmd"].GetString()))
                {
                    CThostFtdcTraderApi* ptr = (CThostFtdcTraderApi*)d["ptr"].GetUint64();
                    CThostFtdcInputOptionSelfCloseActionField cfd = { 0 };
                    auto pObj = d["pInputOptionSelfCloseAction"].GetObject();
                    strcpy(cfd.BrokerID, pObj["BrokerID"].GetString());
                    strcpy(cfd.InvestorID, pObj["InvestorID"].GetString());
                    cfd.OptionSelfCloseActionRef = pObj["OptionSelfCloseActionRef"].GetInt();
                    strcpy(cfd.OptionSelfCloseRef, pObj["OptionSelfCloseRef"].GetString());
                    cfd.RequestID = pObj["RequestID"].GetInt();
                    cfd.FrontID = pObj["FrontID"].GetInt();
                    cfd.SessionID = pObj["SessionID"].GetInt();
                    strcpy(cfd.ExchangeID, pObj["ExchangeID"].GetString());
                    strcpy(cfd.OptionSelfCloseSysID, pObj["OptionSelfCloseSysID"].GetString());
                    cfd.ActionFlag = pObj["ActionFlag"].GetString()[0];
                    strcpy(cfd.UserID, pObj["UserID"].GetString());
                    strcpy(cfd.reserve1, pObj["reserve1"].GetString());
                    strcpy(cfd.InvestUnitID, pObj["InvestUnitID"].GetString());
                    strcpy(cfd.reserve2, pObj["reserve2"].GetString());
                    strcpy(cfd.MacAddress, pObj["MacAddress"].GetString());
                    strcpy(cfd.InstrumentID, pObj["InstrumentID"].GetString());
                    strcpy(cfd.IPAddress, pObj["IPAddress"].GetString());
                    writer.StartObject();
                    writer.Key("req_id");
                    writer.String(d["req_id"].GetString());
                    writer.Key("value");
                    writer.Int(ptr->ReqOptionSelfCloseAction(&cfd, d["nRequestID"].GetInt()));
                    writer.EndObject();
                }
                else if (0 == strcmp("ReqCombActionInsert", d["cmd"].GetString()))
                {
                    CThostFtdcTraderApi* ptr = (CThostFtdcTraderApi*)d["ptr"].GetUint64();
                    CThostFtdcInputCombActionField cfd = { 0 };
                    auto pObj = d["pInputCombAction"].GetObject();
                    strcpy(cfd.BrokerID, pObj["BrokerID"].GetString());
                    strcpy(cfd.InvestorID, pObj["InvestorID"].GetString());
                    strcpy(cfd.reserve1, pObj["reserve1"].GetString());
                    strcpy(cfd.CombActionRef, pObj["CombActionRef"].GetString());
                    strcpy(cfd.UserID, pObj["UserID"].GetString());
                    cfd.Direction = pObj["Direction"].GetString()[0];
                    cfd.Volume = pObj["Volume"].GetInt();
                    cfd.CombDirection = pObj["CombDirection"].GetString()[0];
                    cfd.HedgeFlag = pObj["HedgeFlag"].GetString()[0];
                    strcpy(cfd.ExchangeID, pObj["ExchangeID"].GetString());
                    strcpy(cfd.reserve2, pObj["reserve2"].GetString());
                    strcpy(cfd.MacAddress, pObj["MacAddress"].GetString());
                    strcpy(cfd.InvestUnitID, pObj["InvestUnitID"].GetString());
                    cfd.FrontID = pObj["FrontID"].GetInt();
                    cfd.SessionID = pObj["SessionID"].GetInt();
                    strcpy(cfd.InstrumentID, pObj["InstrumentID"].GetString());
                    strcpy(cfd.IPAddress, pObj["IPAddress"].GetString());
                    writer.StartObject();
                    writer.Key("req_id");
                    writer.String(d["req_id"].GetString());
                    writer.Key("value");
                    writer.Int(ptr->ReqCombActionInsert(&cfd, d["nRequestID"].GetInt()));
                    writer.EndObject();
                }
                else if (0 == strcmp("ReqQryOrder", d["cmd"].GetString()))
                {
                    CThostFtdcTraderApi* ptr = (CThostFtdcTraderApi*)d["ptr"].GetUint64();
                    CThostFtdcQryOrderField cfd = { 0 };
                    auto pObj = d["pQryOrder"].GetObject();
                    strcpy(cfd.BrokerID, pObj["BrokerID"].GetString());
                    strcpy(cfd.InvestorID, pObj["InvestorID"].GetString());
                    strcpy(cfd.reserve1, pObj["reserve1"].GetString());
                    strcpy(cfd.ExchangeID, pObj["ExchangeID"].GetString());
                    strcpy(cfd.OrderSysID, pObj["OrderSysID"].GetString());
                    strcpy(cfd.InsertTimeStart, pObj["InsertTimeStart"].GetString());
                    strcpy(cfd.InsertTimeEnd, pObj["InsertTimeEnd"].GetString());
                    strcpy(cfd.InvestUnitID, pObj["InvestUnitID"].GetString());
                    strcpy(cfd.InstrumentID, pObj["InstrumentID"].GetString());
                    writer.StartObject();
                    writer.Key("req_id");
                    writer.String(d["req_id"].GetString());
                    writer.Key("value");
                    writer.Int(ptr->ReqQryOrder(&cfd, d["nRequestID"].GetInt()));
                    writer.EndObject();
                }
                else if (0 == strcmp("ReqQryTrade", d["cmd"].GetString()))
                {
                    CThostFtdcTraderApi* ptr = (CThostFtdcTraderApi*)d["ptr"].GetUint64();
                    CThostFtdcQryTradeField cfd = { 0 };
                    auto pObj = d["pQryTrade"].GetObject();
                    strcpy(cfd.BrokerID, pObj["BrokerID"].GetString());
                    strcpy(cfd.InvestorID, pObj["InvestorID"].GetString());
                    strcpy(cfd.reserve1, pObj["reserve1"].GetString());
                    strcpy(cfd.ExchangeID, pObj["ExchangeID"].GetString());
                    strcpy(cfd.TradeID, pObj["TradeID"].GetString());
                    strcpy(cfd.TradeTimeStart, pObj["TradeTimeStart"].GetString());
                    strcpy(cfd.TradeTimeEnd, pObj["TradeTimeEnd"].GetString());
                    strcpy(cfd.InvestUnitID, pObj["InvestUnitID"].GetString());
                    strcpy(cfd.InstrumentID, pObj["InstrumentID"].GetString());
                    writer.StartObject();
                    writer.Key("req_id");
                    writer.String(d["req_id"].GetString());
                    writer.Key("value");
                    writer.Int(ptr->ReqQryTrade(&cfd, d["nRequestID"].GetInt()));
                    writer.EndObject();
                }
                else if (0 == strcmp("ReqQryInvestorPosition", d["cmd"].GetString()))
                {
                    CThostFtdcTraderApi* ptr = (CThostFtdcTraderApi*)d["ptr"].GetUint64();
                    CThostFtdcQryInvestorPositionField cfd = { 0 };
                    auto pObj = d["pQryInvestorPosition"].GetObject();
                    strcpy(cfd.BrokerID, pObj["BrokerID"].GetString());
                    strcpy(cfd.InvestorID, pObj["InvestorID"].GetString());
                    strcpy(cfd.reserve1, pObj["reserve1"].GetString());
                    strcpy(cfd.ExchangeID, pObj["ExchangeID"].GetString());
                    strcpy(cfd.InvestUnitID, pObj["InvestUnitID"].GetString());
                    strcpy(cfd.InstrumentID, pObj["InstrumentID"].GetString());
                    writer.StartObject();
                    writer.Key("req_id");
                    writer.String(d["req_id"].GetString());
                    writer.Key("value");
                    writer.Int(ptr->ReqQryInvestorPosition(&cfd, d["nRequestID"].GetInt()));
                    writer.EndObject();
                }
                else if (0 == strcmp("ReqQryTradingAccount", d["cmd"].GetString()))
                {
                    CThostFtdcTraderApi* ptr = (CThostFtdcTraderApi*)d["ptr"].GetUint64();
                    CThostFtdcQryTradingAccountField cfd = { 0 };
                    auto pObj = d["pQryTradingAccount"].GetObject();
                    strcpy(cfd.BrokerID, pObj["BrokerID"].GetString());
                    strcpy(cfd.InvestorID, pObj["InvestorID"].GetString());
                    strcpy(cfd.CurrencyID, pObj["CurrencyID"].GetString());
                    cfd.BizType = pObj["BizType"].GetString()[0];
                    strcpy(cfd.AccountID, pObj["AccountID"].GetString());
                    writer.StartObject();
                    writer.Key("req_id");
                    writer.String(d["req_id"].GetString());
                    writer.Key("value");
                    writer.Int(ptr->ReqQryTradingAccount(&cfd, d["nRequestID"].GetInt()));
                    writer.EndObject();
                }
                else if (0 == strcmp("ReqQryInvestor", d["cmd"].GetString()))
                {
                    CThostFtdcTraderApi* ptr = (CThostFtdcTraderApi*)d["ptr"].GetUint64();
                    CThostFtdcQryInvestorField cfd = { 0 };
                    auto pObj = d["pQryInvestor"].GetObject();
                    strcpy(cfd.BrokerID, pObj["BrokerID"].GetString());
                    strcpy(cfd.InvestorID, pObj["InvestorID"].GetString());
                    writer.StartObject();
                    writer.Key("req_id");
                    writer.String(d["req_id"].GetString());
                    writer.Key("value");
                    writer.Int(ptr->ReqQryInvestor(&cfd, d["nRequestID"].GetInt()));
                    writer.EndObject();
                }
                else if (0 == strcmp("ReqQryTradingCode", d["cmd"].GetString()))
                {
                    CThostFtdcTraderApi* ptr = (CThostFtdcTraderApi*)d["ptr"].GetUint64();
                    CThostFtdcQryTradingCodeField cfd = { 0 };
                    auto pObj = d["pQryTradingCode"].GetObject();
                    strcpy(cfd.BrokerID, pObj["BrokerID"].GetString());
                    strcpy(cfd.InvestorID, pObj["InvestorID"].GetString());
                    strcpy(cfd.ExchangeID, pObj["ExchangeID"].GetString());
                    strcpy(cfd.ClientID, pObj["ClientID"].GetString());
                    cfd.ClientIDType = pObj["ClientIDType"].GetString()[0];
                    strcpy(cfd.InvestUnitID, pObj["InvestUnitID"].GetString());
                    writer.StartObject();
                    writer.Key("req_id");
                    writer.String(d["req_id"].GetString());
                    writer.Key("value");
                    writer.Int(ptr->ReqQryTradingCode(&cfd, d["nRequestID"].GetInt()));
                    writer.EndObject();
                }
                else if (0 == strcmp("ReqQryInstrumentMarginRate", d["cmd"].GetString()))
                {
                    CThostFtdcTraderApi* ptr = (CThostFtdcTraderApi*)d["ptr"].GetUint64();
                    CThostFtdcQryInstrumentMarginRateField cfd = { 0 };
                    auto pObj = d["pQryInstrumentMarginRate"].GetObject();
                    strcpy(cfd.BrokerID, pObj["BrokerID"].GetString());
                    strcpy(cfd.InvestorID, pObj["InvestorID"].GetString());
                    strcpy(cfd.reserve1, pObj["reserve1"].GetString());
                    cfd.HedgeFlag = pObj["HedgeFlag"].GetString()[0];
                    strcpy(cfd.ExchangeID, pObj["ExchangeID"].GetString());
                    strcpy(cfd.InvestUnitID, pObj["InvestUnitID"].GetString());
                    strcpy(cfd.InstrumentID, pObj["InstrumentID"].GetString());
                    writer.StartObject();
                    writer.Key("req_id");
                    writer.String(d["req_id"].GetString());
                    writer.Key("value");
                    writer.Int(ptr->ReqQryInstrumentMarginRate(&cfd, d["nRequestID"].GetInt()));
                    writer.EndObject();
                }
                else if (0 == strcmp("ReqQryInstrumentCommissionRate", d["cmd"].GetString()))
                {
                    CThostFtdcTraderApi* ptr = (CThostFtdcTraderApi*)d["ptr"].GetUint64();
                    CThostFtdcQryInstrumentCommissionRateField cfd = { 0 };
                    auto pObj = d["pQryInstrumentCommissionRate"].GetObject();
                    strcpy(cfd.BrokerID, pObj["BrokerID"].GetString());
                    strcpy(cfd.InvestorID, pObj["InvestorID"].GetString());
                    strcpy(cfd.reserve1, pObj["reserve1"].GetString());
                    strcpy(cfd.ExchangeID, pObj["ExchangeID"].GetString());
                    strcpy(cfd.InvestUnitID, pObj["InvestUnitID"].GetString());
                    strcpy(cfd.InstrumentID, pObj["InstrumentID"].GetString());
                    writer.StartObject();
                    writer.Key("req_id");
                    writer.String(d["req_id"].GetString());
                    writer.Key("value");
                    writer.Int(ptr->ReqQryInstrumentCommissionRate(&cfd, d["nRequestID"].GetInt()));
                    writer.EndObject();
                }
                else if (0 == strcmp("ReqQryExchange", d["cmd"].GetString()))
                {
                    CThostFtdcTraderApi* ptr = (CThostFtdcTraderApi*)d["ptr"].GetUint64();
                    CThostFtdcQryExchangeField cfd = { 0 };
                    auto pObj = d["pQryExchange"].GetObject();
                    strcpy(cfd.ExchangeID, pObj["ExchangeID"].GetString());
                    writer.StartObject();
                    writer.Key("req_id");
                    writer.String(d["req_id"].GetString());
                    writer.Key("value");
                    writer.Int(ptr->ReqQryExchange(&cfd, d["nRequestID"].GetInt()));
                    writer.EndObject();
                }
                else if (0 == strcmp("ReqQryProduct", d["cmd"].GetString()))
                {
                    CThostFtdcTraderApi* ptr = (CThostFtdcTraderApi*)d["ptr"].GetUint64();
                    CThostFtdcQryProductField cfd = { 0 };
                    auto pObj = d["pQryProduct"].GetObject();
                    strcpy(cfd.reserve1, pObj["reserve1"].GetString());
                    cfd.ProductClass = pObj["ProductClass"].GetString()[0];
                    strcpy(cfd.ExchangeID, pObj["ExchangeID"].GetString());
                    strcpy(cfd.ProductID, pObj["ProductID"].GetString());
                    writer.StartObject();
                    writer.Key("req_id");
                    writer.String(d["req_id"].GetString());
                    writer.Key("value");
                    writer.Int(ptr->ReqQryProduct(&cfd, d["nRequestID"].GetInt()));
                    writer.EndObject();
                }
                else if (0 == strcmp("ReqQryInstrument", d["cmd"].GetString()))
                {
                    CThostFtdcTraderApi* ptr = (CThostFtdcTraderApi*)d["ptr"].GetUint64();
                    CThostFtdcQryInstrumentField cfd = { 0 };
                    auto pObj = d["pQryInstrument"].GetObject();
                    strcpy(cfd.reserve1, pObj["reserve1"].GetString());
                    strcpy(cfd.ExchangeID, pObj["ExchangeID"].GetString());
                    strcpy(cfd.reserve2, pObj["reserve2"].GetString());
                    strcpy(cfd.reserve3, pObj["reserve3"].GetString());
                    strcpy(cfd.InstrumentID, pObj["InstrumentID"].GetString());
                    strcpy(cfd.ExchangeInstID, pObj["ExchangeInstID"].GetString());
                    strcpy(cfd.ProductID, pObj["ProductID"].GetString());
                    writer.StartObject();
                    writer.Key("req_id");
                    writer.String(d["req_id"].GetString());
                    writer.Key("value");
                    writer.Int(ptr->ReqQryInstrument(&cfd, d["nRequestID"].GetInt()));
                    writer.EndObject();
                }
                else if (0 == strcmp("ReqQryDepthMarketData", d["cmd"].GetString()))
                {
                    CThostFtdcTraderApi* ptr = (CThostFtdcTraderApi*)d["ptr"].GetUint64();
                    CThostFtdcQryDepthMarketDataField cfd = { 0 };
                    auto pObj = d["pQryDepthMarketData"].GetObject();
                    strcpy(cfd.reserve1, pObj["reserve1"].GetString());
                    strcpy(cfd.ExchangeID, pObj["ExchangeID"].GetString());
                    strcpy(cfd.InstrumentID, pObj["InstrumentID"].GetString());
                    writer.StartObject();
                    writer.Key("req_id");
                    writer.String(d["req_id"].GetString());
                    writer.Key("value");
                    writer.Int(ptr->ReqQryDepthMarketData(&cfd, d["nRequestID"].GetInt()));
                    writer.EndObject();
                }
                else if (0 == strcmp("ReqQrySettlementInfo", d["cmd"].GetString()))
                {
                    CThostFtdcTraderApi* ptr = (CThostFtdcTraderApi*)d["ptr"].GetUint64();
                    CThostFtdcQrySettlementInfoField cfd = { 0 };
                    auto pObj = d["pQrySettlementInfo"].GetObject();
                    strcpy(cfd.BrokerID, pObj["BrokerID"].GetString());
                    strcpy(cfd.InvestorID, pObj["InvestorID"].GetString());
                    strcpy(cfd.TradingDay, pObj["TradingDay"].GetString());
                    strcpy(cfd.AccountID, pObj["AccountID"].GetString());
                    strcpy(cfd.CurrencyID, pObj["CurrencyID"].GetString());
                    writer.StartObject();
                    writer.Key("req_id");
                    writer.String(d["req_id"].GetString());
                    writer.Key("value");
                    writer.Int(ptr->ReqQrySettlementInfo(&cfd, d["nRequestID"].GetInt()));
                    writer.EndObject();
                }
                else if (0 == strcmp("ReqQryTransferBank", d["cmd"].GetString()))
                {
                    CThostFtdcTraderApi* ptr = (CThostFtdcTraderApi*)d["ptr"].GetUint64();
                    CThostFtdcQryTransferBankField cfd = { 0 };
                    auto pObj = d["pQryTransferBank"].GetObject();
                    strcpy(cfd.BankID, pObj["BankID"].GetString());
                    strcpy(cfd.BankBrchID, pObj["BankBrchID"].GetString());
                    writer.StartObject();
                    writer.Key("req_id");
                    writer.String(d["req_id"].GetString());
                    writer.Key("value");
                    writer.Int(ptr->ReqQryTransferBank(&cfd, d["nRequestID"].GetInt()));
                    writer.EndObject();
                }
                else if (0 == strcmp("ReqQryInvestorPositionDetail", d["cmd"].GetString()))
                {
                    CThostFtdcTraderApi* ptr = (CThostFtdcTraderApi*)d["ptr"].GetUint64();
                    CThostFtdcQryInvestorPositionDetailField cfd = { 0 };
                    auto pObj = d["pQryInvestorPositionDetail"].GetObject();
                    strcpy(cfd.BrokerID, pObj["BrokerID"].GetString());
                    strcpy(cfd.InvestorID, pObj["InvestorID"].GetString());
                    strcpy(cfd.reserve1, pObj["reserve1"].GetString());
                    strcpy(cfd.ExchangeID, pObj["ExchangeID"].GetString());
                    strcpy(cfd.InvestUnitID, pObj["InvestUnitID"].GetString());
                    strcpy(cfd.InstrumentID, pObj["InstrumentID"].GetString());
                    writer.StartObject();
                    writer.Key("req_id");
                    writer.String(d["req_id"].GetString());
                    writer.Key("value");
                    writer.Int(ptr->ReqQryInvestorPositionDetail(&cfd, d["nRequestID"].GetInt()));
                    writer.EndObject();
                }
                else if (0 == strcmp("ReqQryNotice", d["cmd"].GetString()))
                {
                    CThostFtdcTraderApi* ptr = (CThostFtdcTraderApi*)d["ptr"].GetUint64();
                    CThostFtdcQryNoticeField cfd = { 0 };
                    auto pObj = d["pQryNotice"].GetObject();
                    strcpy(cfd.BrokerID, pObj["BrokerID"].GetString());
                    writer.StartObject();
                    writer.Key("req_id");
                    writer.String(d["req_id"].GetString());
                    writer.Key("value");
                    writer.Int(ptr->ReqQryNotice(&cfd, d["nRequestID"].GetInt()));
                    writer.EndObject();
                }
                else if (0 == strcmp("ReqQrySettlementInfoConfirm", d["cmd"].GetString()))
                {
                    CThostFtdcTraderApi* ptr = (CThostFtdcTraderApi*)d["ptr"].GetUint64();
                    CThostFtdcQrySettlementInfoConfirmField cfd = { 0 };
                    auto pObj = d["pQrySettlementInfoConfirm"].GetObject();
                    strcpy(cfd.BrokerID, pObj["BrokerID"].GetString());
                    strcpy(cfd.InvestorID, pObj["InvestorID"].GetString());
                    strcpy(cfd.AccountID, pObj["AccountID"].GetString());
                    strcpy(cfd.CurrencyID, pObj["CurrencyID"].GetString());
                    writer.StartObject();
                    writer.Key("req_id");
                    writer.String(d["req_id"].GetString());
                    writer.Key("value");
                    writer.Int(ptr->ReqQrySettlementInfoConfirm(&cfd, d["nRequestID"].GetInt()));
                    writer.EndObject();
                }
                else if (0 == strcmp("ReqQryInvestorPositionCombineDetail", d["cmd"].GetString()))
                {
                    CThostFtdcTraderApi* ptr = (CThostFtdcTraderApi*)d["ptr"].GetUint64();
                    CThostFtdcQryInvestorPositionCombineDetailField cfd = { 0 };
                    auto pObj = d["pQryInvestorPositionCombineDetail"].GetObject();
                    strcpy(cfd.BrokerID, pObj["BrokerID"].GetString());
                    strcpy(cfd.InvestorID, pObj["InvestorID"].GetString());
                    strcpy(cfd.reserve1, pObj["reserve1"].GetString());
                    strcpy(cfd.ExchangeID, pObj["ExchangeID"].GetString());
                    strcpy(cfd.InvestUnitID, pObj["InvestUnitID"].GetString());
                    strcpy(cfd.CombInstrumentID, pObj["CombInstrumentID"].GetString());
                    writer.StartObject();
                    writer.Key("req_id");
                    writer.String(d["req_id"].GetString());
                    writer.Key("value");
                    writer.Int(ptr->ReqQryInvestorPositionCombineDetail(&cfd, d["nRequestID"].GetInt()));
                    writer.EndObject();
                }
                else if (0 == strcmp("ReqQryCFMMCTradingAccountKey", d["cmd"].GetString()))
                {
                    CThostFtdcTraderApi* ptr = (CThostFtdcTraderApi*)d["ptr"].GetUint64();
                    CThostFtdcQryCFMMCTradingAccountKeyField cfd = { 0 };
                    auto pObj = d["pQryCFMMCTradingAccountKey"].GetObject();
                    strcpy(cfd.BrokerID, pObj["BrokerID"].GetString());
                    strcpy(cfd.InvestorID, pObj["InvestorID"].GetString());
                    writer.StartObject();
                    writer.Key("req_id");
                    writer.String(d["req_id"].GetString());
                    writer.Key("value");
                    writer.Int(ptr->ReqQryCFMMCTradingAccountKey(&cfd, d["nRequestID"].GetInt()));
                    writer.EndObject();
                }
                else if (0 == strcmp("ReqQryEWarrantOffset", d["cmd"].GetString()))
                {
                    CThostFtdcTraderApi* ptr = (CThostFtdcTraderApi*)d["ptr"].GetUint64();
                    CThostFtdcQryEWarrantOffsetField cfd = { 0 };
                    auto pObj = d["pQryEWarrantOffset"].GetObject();
                    strcpy(cfd.BrokerID, pObj["BrokerID"].GetString());
                    strcpy(cfd.InvestorID, pObj["InvestorID"].GetString());
                    strcpy(cfd.ExchangeID, pObj["ExchangeID"].GetString());
                    strcpy(cfd.reserve1, pObj["reserve1"].GetString());
                    strcpy(cfd.InvestUnitID, pObj["InvestUnitID"].GetString());
                    strcpy(cfd.InstrumentID, pObj["InstrumentID"].GetString());
                    writer.StartObject();
                    writer.Key("req_id");
                    writer.String(d["req_id"].GetString());
                    writer.Key("value");
                    writer.Int(ptr->ReqQryEWarrantOffset(&cfd, d["nRequestID"].GetInt()));
                    writer.EndObject();
                }
                else if (0 == strcmp("ReqQryInvestorProductGroupMargin", d["cmd"].GetString()))
                {
                    CThostFtdcTraderApi* ptr = (CThostFtdcTraderApi*)d["ptr"].GetUint64();
                    CThostFtdcQryInvestorProductGroupMarginField cfd = { 0 };
                    auto pObj = d["pQryInvestorProductGroupMargin"].GetObject();
                    strcpy(cfd.BrokerID, pObj["BrokerID"].GetString());
                    strcpy(cfd.InvestorID, pObj["InvestorID"].GetString());
                    strcpy(cfd.reserve1, pObj["reserve1"].GetString());
                    cfd.HedgeFlag = pObj["HedgeFlag"].GetString()[0];
                    strcpy(cfd.ExchangeID, pObj["ExchangeID"].GetString());
                    strcpy(cfd.InvestUnitID, pObj["InvestUnitID"].GetString());
                    strcpy(cfd.ProductGroupID, pObj["ProductGroupID"].GetString());
                    writer.StartObject();
                    writer.Key("req_id");
                    writer.String(d["req_id"].GetString());
                    writer.Key("value");
                    writer.Int(ptr->ReqQryInvestorProductGroupMargin(&cfd, d["nRequestID"].GetInt()));
                    writer.EndObject();
                }
                else if (0 == strcmp("ReqQryExchangeMarginRate", d["cmd"].GetString()))
                {
                    CThostFtdcTraderApi* ptr = (CThostFtdcTraderApi*)d["ptr"].GetUint64();
                    CThostFtdcQryExchangeMarginRateField cfd = { 0 };
                    auto pObj = d["pQryExchangeMarginRate"].GetObject();
                    strcpy(cfd.BrokerID, pObj["BrokerID"].GetString());
                    strcpy(cfd.reserve1, pObj["reserve1"].GetString());
                    cfd.HedgeFlag = pObj["HedgeFlag"].GetString()[0];
                    strcpy(cfd.ExchangeID, pObj["ExchangeID"].GetString());
                    strcpy(cfd.InstrumentID, pObj["InstrumentID"].GetString());
                    writer.StartObject();
                    writer.Key("req_id");
                    writer.String(d["req_id"].GetString());
                    writer.Key("value");
                    writer.Int(ptr->ReqQryExchangeMarginRate(&cfd, d["nRequestID"].GetInt()));
                    writer.EndObject();
                }
                else if (0 == strcmp("ReqQryExchangeMarginRateAdjust", d["cmd"].GetString()))
                {
                    CThostFtdcTraderApi* ptr = (CThostFtdcTraderApi*)d["ptr"].GetUint64();
                    CThostFtdcQryExchangeMarginRateAdjustField cfd = { 0 };
                    auto pObj = d["pQryExchangeMarginRateAdjust"].GetObject();
                    strcpy(cfd.BrokerID, pObj["BrokerID"].GetString());
                    strcpy(cfd.reserve1, pObj["reserve1"].GetString());
                    cfd.HedgeFlag = pObj["HedgeFlag"].GetString()[0];
                    strcpy(cfd.InstrumentID, pObj["InstrumentID"].GetString());
                    writer.StartObject();
                    writer.Key("req_id");
                    writer.String(d["req_id"].GetString());
                    writer.Key("value");
                    writer.Int(ptr->ReqQryExchangeMarginRateAdjust(&cfd, d["nRequestID"].GetInt()));
                    writer.EndObject();
                }
                else if (0 == strcmp("ReqQryExchangeRate", d["cmd"].GetString()))
                {
                    CThostFtdcTraderApi* ptr = (CThostFtdcTraderApi*)d["ptr"].GetUint64();
                    CThostFtdcQryExchangeRateField cfd = { 0 };
                    auto pObj = d["pQryExchangeRate"].GetObject();
                    strcpy(cfd.BrokerID, pObj["BrokerID"].GetString());
                    strcpy(cfd.FromCurrencyID, pObj["FromCurrencyID"].GetString());
                    strcpy(cfd.ToCurrencyID, pObj["ToCurrencyID"].GetString());
                    writer.StartObject();
                    writer.Key("req_id");
                    writer.String(d["req_id"].GetString());
                    writer.Key("value");
                    writer.Int(ptr->ReqQryExchangeRate(&cfd, d["nRequestID"].GetInt()));
                    writer.EndObject();
                }
                else if (0 == strcmp("ReqQrySecAgentACIDMap", d["cmd"].GetString()))
                {
                    CThostFtdcTraderApi* ptr = (CThostFtdcTraderApi*)d["ptr"].GetUint64();
                    CThostFtdcQrySecAgentACIDMapField cfd = { 0 };
                    auto pObj = d["pQrySecAgentACIDMap"].GetObject();
                    strcpy(cfd.BrokerID, pObj["BrokerID"].GetString());
                    strcpy(cfd.UserID, pObj["UserID"].GetString());
                    strcpy(cfd.AccountID, pObj["AccountID"].GetString());
                    strcpy(cfd.CurrencyID, pObj["CurrencyID"].GetString());
                    writer.StartObject();
                    writer.Key("req_id");
                    writer.String(d["req_id"].GetString());
                    writer.Key("value");
                    writer.Int(ptr->ReqQrySecAgentACIDMap(&cfd, d["nRequestID"].GetInt()));
                    writer.EndObject();
                }
                else if (0 == strcmp("ReqQryProductExchRate", d["cmd"].GetString()))
                {
                    CThostFtdcTraderApi* ptr = (CThostFtdcTraderApi*)d["ptr"].GetUint64();
                    CThostFtdcQryProductExchRateField cfd = { 0 };
                    auto pObj = d["pQryProductExchRate"].GetObject();
                    strcpy(cfd.reserve1, pObj["reserve1"].GetString());
                    strcpy(cfd.ExchangeID, pObj["ExchangeID"].GetString());
                    strcpy(cfd.ProductID, pObj["ProductID"].GetString());
                    writer.StartObject();
                    writer.Key("req_id");
                    writer.String(d["req_id"].GetString());
                    writer.Key("value");
                    writer.Int(ptr->ReqQryProductExchRate(&cfd, d["nRequestID"].GetInt()));
                    writer.EndObject();
                }
                else if (0 == strcmp("ReqQryProductGroup", d["cmd"].GetString()))
                {
                    CThostFtdcTraderApi* ptr = (CThostFtdcTraderApi*)d["ptr"].GetUint64();
                    CThostFtdcQryProductGroupField cfd = { 0 };
                    auto pObj = d["pQryProductGroup"].GetObject();
                    strcpy(cfd.reserve1, pObj["reserve1"].GetString());
                    strcpy(cfd.ExchangeID, pObj["ExchangeID"].GetString());
                    strcpy(cfd.ProductID, pObj["ProductID"].GetString());
                    writer.StartObject();
                    writer.Key("req_id");
                    writer.String(d["req_id"].GetString());
                    writer.Key("value");
                    writer.Int(ptr->ReqQryProductGroup(&cfd, d["nRequestID"].GetInt()));
                    writer.EndObject();
                }
                else if (0 == strcmp("ReqQryMMInstrumentCommissionRate", d["cmd"].GetString()))
                {
                    CThostFtdcTraderApi* ptr = (CThostFtdcTraderApi*)d["ptr"].GetUint64();
                    CThostFtdcQryMMInstrumentCommissionRateField cfd = { 0 };
                    auto pObj = d["pQryMMInstrumentCommissionRate"].GetObject();
                    strcpy(cfd.BrokerID, pObj["BrokerID"].GetString());
                    strcpy(cfd.InvestorID, pObj["InvestorID"].GetString());
                    strcpy(cfd.reserve1, pObj["reserve1"].GetString());
                    strcpy(cfd.InstrumentID, pObj["InstrumentID"].GetString());
                    writer.StartObject();
                    writer.Key("req_id");
                    writer.String(d["req_id"].GetString());
                    writer.Key("value");
                    writer.Int(ptr->ReqQryMMInstrumentCommissionRate(&cfd, d["nRequestID"].GetInt()));
                    writer.EndObject();
                }
                else if (0 == strcmp("ReqQryMMOptionInstrCommRate", d["cmd"].GetString()))
                {
                    CThostFtdcTraderApi* ptr = (CThostFtdcTraderApi*)d["ptr"].GetUint64();
                    CThostFtdcQryMMOptionInstrCommRateField cfd = { 0 };
                    auto pObj = d["pQryMMOptionInstrCommRate"].GetObject();
                    strcpy(cfd.BrokerID, pObj["BrokerID"].GetString());
                    strcpy(cfd.InvestorID, pObj["InvestorID"].GetString());
                    strcpy(cfd.reserve1, pObj["reserve1"].GetString());
                    strcpy(cfd.InstrumentID, pObj["InstrumentID"].GetString());
                    writer.StartObject();
                    writer.Key("req_id");
                    writer.String(d["req_id"].GetString());
                    writer.Key("value");
                    writer.Int(ptr->ReqQryMMOptionInstrCommRate(&cfd, d["nRequestID"].GetInt()));
                    writer.EndObject();
                }
                else if (0 == strcmp("ReqQryInstrumentOrderCommRate", d["cmd"].GetString()))
                {
                    CThostFtdcTraderApi* ptr = (CThostFtdcTraderApi*)d["ptr"].GetUint64();
                    CThostFtdcQryInstrumentOrderCommRateField cfd = { 0 };
                    auto pObj = d["pQryInstrumentOrderCommRate"].GetObject();
                    strcpy(cfd.BrokerID, pObj["BrokerID"].GetString());
                    strcpy(cfd.InvestorID, pObj["InvestorID"].GetString());
                    strcpy(cfd.reserve1, pObj["reserve1"].GetString());
                    strcpy(cfd.InstrumentID, pObj["InstrumentID"].GetString());
                    writer.StartObject();
                    writer.Key("req_id");
                    writer.String(d["req_id"].GetString());
                    writer.Key("value");
                    writer.Int(ptr->ReqQryInstrumentOrderCommRate(&cfd, d["nRequestID"].GetInt()));
                    writer.EndObject();
                }
                else if (0 == strcmp("ReqQrySecAgentTradingAccount", d["cmd"].GetString()))
                {
                    CThostFtdcTraderApi* ptr = (CThostFtdcTraderApi*)d["ptr"].GetUint64();
                    CThostFtdcQryTradingAccountField cfd = { 0 };
                    auto pObj = d["pQryTradingAccount"].GetObject();
                    strcpy(cfd.BrokerID, pObj["BrokerID"].GetString());
                    strcpy(cfd.InvestorID, pObj["InvestorID"].GetString());
                    strcpy(cfd.CurrencyID, pObj["CurrencyID"].GetString());
                    cfd.BizType = pObj["BizType"].GetString()[0];
                    strcpy(cfd.AccountID, pObj["AccountID"].GetString());
                    writer.StartObject();
                    writer.Key("req_id");
                    writer.String(d["req_id"].GetString());
                    writer.Key("value");
                    writer.Int(ptr->ReqQrySecAgentTradingAccount(&cfd, d["nRequestID"].GetInt()));
                    writer.EndObject();
                }
                else if (0 == strcmp("ReqQrySecAgentCheckMode", d["cmd"].GetString()))
                {
                    CThostFtdcTraderApi* ptr = (CThostFtdcTraderApi*)d["ptr"].GetUint64();
                    CThostFtdcQrySecAgentCheckModeField cfd = { 0 };
                    auto pObj = d["pQrySecAgentCheckMode"].GetObject();
                    strcpy(cfd.BrokerID, pObj["BrokerID"].GetString());
                    strcpy(cfd.InvestorID, pObj["InvestorID"].GetString());
                    writer.StartObject();
                    writer.Key("req_id");
                    writer.String(d["req_id"].GetString());
                    writer.Key("value");
                    writer.Int(ptr->ReqQrySecAgentCheckMode(&cfd, d["nRequestID"].GetInt()));
                    writer.EndObject();
                }
                else if (0 == strcmp("ReqQrySecAgentTradeInfo", d["cmd"].GetString()))
                {
                    CThostFtdcTraderApi* ptr = (CThostFtdcTraderApi*)d["ptr"].GetUint64();
                    CThostFtdcQrySecAgentTradeInfoField cfd = { 0 };
                    auto pObj = d["pQrySecAgentTradeInfo"].GetObject();
                    strcpy(cfd.BrokerID, pObj["BrokerID"].GetString());
                    strcpy(cfd.BrokerSecAgentID, pObj["BrokerSecAgentID"].GetString());
                    writer.StartObject();
                    writer.Key("req_id");
                    writer.String(d["req_id"].GetString());
                    writer.Key("value");
                    writer.Int(ptr->ReqQrySecAgentTradeInfo(&cfd, d["nRequestID"].GetInt()));
                    writer.EndObject();
                }
                else if (0 == strcmp("ReqQryOptionInstrTradeCost", d["cmd"].GetString()))
                {
                    CThostFtdcTraderApi* ptr = (CThostFtdcTraderApi*)d["ptr"].GetUint64();
                    CThostFtdcQryOptionInstrTradeCostField cfd = { 0 };
                    auto pObj = d["pQryOptionInstrTradeCost"].GetObject();
                    strcpy(cfd.BrokerID, pObj["BrokerID"].GetString());
                    strcpy(cfd.InvestorID, pObj["InvestorID"].GetString());
                    strcpy(cfd.reserve1, pObj["reserve1"].GetString());
                    cfd.HedgeFlag = pObj["HedgeFlag"].GetString()[0];
                    cfd.InputPrice = pObj["InputPrice"].GetDouble();
                    cfd.UnderlyingPrice = pObj["UnderlyingPrice"].GetDouble();
                    strcpy(cfd.ExchangeID, pObj["ExchangeID"].GetString());
                    strcpy(cfd.InvestUnitID, pObj["InvestUnitID"].GetString());
                    strcpy(cfd.InstrumentID, pObj["InstrumentID"].GetString());
                    writer.StartObject();
                    writer.Key("req_id");
                    writer.String(d["req_id"].GetString());
                    writer.Key("value");
                    writer.Int(ptr->ReqQryOptionInstrTradeCost(&cfd, d["nRequestID"].GetInt()));
                    writer.EndObject();
                }
                else if (0 == strcmp("ReqQryOptionInstrCommRate", d["cmd"].GetString()))
                {
                    CThostFtdcTraderApi* ptr = (CThostFtdcTraderApi*)d["ptr"].GetUint64();
                    CThostFtdcQryOptionInstrCommRateField cfd = { 0 };
                    auto pObj = d["pQryOptionInstrCommRate"].GetObject();
                    strcpy(cfd.BrokerID, pObj["BrokerID"].GetString());
                    strcpy(cfd.InvestorID, pObj["InvestorID"].GetString());
                    strcpy(cfd.reserve1, pObj["reserve1"].GetString());
                    strcpy(cfd.ExchangeID, pObj["ExchangeID"].GetString());
                    strcpy(cfd.InvestUnitID, pObj["InvestUnitID"].GetString());
                    strcpy(cfd.InstrumentID, pObj["InstrumentID"].GetString());
                    writer.StartObject();
                    writer.Key("req_id");
                    writer.String(d["req_id"].GetString());
                    writer.Key("value");
                    writer.Int(ptr->ReqQryOptionInstrCommRate(&cfd, d["nRequestID"].GetInt()));
                    writer.EndObject();
                }
                else if (0 == strcmp("ReqQryExecOrder", d["cmd"].GetString()))
                {
                    CThostFtdcTraderApi* ptr = (CThostFtdcTraderApi*)d["ptr"].GetUint64();
                    CThostFtdcQryExecOrderField cfd = { 0 };
                    auto pObj = d["pQryExecOrder"].GetObject();
                    strcpy(cfd.BrokerID, pObj["BrokerID"].GetString());
                    strcpy(cfd.InvestorID, pObj["InvestorID"].GetString());
                    strcpy(cfd.reserve1, pObj["reserve1"].GetString());
                    strcpy(cfd.ExchangeID, pObj["ExchangeID"].GetString());
                    strcpy(cfd.ExecOrderSysID, pObj["ExecOrderSysID"].GetString());
                    strcpy(cfd.InsertTimeStart, pObj["InsertTimeStart"].GetString());
                    strcpy(cfd.InsertTimeEnd, pObj["InsertTimeEnd"].GetString());
                    strcpy(cfd.InstrumentID, pObj["InstrumentID"].GetString());
                    writer.StartObject();
                    writer.Key("req_id");
                    writer.String(d["req_id"].GetString());
                    writer.Key("value");
                    writer.Int(ptr->ReqQryExecOrder(&cfd, d["nRequestID"].GetInt()));
                    writer.EndObject();
                }
                else if (0 == strcmp("ReqQryForQuote", d["cmd"].GetString()))
                {
                    CThostFtdcTraderApi* ptr = (CThostFtdcTraderApi*)d["ptr"].GetUint64();
                    CThostFtdcQryForQuoteField cfd = { 0 };
                    auto pObj = d["pQryForQuote"].GetObject();
                    strcpy(cfd.BrokerID, pObj["BrokerID"].GetString());
                    strcpy(cfd.InvestorID, pObj["InvestorID"].GetString());
                    strcpy(cfd.reserve1, pObj["reserve1"].GetString());
                    strcpy(cfd.ExchangeID, pObj["ExchangeID"].GetString());
                    strcpy(cfd.InsertTimeStart, pObj["InsertTimeStart"].GetString());
                    strcpy(cfd.InsertTimeEnd, pObj["InsertTimeEnd"].GetString());
                    strcpy(cfd.InvestUnitID, pObj["InvestUnitID"].GetString());
                    strcpy(cfd.InstrumentID, pObj["InstrumentID"].GetString());
                    writer.StartObject();
                    writer.Key("req_id");
                    writer.String(d["req_id"].GetString());
                    writer.Key("value");
                    writer.Int(ptr->ReqQryForQuote(&cfd, d["nRequestID"].GetInt()));
                    writer.EndObject();
                }
                else if (0 == strcmp("ReqQryQuote", d["cmd"].GetString()))
                {
                    CThostFtdcTraderApi* ptr = (CThostFtdcTraderApi*)d["ptr"].GetUint64();
                    CThostFtdcQryQuoteField cfd = { 0 };
                    auto pObj = d["pQryQuote"].GetObject();
                    strcpy(cfd.BrokerID, pObj["BrokerID"].GetString());
                    strcpy(cfd.InvestorID, pObj["InvestorID"].GetString());
                    strcpy(cfd.reserve1, pObj["reserve1"].GetString());
                    strcpy(cfd.ExchangeID, pObj["ExchangeID"].GetString());
                    strcpy(cfd.QuoteSysID, pObj["QuoteSysID"].GetString());
                    strcpy(cfd.InsertTimeStart, pObj["InsertTimeStart"].GetString());
                    strcpy(cfd.InsertTimeEnd, pObj["InsertTimeEnd"].GetString());
                    strcpy(cfd.InvestUnitID, pObj["InvestUnitID"].GetString());
                    strcpy(cfd.InstrumentID, pObj["InstrumentID"].GetString());
                    writer.StartObject();
                    writer.Key("req_id");
                    writer.String(d["req_id"].GetString());
                    writer.Key("value");
                    writer.Int(ptr->ReqQryQuote(&cfd, d["nRequestID"].GetInt()));
                    writer.EndObject();
                }
                else if (0 == strcmp("ReqQryOptionSelfClose", d["cmd"].GetString()))
                {
                    CThostFtdcTraderApi* ptr = (CThostFtdcTraderApi*)d["ptr"].GetUint64();
                    CThostFtdcQryOptionSelfCloseField cfd = { 0 };
                    auto pObj = d["pQryOptionSelfClose"].GetObject();
                    strcpy(cfd.BrokerID, pObj["BrokerID"].GetString());
                    strcpy(cfd.InvestorID, pObj["InvestorID"].GetString());
                    strcpy(cfd.reserve1, pObj["reserve1"].GetString());
                    strcpy(cfd.ExchangeID, pObj["ExchangeID"].GetString());
                    strcpy(cfd.OptionSelfCloseSysID, pObj["OptionSelfCloseSysID"].GetString());
                    strcpy(cfd.InsertTimeStart, pObj["InsertTimeStart"].GetString());
                    strcpy(cfd.InsertTimeEnd, pObj["InsertTimeEnd"].GetString());
                    strcpy(cfd.InstrumentID, pObj["InstrumentID"].GetString());
                    writer.StartObject();
                    writer.Key("req_id");
                    writer.String(d["req_id"].GetString());
                    writer.Key("value");
                    writer.Int(ptr->ReqQryOptionSelfClose(&cfd, d["nRequestID"].GetInt()));
                    writer.EndObject();
                }
                else if (0 == strcmp("ReqQryInvestUnit", d["cmd"].GetString()))
                {
                    CThostFtdcTraderApi* ptr = (CThostFtdcTraderApi*)d["ptr"].GetUint64();
                    CThostFtdcQryInvestUnitField cfd = { 0 };
                    auto pObj = d["pQryInvestUnit"].GetObject();
                    strcpy(cfd.BrokerID, pObj["BrokerID"].GetString());
                    strcpy(cfd.InvestorID, pObj["InvestorID"].GetString());
                    strcpy(cfd.InvestUnitID, pObj["InvestUnitID"].GetString());
                    writer.StartObject();
                    writer.Key("req_id");
                    writer.String(d["req_id"].GetString());
                    writer.Key("value");
                    writer.Int(ptr->ReqQryInvestUnit(&cfd, d["nRequestID"].GetInt()));
                    writer.EndObject();
                }
                else if (0 == strcmp("ReqQryCombInstrumentGuard", d["cmd"].GetString()))
                {
                    CThostFtdcTraderApi* ptr = (CThostFtdcTraderApi*)d["ptr"].GetUint64();
                    CThostFtdcQryCombInstrumentGuardField cfd = { 0 };
                    auto pObj = d["pQryCombInstrumentGuard"].GetObject();
                    strcpy(cfd.BrokerID, pObj["BrokerID"].GetString());
                    strcpy(cfd.reserve1, pObj["reserve1"].GetString());
                    strcpy(cfd.ExchangeID, pObj["ExchangeID"].GetString());
                    strcpy(cfd.InstrumentID, pObj["InstrumentID"].GetString());
                    writer.StartObject();
                    writer.Key("req_id");
                    writer.String(d["req_id"].GetString());
                    writer.Key("value");
                    writer.Int(ptr->ReqQryCombInstrumentGuard(&cfd, d["nRequestID"].GetInt()));
                    writer.EndObject();
                }
                else if (0 == strcmp("ReqQryCombAction", d["cmd"].GetString()))
                {
                    CThostFtdcTraderApi* ptr = (CThostFtdcTraderApi*)d["ptr"].GetUint64();
                    CThostFtdcQryCombActionField cfd = { 0 };
                    auto pObj = d["pQryCombAction"].GetObject();
                    strcpy(cfd.BrokerID, pObj["BrokerID"].GetString());
                    strcpy(cfd.InvestorID, pObj["InvestorID"].GetString());
                    strcpy(cfd.reserve1, pObj["reserve1"].GetString());
                    strcpy(cfd.ExchangeID, pObj["ExchangeID"].GetString());
                    strcpy(cfd.InvestUnitID, pObj["InvestUnitID"].GetString());
                    strcpy(cfd.InstrumentID, pObj["InstrumentID"].GetString());
                    writer.StartObject();
                    writer.Key("req_id");
                    writer.String(d["req_id"].GetString());
                    writer.Key("value");
                    writer.Int(ptr->ReqQryCombAction(&cfd, d["nRequestID"].GetInt()));
                    writer.EndObject();
                }
                else if (0 == strcmp("ReqQryTransferSerial", d["cmd"].GetString()))
                {
                    CThostFtdcTraderApi* ptr = (CThostFtdcTraderApi*)d["ptr"].GetUint64();
                    CThostFtdcQryTransferSerialField cfd = { 0 };
                    auto pObj = d["pQryTransferSerial"].GetObject();
                    strcpy(cfd.BrokerID, pObj["BrokerID"].GetString());
                    strcpy(cfd.AccountID, pObj["AccountID"].GetString());
                    strcpy(cfd.BankID, pObj["BankID"].GetString());
                    strcpy(cfd.CurrencyID, pObj["CurrencyID"].GetString());
                    writer.StartObject();
                    writer.Key("req_id");
                    writer.String(d["req_id"].GetString());
                    writer.Key("value");
                    writer.Int(ptr->ReqQryTransferSerial(&cfd, d["nRequestID"].GetInt()));
                    writer.EndObject();
                }
                else if (0 == strcmp("ReqQryAccountregister", d["cmd"].GetString()))
                {
                    CThostFtdcTraderApi* ptr = (CThostFtdcTraderApi*)d["ptr"].GetUint64();
                    CThostFtdcQryAccountregisterField cfd = { 0 };
                    auto pObj = d["pQryAccountregister"].GetObject();
                    strcpy(cfd.BrokerID, pObj["BrokerID"].GetString());
                    strcpy(cfd.AccountID, pObj["AccountID"].GetString());
                    strcpy(cfd.BankID, pObj["BankID"].GetString());
                    strcpy(cfd.BankBranchID, pObj["BankBranchID"].GetString());
                    strcpy(cfd.CurrencyID, pObj["CurrencyID"].GetString());
                    writer.StartObject();
                    writer.Key("req_id");
                    writer.String(d["req_id"].GetString());
                    writer.Key("value");
                    writer.Int(ptr->ReqQryAccountregister(&cfd, d["nRequestID"].GetInt()));
                    writer.EndObject();
                }
                else if (0 == strcmp("ReqQryContractBank", d["cmd"].GetString()))
                {
                    CThostFtdcTraderApi* ptr = (CThostFtdcTraderApi*)d["ptr"].GetUint64();
                    CThostFtdcQryContractBankField cfd = { 0 };
                    auto pObj = d["pQryContractBank"].GetObject();
                    strcpy(cfd.BrokerID, pObj["BrokerID"].GetString());
                    strcpy(cfd.BankID, pObj["BankID"].GetString());
                    strcpy(cfd.BankBrchID, pObj["BankBrchID"].GetString());
                    writer.StartObject();
                    writer.Key("req_id");
                    writer.String(d["req_id"].GetString());
                    writer.Key("value");
                    writer.Int(ptr->ReqQryContractBank(&cfd, d["nRequestID"].GetInt()));
                    writer.EndObject();
                }
                else if (0 == strcmp("ReqQryParkedOrder", d["cmd"].GetString()))
                {
                    CThostFtdcTraderApi* ptr = (CThostFtdcTraderApi*)d["ptr"].GetUint64();
                    CThostFtdcQryParkedOrderField cfd = { 0 };
                    auto pObj = d["pQryParkedOrder"].GetObject();
                    strcpy(cfd.BrokerID, pObj["BrokerID"].GetString());
                    strcpy(cfd.InvestorID, pObj["InvestorID"].GetString());
                    strcpy(cfd.reserve1, pObj["reserve1"].GetString());
                    strcpy(cfd.ExchangeID, pObj["ExchangeID"].GetString());
                    strcpy(cfd.InvestUnitID, pObj["InvestUnitID"].GetString());
                    strcpy(cfd.InstrumentID, pObj["InstrumentID"].GetString());
                    writer.StartObject();
                    writer.Key("req_id");
                    writer.String(d["req_id"].GetString());
                    writer.Key("value");
                    writer.Int(ptr->ReqQryParkedOrder(&cfd, d["nRequestID"].GetInt()));
                    writer.EndObject();
                }
                else if (0 == strcmp("ReqQryParkedOrderAction", d["cmd"].GetString()))
                {
                    CThostFtdcTraderApi* ptr = (CThostFtdcTraderApi*)d["ptr"].GetUint64();
                    CThostFtdcQryParkedOrderActionField cfd = { 0 };
                    auto pObj = d["pQryParkedOrderAction"].GetObject();
                    strcpy(cfd.BrokerID, pObj["BrokerID"].GetString());
                    strcpy(cfd.InvestorID, pObj["InvestorID"].GetString());
                    strcpy(cfd.reserve1, pObj["reserve1"].GetString());
                    strcpy(cfd.ExchangeID, pObj["ExchangeID"].GetString());
                    strcpy(cfd.InvestUnitID, pObj["InvestUnitID"].GetString());
                    strcpy(cfd.InstrumentID, pObj["InstrumentID"].GetString());
                    writer.StartObject();
                    writer.Key("req_id");
                    writer.String(d["req_id"].GetString());
                    writer.Key("value");
                    writer.Int(ptr->ReqQryParkedOrderAction(&cfd, d["nRequestID"].GetInt()));
                    writer.EndObject();
                }
                else if (0 == strcmp("ReqQryTradingNotice", d["cmd"].GetString()))
                {
                    CThostFtdcTraderApi* ptr = (CThostFtdcTraderApi*)d["ptr"].GetUint64();
                    CThostFtdcQryTradingNoticeField cfd = { 0 };
                    auto pObj = d["pQryTradingNotice"].GetObject();
                    strcpy(cfd.BrokerID, pObj["BrokerID"].GetString());
                    strcpy(cfd.InvestorID, pObj["InvestorID"].GetString());
                    strcpy(cfd.InvestUnitID, pObj["InvestUnitID"].GetString());
                    writer.StartObject();
                    writer.Key("req_id");
                    writer.String(d["req_id"].GetString());
                    writer.Key("value");
                    writer.Int(ptr->ReqQryTradingNotice(&cfd, d["nRequestID"].GetInt()));
                    writer.EndObject();
                }
                else if (0 == strcmp("ReqQryBrokerTradingParams", d["cmd"].GetString()))
                {
                    CThostFtdcTraderApi* ptr = (CThostFtdcTraderApi*)d["ptr"].GetUint64();
                    CThostFtdcQryBrokerTradingParamsField cfd = { 0 };
                    auto pObj = d["pQryBrokerTradingParams"].GetObject();
                    strcpy(cfd.BrokerID, pObj["BrokerID"].GetString());
                    strcpy(cfd.InvestorID, pObj["InvestorID"].GetString());
                    strcpy(cfd.CurrencyID, pObj["CurrencyID"].GetString());
                    strcpy(cfd.AccountID, pObj["AccountID"].GetString());
                    writer.StartObject();
                    writer.Key("req_id");
                    writer.String(d["req_id"].GetString());
                    writer.Key("value");
                    writer.Int(ptr->ReqQryBrokerTradingParams(&cfd, d["nRequestID"].GetInt()));
                    writer.EndObject();
                }
                else if (0 == strcmp("ReqQryBrokerTradingAlgos", d["cmd"].GetString()))
                {
                    CThostFtdcTraderApi* ptr = (CThostFtdcTraderApi*)d["ptr"].GetUint64();
                    CThostFtdcQryBrokerTradingAlgosField cfd = { 0 };
                    auto pObj = d["pQryBrokerTradingAlgos"].GetObject();
                    strcpy(cfd.BrokerID, pObj["BrokerID"].GetString());
                    strcpy(cfd.ExchangeID, pObj["ExchangeID"].GetString());
                    strcpy(cfd.reserve1, pObj["reserve1"].GetString());
                    strcpy(cfd.InstrumentID, pObj["InstrumentID"].GetString());
                    writer.StartObject();
                    writer.Key("req_id");
                    writer.String(d["req_id"].GetString());
                    writer.Key("value");
                    writer.Int(ptr->ReqQryBrokerTradingAlgos(&cfd, d["nRequestID"].GetInt()));
                    writer.EndObject();
                }
                else if (0 == strcmp("ReqQueryCFMMCTradingAccountToken", d["cmd"].GetString()))
                {
                    CThostFtdcTraderApi* ptr = (CThostFtdcTraderApi*)d["ptr"].GetUint64();
                    CThostFtdcQueryCFMMCTradingAccountTokenField cfd = { 0 };
                    auto pObj = d["pQueryCFMMCTradingAccountToken"].GetObject();
                    strcpy(cfd.BrokerID, pObj["BrokerID"].GetString());
                    strcpy(cfd.InvestorID, pObj["InvestorID"].GetString());
                    strcpy(cfd.InvestUnitID, pObj["InvestUnitID"].GetString());
                    writer.StartObject();
                    writer.Key("req_id");
                    writer.String(d["req_id"].GetString());
                    writer.Key("value");
                    writer.Int(ptr->ReqQueryCFMMCTradingAccountToken(&cfd, d["nRequestID"].GetInt()));
                    writer.EndObject();
                }
                else if (0 == strcmp("ReqFromBankToFutureByFuture", d["cmd"].GetString()))
                {
                    CThostFtdcTraderApi* ptr = (CThostFtdcTraderApi*)d["ptr"].GetUint64();
                    CThostFtdcReqTransferField cfd = { 0 };
                    auto pObj = d["pReqTransfer"].GetObject();
                    strcpy(cfd.TradeCode, pObj["TradeCode"].GetString());
                    strcpy(cfd.BankID, pObj["BankID"].GetString());
                    strcpy(cfd.BankBranchID, pObj["BankBranchID"].GetString());
                    strcpy(cfd.BrokerID, pObj["BrokerID"].GetString());
                    strcpy(cfd.BrokerBranchID, pObj["BrokerBranchID"].GetString());
                    strcpy(cfd.TradeDate, pObj["TradeDate"].GetString());
                    strcpy(cfd.TradeTime, pObj["TradeTime"].GetString());
                    strcpy(cfd.BankSerial, pObj["BankSerial"].GetString());
                    strcpy(cfd.TradingDay, pObj["TradingDay"].GetString());
                    cfd.PlateSerial = pObj["PlateSerial"].GetInt();
                    cfd.LastFragment = pObj["LastFragment"].GetString()[0];
                    cfd.SessionID = pObj["SessionID"].GetInt();
                    strcpy(cfd.CustomerName, pObj["CustomerName"].GetString());
                    cfd.IdCardType = pObj["IdCardType"].GetString()[0];
                    strcpy(cfd.IdentifiedCardNo, pObj["IdentifiedCardNo"].GetString());
                    cfd.CustType = pObj["CustType"].GetString()[0];
                    strcpy(cfd.BankAccount, pObj["BankAccount"].GetString());
                    strcpy(cfd.BankPassWord, pObj["BankPassWord"].GetString());
                    strcpy(cfd.AccountID, pObj["AccountID"].GetString());
                    strcpy(cfd.Password, pObj["Password"].GetString());
                    cfd.InstallID = pObj["InstallID"].GetInt();
                    cfd.FutureSerial = pObj["FutureSerial"].GetInt();
                    strcpy(cfd.UserID, pObj["UserID"].GetString());
                    cfd.VerifyCertNoFlag = pObj["VerifyCertNoFlag"].GetString()[0];
                    strcpy(cfd.CurrencyID, pObj["CurrencyID"].GetString());
                    cfd.TradeAmount = pObj["TradeAmount"].GetDouble();
                    cfd.FutureFetchAmount = pObj["FutureFetchAmount"].GetDouble();
                    cfd.FeePayFlag = pObj["FeePayFlag"].GetString()[0];
                    cfd.CustFee = pObj["CustFee"].GetDouble();
                    cfd.BrokerFee = pObj["BrokerFee"].GetDouble();
                    strcpy(cfd.Message, pObj["Message"].GetString());
                    strcpy(cfd.Digest, pObj["Digest"].GetString());
                    cfd.BankAccType = pObj["BankAccType"].GetString()[0];
                    strcpy(cfd.DeviceID, pObj["DeviceID"].GetString());
                    cfd.BankSecuAccType = pObj["BankSecuAccType"].GetString()[0];
                    strcpy(cfd.BrokerIDByBank, pObj["BrokerIDByBank"].GetString());
                    strcpy(cfd.BankSecuAcc, pObj["BankSecuAcc"].GetString());
                    cfd.BankPwdFlag = pObj["BankPwdFlag"].GetString()[0];
                    cfd.SecuPwdFlag = pObj["SecuPwdFlag"].GetString()[0];
                    strcpy(cfd.OperNo, pObj["OperNo"].GetString());
                    cfd.RequestID = pObj["RequestID"].GetInt();
                    cfd.TID = pObj["TID"].GetInt();
                    cfd.TransferStatus = pObj["TransferStatus"].GetString()[0];
                    strcpy(cfd.LongCustomerName, pObj["LongCustomerName"].GetString());
                    writer.StartObject();
                    writer.Key("req_id");
                    writer.String(d["req_id"].GetString());
                    writer.Key("value");
                    writer.Int(ptr->ReqFromBankToFutureByFuture(&cfd, d["nRequestID"].GetInt()));
                    writer.EndObject();
                }
                else if (0 == strcmp("ReqFromFutureToBankByFuture", d["cmd"].GetString()))
                {
                    CThostFtdcTraderApi* ptr = (CThostFtdcTraderApi*)d["ptr"].GetUint64();
                    CThostFtdcReqTransferField cfd = { 0 };
                    auto pObj = d["pReqTransfer"].GetObject();
                    strcpy(cfd.TradeCode, pObj["TradeCode"].GetString());
                    strcpy(cfd.BankID, pObj["BankID"].GetString());
                    strcpy(cfd.BankBranchID, pObj["BankBranchID"].GetString());
                    strcpy(cfd.BrokerID, pObj["BrokerID"].GetString());
                    strcpy(cfd.BrokerBranchID, pObj["BrokerBranchID"].GetString());
                    strcpy(cfd.TradeDate, pObj["TradeDate"].GetString());
                    strcpy(cfd.TradeTime, pObj["TradeTime"].GetString());
                    strcpy(cfd.BankSerial, pObj["BankSerial"].GetString());
                    strcpy(cfd.TradingDay, pObj["TradingDay"].GetString());
                    cfd.PlateSerial = pObj["PlateSerial"].GetInt();
                    cfd.LastFragment = pObj["LastFragment"].GetString()[0];
                    cfd.SessionID = pObj["SessionID"].GetInt();
                    strcpy(cfd.CustomerName, pObj["CustomerName"].GetString());
                    cfd.IdCardType = pObj["IdCardType"].GetString()[0];
                    strcpy(cfd.IdentifiedCardNo, pObj["IdentifiedCardNo"].GetString());
                    cfd.CustType = pObj["CustType"].GetString()[0];
                    strcpy(cfd.BankAccount, pObj["BankAccount"].GetString());
                    strcpy(cfd.BankPassWord, pObj["BankPassWord"].GetString());
                    strcpy(cfd.AccountID, pObj["AccountID"].GetString());
                    strcpy(cfd.Password, pObj["Password"].GetString());
                    cfd.InstallID = pObj["InstallID"].GetInt();
                    cfd.FutureSerial = pObj["FutureSerial"].GetInt();
                    strcpy(cfd.UserID, pObj["UserID"].GetString());
                    cfd.VerifyCertNoFlag = pObj["VerifyCertNoFlag"].GetString()[0];
                    strcpy(cfd.CurrencyID, pObj["CurrencyID"].GetString());
                    cfd.TradeAmount = pObj["TradeAmount"].GetDouble();
                    cfd.FutureFetchAmount = pObj["FutureFetchAmount"].GetDouble();
                    cfd.FeePayFlag = pObj["FeePayFlag"].GetString()[0];
                    cfd.CustFee = pObj["CustFee"].GetDouble();
                    cfd.BrokerFee = pObj["BrokerFee"].GetDouble();
                    strcpy(cfd.Message, pObj["Message"].GetString());
                    strcpy(cfd.Digest, pObj["Digest"].GetString());
                    cfd.BankAccType = pObj["BankAccType"].GetString()[0];
                    strcpy(cfd.DeviceID, pObj["DeviceID"].GetString());
                    cfd.BankSecuAccType = pObj["BankSecuAccType"].GetString()[0];
                    strcpy(cfd.BrokerIDByBank, pObj["BrokerIDByBank"].GetString());
                    strcpy(cfd.BankSecuAcc, pObj["BankSecuAcc"].GetString());
                    cfd.BankPwdFlag = pObj["BankPwdFlag"].GetString()[0];
                    cfd.SecuPwdFlag = pObj["SecuPwdFlag"].GetString()[0];
                    strcpy(cfd.OperNo, pObj["OperNo"].GetString());
                    cfd.RequestID = pObj["RequestID"].GetInt();
                    cfd.TID = pObj["TID"].GetInt();
                    cfd.TransferStatus = pObj["TransferStatus"].GetString()[0];
                    strcpy(cfd.LongCustomerName, pObj["LongCustomerName"].GetString());
                    writer.StartObject();
                    writer.Key("req_id");
                    writer.String(d["req_id"].GetString());
                    writer.Key("value");
                    writer.Int(ptr->ReqFromFutureToBankByFuture(&cfd, d["nRequestID"].GetInt()));
                    writer.EndObject();
                }
                else if (0 == strcmp("ReqQueryBankAccountMoneyByFuture", d["cmd"].GetString()))
                {
                    CThostFtdcTraderApi* ptr = (CThostFtdcTraderApi*)d["ptr"].GetUint64();
                    CThostFtdcReqQueryAccountField cfd = { 0 };
                    auto pObj = d["pReqQueryAccount"].GetObject();
                    strcpy(cfd.TradeCode, pObj["TradeCode"].GetString());
                    strcpy(cfd.BankID, pObj["BankID"].GetString());
                    strcpy(cfd.BankBranchID, pObj["BankBranchID"].GetString());
                    strcpy(cfd.BrokerID, pObj["BrokerID"].GetString());
                    strcpy(cfd.BrokerBranchID, pObj["BrokerBranchID"].GetString());
                    strcpy(cfd.TradeDate, pObj["TradeDate"].GetString());
                    strcpy(cfd.TradeTime, pObj["TradeTime"].GetString());
                    strcpy(cfd.BankSerial, pObj["BankSerial"].GetString());
                    strcpy(cfd.TradingDay, pObj["TradingDay"].GetString());
                    cfd.PlateSerial = pObj["PlateSerial"].GetInt();
                    cfd.LastFragment = pObj["LastFragment"].GetString()[0];
                    cfd.SessionID = pObj["SessionID"].GetInt();
                    strcpy(cfd.CustomerName, pObj["CustomerName"].GetString());
                    cfd.IdCardType = pObj["IdCardType"].GetString()[0];
                    strcpy(cfd.IdentifiedCardNo, pObj["IdentifiedCardNo"].GetString());
                    cfd.CustType = pObj["CustType"].GetString()[0];
                    strcpy(cfd.BankAccount, pObj["BankAccount"].GetString());
                    strcpy(cfd.BankPassWord, pObj["BankPassWord"].GetString());
                    strcpy(cfd.AccountID, pObj["AccountID"].GetString());
                    strcpy(cfd.Password, pObj["Password"].GetString());
                    cfd.FutureSerial = pObj["FutureSerial"].GetInt();
                    cfd.InstallID = pObj["InstallID"].GetInt();
                    strcpy(cfd.UserID, pObj["UserID"].GetString());
                    cfd.VerifyCertNoFlag = pObj["VerifyCertNoFlag"].GetString()[0];
                    strcpy(cfd.CurrencyID, pObj["CurrencyID"].GetString());
                    strcpy(cfd.Digest, pObj["Digest"].GetString());
                    cfd.BankAccType = pObj["BankAccType"].GetString()[0];
                    strcpy(cfd.DeviceID, pObj["DeviceID"].GetString());
                    cfd.BankSecuAccType = pObj["BankSecuAccType"].GetString()[0];
                    strcpy(cfd.BrokerIDByBank, pObj["BrokerIDByBank"].GetString());
                    strcpy(cfd.BankSecuAcc, pObj["BankSecuAcc"].GetString());
                    cfd.BankPwdFlag = pObj["BankPwdFlag"].GetString()[0];
                    cfd.SecuPwdFlag = pObj["SecuPwdFlag"].GetString()[0];
                    strcpy(cfd.OperNo, pObj["OperNo"].GetString());
                    cfd.RequestID = pObj["RequestID"].GetInt();
                    cfd.TID = pObj["TID"].GetInt();
                    strcpy(cfd.LongCustomerName, pObj["LongCustomerName"].GetString());
                    writer.StartObject();
                    writer.Key("req_id");
                    writer.String(d["req_id"].GetString());
                    writer.Key("value");
                    writer.Int(ptr->ReqQueryBankAccountMoneyByFuture(&cfd, d["nRequestID"].GetInt()));
                    writer.EndObject();
                }
                else if (0 == strcmp("ReqQryClassifiedInstrument", d["cmd"].GetString()))
                {
                    CThostFtdcTraderApi* ptr = (CThostFtdcTraderApi*)d["ptr"].GetUint64();
                    CThostFtdcQryClassifiedInstrumentField cfd = { 0 };
                    auto pObj = d["pQryClassifiedInstrument"].GetObject();
                    strcpy(cfd.InstrumentID, pObj["InstrumentID"].GetString());
                    strcpy(cfd.ExchangeID, pObj["ExchangeID"].GetString());
                    strcpy(cfd.ExchangeInstID, pObj["ExchangeInstID"].GetString());
                    strcpy(cfd.ProductID, pObj["ProductID"].GetString());
                    cfd.TradingType = pObj["TradingType"].GetString()[0];
                    cfd.ClassType = pObj["ClassType"].GetString()[0];
                    writer.StartObject();
                    writer.Key("req_id");
                    writer.String(d["req_id"].GetString());
                    writer.Key("value");
                    writer.Int(ptr->ReqQryClassifiedInstrument(&cfd, d["nRequestID"].GetInt()));
                    writer.EndObject();
                }
                else if (0 == strcmp("ReqQryCombPromotionParam", d["cmd"].GetString()))
                {
                    CThostFtdcTraderApi* ptr = (CThostFtdcTraderApi*)d["ptr"].GetUint64();
                    CThostFtdcQryCombPromotionParamField cfd = { 0 };
                    auto pObj = d["pQryCombPromotionParam"].GetObject();
                    strcpy(cfd.ExchangeID, pObj["ExchangeID"].GetString());
                    strcpy(cfd.InstrumentID, pObj["InstrumentID"].GetString());
                    writer.StartObject();
                    writer.Key("req_id");
                    writer.String(d["req_id"].GetString());
                    writer.Key("value");
                    writer.Int(ptr->ReqQryCombPromotionParam(&cfd, d["nRequestID"].GetInt()));
                    writer.EndObject();
                }
            }
        }

        // the return json string had been built.
        socks->send_rsp(s.GetString());
    }
};
#endif