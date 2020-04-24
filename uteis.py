import paramiko
import socket
import os
import nmap

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
nm = nmap.PortScanner()
hosts = []

def lookip(ip, port):
    nm.scan(ip, port)
    for host in nm.all_hosts():
        hosts.append(host)
    return hosts

def conect():
    for devices in lookip('192.168.0.0/24', '22-443'):
        try:
            ssh.connect(devices, username='qwerty', password='init4289')
            print("conectado")
            ssh.exec_command('eject -r')
        except:
            continue
