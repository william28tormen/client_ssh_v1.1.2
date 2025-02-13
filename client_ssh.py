import paramiko

host = 'IP HOST'
user = 'USER'
passwd  = 'PASSWD'

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(host, username=user, password=passwd)


while True:
    stdin, stdout, stderr = client.exec_command(input('Digite o comando:'))
    print('-----------------------------------------')
    for line in stdout.readlines():
        print(line.strip())

    erros = stderr.readlines()
    if erros:
        print('-----------------------------------------')
        print(erros)