from fbchat import Client
from fbchat.models import *
from ConfigParser import SafeConfigParser
import logging
import sys

config = SafeConfigParser()
config.read ('config.ini')

# Set logging= to DEBUG, WARNING or INFO. I have left as DEBUG whilst coding
logging.basicConfig(filename='EdiNagFBDebug.log',level=logging.DEBUG)

fbuseremail = config.get("FacebookAuthDetails","Email")
fbuserpassword = config.get("FacebookAuthDetails","Password")
configerrormessage = config.get("ErrorMessages","ConfigError")

logging.info('Loaded Configuration')
logging.debug('Performing Configuration Validation')

if fbuseremail == 'FBEmailAddress':
    print(configerrormessage)
    logging.warning('Email not set in config.ini')
    sys.exit(1)

if fbuserpassword == 'BlankPassword':
    print(configerrormessage)
    logging.warning('Password not set in config.ini')
    sys.exit(1)

