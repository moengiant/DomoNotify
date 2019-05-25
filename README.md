# DomoNotify
This is a notification script that uses the pychromecast and gTTS modules to speak notifications to any Chromecast device on your network

1) Add the notify.py script in the scripts/python directory in Domoticz. 
2) Add notifications to a device and pass the vars to the script using the following parameters: "Notification message" "Chromecast device name" Reference "Device Notification Example.png" to see an example 
3) In Domoticz settings -> notifications change the URL/Action field under the Custom HTTP/Actions settings to the following: script://scripts\python\notify.pyw #MESSAGE (this path works on Windows 10 - path for other operating systems this path may be different) Reference Settings.pn for an example

Enjoy
