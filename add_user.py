import shelve

#Функция извлечения данных из хранилища
def get_db(user_name):
    db = shelve.open('userslist')
    if len(db) == 0:
        db['users'] = [user_name]
        db.close()
    else:
        connect_users_list =  db['users']
        print(connect_users_list)
        if user_name in connect_users_list:
            print('Логин существует')
            db.close()
        else:
            print('Логин не существует')
            connect_users_list.append(user_name)
            print(connect_users_list)
            db.close()
            add_db(connect_users_list)


#
def add_db(connect_users_list):
    db = shelve.open('userslist')
    db['users'] = connect_users_list
    db.close()

user_name = input("Ввести: ")
get_db(user_name)