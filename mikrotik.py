# -*- coding: utf-8 -*-
from paramiko import SSHClient
from paramiko import AutoAddPolicy
import time

class Mikrotik():
    def add_user_mikrotik(self, sel_device, enter_data):
        if sel_device[1] == 'ppp':
            print sel_device[1]
            ssh = SSHClient()
            ssh.set_missing_host_key_policy(AutoAddPolicy())
            try:
                ssh.connect(sel_device[0], port=int(sel_device[4]), username=sel_device[2], password=sel_device[3])
            except :
                return 'Нет связи с сервером'
            else:
                cmd = "/ppp secret add name=%s password=%s service=any profile=default local=172.16.1.1 remote=%s" % (enter_data[0], enter_data[1], enter_data[2])
                ssh.exec_command(cmd)
                time.sleep(1)

                cmd = "/ip fi address-list add address=%s list=%s" % (enter_data[2], 'working')
                ssh.exec_command(cmd)
                time.sleep(1)

                cmd = "/queue simple add name=%s target-addresses=%s max-limit=%s%s/%s%s" % (enter_data[0], enter_data[2], '5', 'M', '10', 'M')
                ssh.exec_command(cmd)
                ssh.close()

                return 'Клиент добавлен'

        if sel_device[1] == 'ip':
            print sel_device[1]
            ssh = SSHClient()
            ssh.set_missing_host_key_policy(AutoAddPolicy())
            ssh.connect("192.168.5.220", port=22, username="user1", password="1q2w3e")
            cmd = "/ppp secret add name=%s password=%s service=any profile=default local=172.16.1.1 remote=%s" % (login, password, ipaddress)
            ssh.exec_command(cmd)
            ssh.close()

        if sel_device[1] == 'ip-mac':
            print sel_device[1]
            ssh = SSHClient()
            ssh.set_missing_host_key_policy(AutoAddPolicy())
            ssh.connect("192.168.5.220", port=22, username="user1", password="1q2w3e")
            cmd = "/ppp secret add name=%s password=%s service=any profile=default local=172.16.1.1 remote=%s" % (login, password, ipaddress)
            ssh.exec_command(cmd)
            ssh.close()

        if sel_device[1] == 'dhcp':
            print sel_device[1]
            ssh = SSHClient()
            ssh.set_missing_host_key_policy(AutoAddPolicy())
            ssh.connect("192.168.5.220", port=22, username="user1", password="1q2w3e")
            cmd = "/ppp secret add name=%s password=%s service=any profile=default local=172.16.1.1 remote=%s" % (login, password, ipaddress)
            ssh.exec_command(cmd)
            ssh.close()




