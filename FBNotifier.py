from fbchat import Client, log
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
startmessage = config.get("Messages","StartMessage")

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



client = Client(fbuseremail,fbuserpassword)
logging.debug('Own id: {}'.format(client.uid))

client.sendMessage(startmessage, thread_id=client.uid, thread_type=ThreadType.USER)
logging.debug('StartMessage has been sent to own ID')

client.logout()
logging.info('EdiNagFB logging out of Facebook session')

#client.listen

