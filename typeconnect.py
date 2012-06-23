__author__ = 'podwar2008@gmail.com'

class Typeconnect():
    def __init__(self, select_type_coonect=None):
        if select_type_coonect == 'ppp':
            self.list_fields = ['login', 'password', 'ip']
        elif select_type_coonect == 'ip':
            self.list_fields = ['login', 'ip']
        elif select_type_coonect == 'ip-mac':
            self.list_fields = ['login', 'ip', 'mac']
        elif select_type_coonect == 'dhcp':
            self.list_fields = ['login', 'ip', 'mac']
        else:
            self.list_fields = []



if __name__ == "__main__":
    obj_type_connect = Typeconnect('ip')
    print (obj_type_connect.list_fields)
