from fbchat import Client
from fbchat.models import *
from ConfigParser import SafeConfigParser
import logging


config = SafeConfigParser()
config.read ('config.ini')

# Set logging= to DEBUG, WARNING or INFO. I have left as DEBUG whilst coding
logging.basicConfig(filename='EdiNagFBDebug.log',level=logging.DEBUG)

fbuseremail = config.get("FacebookAuthDetails","Email")
fbuserpassword = config.get("FacebookAuthDetails","Password")

print(fbuseremail)
if fbuseremail == 'FBEmailAddress':
    print("You have not set an e-mail address in the config.ini, exiting")
#    logging.debug('Email not set in config.ini, exiting.')
