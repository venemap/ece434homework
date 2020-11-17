## Running Program
1. Apply power to beaglebone
2. Make sure bone has internet
3. ./setup.sh
4. sudo ./main.py (requires sudo for framebuffer usage)

## config.py
This file holds all of the necessary api keys for the program to work. Twitter api keys are currently not necessary due to this feature not getting implemented (see TODO)
format of file is as follows:

config.py -->
consumer_key = 'insert twitter api key here'
consumer_secret = 'insert twitter api key here'
access_token = 'insert twitter api key here'
access_token_secret =  'insert twitter api key here'
   
owmkey = 'open weather api key here'

blynkKey = "blynk api key here"


## TODO
1. Migrate program to use beaglebone black wireless (or some equivalent) so that there is no need to pass internet via usb connection from pc
2. Fade background into different images based on what the weather is
3. Integrate twitter in some way (tweet when alarm goes off?), couldn't figure out a good way to integrate this feature in without it feeling shoehorned in
4. Create actual enclosure for display + bone