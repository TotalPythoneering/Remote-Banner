#!/usr/bin/env python3
'''
Mission:
Integrate the AI effort into our solution so as to test
a basic echo. Be sure to run ai_rpc_server.py before
running this file.

Authon: Randall Nagy
Nexus: https://https://ko-fi.com/randallnagy
Rev: 2025/12/16, 1.o
File: main_test.py
Video: tbd.
Project: https://github.com/Python3-Training/TotalPythoneering
Status: Testing Success
'''

#!/usr/bin/env python3
'''
Mission:
Integrate the AI effort into our solution so as to test
a basic echo. Be sure to run ai_rpc_server.py before
running this file.

Authon: Randall Nagy
Nexus: https://https://ko-fi.com/randallnagy
Rev: 2025/12/16, 1.o
File: main.py
Video: tbd.
Project: https://github.com/Python3-Training/TotalPythoneering
Status: Testing Success
'''
import threading
import subprocess
import sys
from EchoClientTcp import client_banner

message = "COLOR:WHITE|Testing Success?"
response = client_banner(message)
if not response[0]:
    subprocess.Popen([sys.executable, "ai_tcp_server.py"])
    response = client_banner(message)
print(response)
if response[0]:
    print("Testing Success.")
else:
    print("Testing failure.")








