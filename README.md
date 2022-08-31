# py_sock_ctp
通过socket与ctp库进行通讯。创建一个c++服务端程序，提供socket支持。
客户端可以用支持socket的语言编写。


## build c++ code
### build windows dll
clang -shared -I .\cpp_sock_ctp\ -I .\cpp_sock_ctp\ctp_api_6.5.1_20200908\ -L .\cpp_sock_ctp\ctp_api_6.5.1_20200908\win64\ -D_CRT_SECURE_NO_WARNINGS -lthostmduserapi_se.lib -lthosttraderapi_se.lib -lWs2_32.lib .\cpp_sock_ctp\cpp_ctp.cpp -o cpp_ctp.dll

### build linux so
g++ ./cpp_sock_ctp/cpp_ctp.cpp -shared -fPIC -I ./cpp_sock_ctp/ -I ./cpp_sock_ctp/ctp_api_6.5.1_20200908/ -L ./cpp_sock_ctp/ctp_api_6.5.1_20200908/linux64/ -lthostmduserapi_se -lthosttraderapi_se -lpthread  -o cpp_ctp


