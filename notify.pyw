#!/usr/bin/env python3.6

from __future__ import print_function
import sys
import time
import pychromecast
from gtts import gTTS
import requests


# Set path to Domoticz
URL_DOMOTICZ = 'http://192.168.1.2:8080/'
req = requests.get('http://192.168.1.2:8080/json.htm?type=command&param=addlogmessage&message="Starting notify script"')



# Grab notification and chromecast device name
message = sys.argv[1] 
CCD = sys.argv[2]
req = requests.get('http://192.168.1.2:8080/json.htm?type=command&param=addlogmessage&message="Message: ' + message + ' Device: ' + CCD + '"')
print(message)
tts = gTTS(text=message, lang='en', slow=False)
# Saves the mp3 to the www/media directory within Domoticz 
# Edit to path to the location of your www/media directory
tts.save("C:/Program Files (x86)/Domoticz/www/media/notification.mp3")


# device_name is the name of the chromecast device or group that will play the message
# Edit to match your google device or group name
chromecasts = pychromecast.get_chromecasts()
cast = next(cc for cc in chromecasts if cc.device.friendly_name == CCD)
cast.wait()
print(cast.device)
print(cast.status)
mc = cast.media_controller
mc.play_media(URL_DOMOTICZ+'media/notification.mp3', 'audio/mp3')
mc.block_until_active()
#print(mc.status)
mc.play()
exit()
