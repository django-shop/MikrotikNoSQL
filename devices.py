__author__ = 'podwar2008@gmail.com'
import shelve
import time, os
import socket

class Devices():
    def __init__(self):
        self.type_connect_list = ['ppp', 'ip', 'ip-mac', 'dhcp']
        self.db_devices = shelve.open('deviceslist')


    def f_add_device(self):

        info_device = []
        while True:
            ip_address_device = input("Введите ip адрес устройства: ")
            try:
                socket.inet_aton(ip_address_device)
            except :
                print('Вы ввели не правильное значение')
                time.sleep(1)
                os.system('cls')
            else:
                info_device.append(ip_address_device) #Добавляем ip адрес в список с данными об устройстве
                break

        def f_auth_type():
            x = 1
            sel_number = {}
            for i in self.type_connect_list:
                print (x, i)
                sel_number[x] = i
                x += 1
            return sel_number
        sel_number = f_auth_type()

        while True:

            try:
                auth_type = int(input("Введите номер типа авторизации: "))
            except :
                print('Вы ввели не правильное значение')
                time.sleep(3)
                os.system('cls')

            else:
                if not sel_number.get(auth_type):
                    print('Вы ввели не правильное значение')
                    time.sleep(1)
                    os.system('cls')

                else:
                    info_device.append(sel_number[auth_type]) #Добавляем тип авторизации
                    break
        while True:
            login_device = input("Введите имя администратора: ")
            if len(login_device) == 0:
                print('Вы ввели не правильное значение')
                time.sleep(1)
                os.system('cls')
            else:
                info_device.append(login_device)
                break

        while True:
            password_device = input("Введите введите пароль администратора: ")
            if len(password_device) == 0:
                print('Вы ввели не правильное значение')
                time.sleep(1)
                os.system('cls')
            else:
                info_device.append(password_device)
                break


        while True:
            try:
                ssh_port_device = int(input("Введите ssh порт устройства: "))
            except :
                print('Вы ввели не правильное значение')
                time.sleep(3)
                os.system('cls')
            else:
                info_device.append(ssh_port_device)
                break

        while True:
            name_interface = input("Введите название локального итерфейса: ")
            if len(name_interface) == 0:
                print('Вы ввели не правильное значение')
                time.sleep(1)
                os.system('cls')
            else:
                info_device.append(name_interface)
                break

        description_device = input("Введите произвольное описание для устройства: ")
        info_device.append(description_device)


        #print(info_device)
        #print(self.db_devices['all_device'])

        if len(self.db_devices) == 0:
            print ('Нет записей')
            self.db_devices['all_device'] = [info_device]
            self.db_devices.close()
        else:
            ip_list = []
            for i in self.db_devices['all_device']:
                ip_list.append(i[0])
            if ip_address_device in ip_list:
                return ('IP занят')
            else:
                new_devices = self.db_devices['all_device']
                new_devices.append(info_device)
                print (new_devices)
                self.db_devices['all_device'] = new_devices
                return ('Устройство добавлено')
            print(self.db_devices['all_device'])
            self.db_devices.close()
            print('Есть записи')


if __name__ == '__main__':
    device = Devices()
    print (device.f_add_device())
