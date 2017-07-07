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
logging.debug('Loaded FB Auth E-mail')
fbuserpassword = config.get("FacebookAuthDetails","Password")
logging.debug('Loaded FB Auth Password')
configerrormessage = config.get("ErrorMessages","ConfigError")
logging.debug('Loaded Configuration Error Message')
startmessage = config.get("Messages","StartMessage")
logging.debug('Loaded Startup Message')
activatedmessage = config.get("Messages","ActivatedMessage")
logging.debug('Loaded Activated Message')
triggeruser = config.get("TriggerInfo","TriggerUser")
logging.debug('Loaded Trigger Username')
logging.info('Loaded Configuration')
logging.debug('Performing Configuration Validation')

if fbuseremail == 'FBEmailAddress':
    print(configerrormessage)
    logging.debug('Checking FB E-mail Address is not default')
    logging.warning('Email not set in config.ini')
    sys.exit(1)

if fbuserpassword == 'BlankPassword':
    print(configerrormessage)
    logging.debug('Checking FB Password is not default')
    logging.warning('Password not set in config.ini')
    sys.exit(1)

if triggeruser == 'TriggerUsername':
    print(configerrormessage)
    logging.debug('Checking Trigger username is not default')
    logging.warning('Trigger Username not set in config.ini')
    sys.exit(1)

client = Client(fbuseremail,fbuserpassword)
logging.debug('Fetching own FB UID')
logging.debug('Own id: {}'.format(client.uid))

client.sendMessage(startmessage, thread_id=client.uid, thread_type=ThreadType.USER)
logging.debug('StartMessage has been sent to own ID')

user = client.searchForUsers(triggeruser)[0]
print('user ID: {}'.format(user.uid))
print("user's name: {}".format(user.name))
triggeruseruid =('user ID: {}'.format(user.uid))

messages = client.fetchThreadMessages(thread_id="100003482325927", limit=1)
print('Latest Message is:') 
for message in messages:
    print(message.text)
    if message.text == "oi potate":
        client.sendMessage(activatedmessage, thread_id=triggeruseruid, thread_type=ThreadType.USER)
	print('OI WAKE UP POTATE')

client.logout()
logging.info('EdiNagFB logging out of Facebook session')

