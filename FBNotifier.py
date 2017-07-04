from fbchat import Client
from fbchat.models import *
from ConfigParser import SafeConfigParser

config = SafeConfigParser()
config.read ('config.ini')

fbuseremail = config.get("FacebookAuthDetails","Email")
fbuserpassword = config.get("FacebookAuthDetails","Password")

print('Using' $fbuseremail 'as username')

