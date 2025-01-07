# pip3 install paramiko
import paramiko
from threading import Thread

fp = open("VALID.txt", 'w')
def check_ssh_connection(ip_port_user_pass):
    try:
        zapros = ip_port_user_pass.split(' ')
        ip, port = zapros[0].split(':')
        user, password = zapros[1].split(':')

        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        client.connect(hostname=ip, port=int(port), username=user, password=password, timeout=0.5)

        print(f"SSH connection to {ip}:{port} with user '{user}' is VALID")
        fp.write(f"{ip}:{port},{user}:{password}\n")

        client.close()
    except Exception as e:
        print(f"Invalid: {e}")

def checking(part, numpart, ssh2file):
    try:
        for linezz in part:
            check_ssh_connection(linezz, ssh2file)
    except Exception as e:
        ssh2file.close()
        print(f"The [{numpart}] is ended working. {e}")

with open('ips.txt', 'r') as f:
    lines = [line.replace("\n", "") for line in f.readlines()]

for line in lines:
    try:
        check_ssh_connection(line)
    except KeyboardInterrupt:
        print("Saving...")
        fp.close()
        break
    except Exception as e:
        print(f"Invalid: {e}")
