#!/usr/bin/env python3
'''
Mission:
Weaponize the AI effort into our solution so as to test
a basic echo. Be sure to run ai_tcp_server.py before
using this strategy.

Authon: Randall Nagy
Rev: 2025/12/16, 1.o
File: EchoClientTcp.py
Video: https://ko-fi.com/post/Free-Remote-Controlled-Banner-Project-L4L61QDWFI
Project: https://github.com/Python3-Training/TotalPythoneering
Status: Testing Success
'''

import socket
import sys

# Configuration to match the server
IP_HOST = '127.0.0.1'
IP_PORT = 65432

def client_banner(message, host=IP_HOST, port=IP_PORT):
    """Connects to the server and sends user input."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((host,int(port)))
            # Send data to the server, encoded to bytes
            s.sendall(message.encode('utf-8'))            
            # Receive the echo response back from the server
            return True, s.recv(1024)
    except ConnectionRefusedError:
        return False, f"Error: Connection refused. Is the server running at {host}:{port}?"
    except Exception as e:
        return False, f"An error occurred: {e}"

if __name__ == "__main__":
    print(client_banner('Testing.'))

