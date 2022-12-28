from time import sleep
from sense_hat import SenseHat
# Python program to explain os.getenv() method
sense=SenseHat()
# importing os module 
import os
  
# Get the value of 'HOME'
# environment variable
key = ''
value='Home'
while(True) :
    
    os.getenv(key)
    if value == os.getenv(key) :

        sense.show_message("HOME")


