import paramiko

SSH = paramiko.SSHClient()
SSH.set_missing_host_key_policy(paramiko.AutoAddPolicy())

def lookip(ip_number, login_name, password_number, shell_command):
    SSH.connect(ip_number, username=login_name, password=password_number)
    SSH.exec_command(shell_command)
    SSH.close()
