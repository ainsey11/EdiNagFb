from fbchat import Client
from fbchat.models import *
from ConfigParser import SafeConfigParser

config = SafeConfigParser()
config.read ('config.ini')

fbuseremail = config.get("FacebookAuthDetails","Email")
fbuserpassword = config.get("FacebookAuthDetails","Password")

if fbuseremail = "FBEmailAddress"
    print("You have not set an e-mail address in the config.ini, exiting"
