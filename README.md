# EdiNagFB



EdiNagFB is part of the EdiNag suite utilized in aiding the awaking of a sleeping Ainsey11

## SO... What does it do



Ainsey (also known as potato) sleeps like a log.. the EdiNag suite is a set of tools that polls certain remote sources for set criteria, if the criteria is met, an Intel Edison board with LCD display and Buzzer will beep and display the item on the display.



At the moment, the basic suite has WorkAlerts.py (this is not on git at the moment of writing) this script polls Gmail utilising the imapclient library and will alert on ANY e-mail sent to my work e-mail when I am on call.



It will now include the EdiNagFB tool, this will poll Facebook messenger for a set string, from a set person, for example "oi potate" 



This is because I have a really bad habit of being sat in bed, talking to my girlfriend, and falling asleep. SO, I figured if I have a method that she can use to wake me up if I fall asleep or miss a message, it could be handy.



I'll also implement rate limiting, so at 5AM she can't spam me with 4 billion messages just to annoy me



### Tech



Requires 

    - python

    - fbchat module

    - import time

    - mraa

    - pyupm_i2clcd

    - pyupm_buzzer



### Installation

Install the dependencies and run install.sh
