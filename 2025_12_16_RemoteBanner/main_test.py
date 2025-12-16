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

from EchoClientTcp import client_banner as echo

def create(*args, **kwargs):
    return echo('Create?')

def move(*args, **kwargs):
    return echo('Move?')

def use(*args, **kwargs):
    return echo('Use?')

def my_help(*args, **kwargs):
    return echo('Help!')

ops = {
    '[C]reate': create,
    '[M]ove':   move,
    '[U]se':    use,
    '[D]one':   quit, # built in!
    '[H]elp':   my_help
    }

while True: # loop forever!
    for key in ops:
        print(key)
    op = input("? ").strip()
    if len(op) == 1:
        for k in ops:
            if k[1] == op.upper():
                print(f'!{k}({ops[k]()})')
                break
    else:
        print("Nope.")


