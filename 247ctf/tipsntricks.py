#!/usr/bin/python3 

from pwn import * 

io = remote('2b4e9ca4324f56db.247ctf.com',50378)
#io.send(b'')
#val = (io.recv(2048)) 
#print(val.split(b'\n'))
val = b''
while b"247CTF{" not in val:
    val = (io.recvline()) 
    if b'What is the answer to' in val:
        print(val)
        val2 = val.split(b' ')
        add1 = int(val2[-3])
        add2 = int((val2[-1].split(b'?'))[0])
        sum=str(add1+add2) + "\r\n"
        io.send(sum.encode())
    
print(val)
    #.split(b'\n'))