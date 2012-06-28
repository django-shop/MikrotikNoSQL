__author__ = 'Dev'

from mikrotik import Mikrotik
from add_user import User

user = User()
user.add_user()
print user.enter_data
print user.sel_device
mikrotik = Mikrotik()
mikrotik.add_user_mikrotik(user.sel_device, user.enter_data)
