// cpp_ctp主程序,手写代码
#include <iostream>
#include <thread>

#include "cpp_ctp_sock.h"


#ifdef _WIN32
#include <windows.h>
#define DLL_EXP extern "C" __declspec(dllexport)
#else
#define DLL_EXP extern "C"
#endif

DLL_EXP void* start(int port)
{
    return (void*)(new CppCtpSock(port));
}

DLL_EXP void stop(void* cpp_sock)
{    
    if(cpp_sock != NULL)
    {
        cout << "cpp_ctp::stop(): delete CppCtpSock object." << endl;
        delete (CppCtpSock*)cpp_sock;
        cpp_sock = NULL;
        cout << "cpp_ctp::stop(): Done!" << endl;
    }
}


#ifdef _WIN32
BOOL APIENTRY DllMain(HANDLE hModule, DWORD dwReason, void* lpReserved)
{
    HANDLE g_hModule;
    switch (dwReason)
    {
    case DLL_PROCESS_ATTACH:
        cout << "Dll is attached!" << endl;
        g_hModule = (HINSTANCE)hModule;
        break;
    case DLL_PROCESS_DETACH:
        cout << "Dll is detached!" << endl;
        g_hModule = NULL;
    default:
        break;
    }
    return true;
}
#endif