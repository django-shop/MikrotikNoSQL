import shelve


db = shelve.open('userslist')
print (db)
#if len(db) == 0:
db['users'] = [user_name]
db.close()