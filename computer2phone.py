## Imports
import os
import string
import sys
import magic
from pushbullet import Pushbullet

## Text Effects
class effect:
    purple = '\033[95m'
    cyan = '\033[96m'
    darkcyan = '\033[36m'
    blue = '\033[94m'
    green = '\033[92m'
    yellow = '\033[93m'
    red = '\033[91m'
    bold = '\033[1m'
    underline = '\033[4m'
    end = '\033[0m'

## Start of Program
def push():
    os.system('cls' if os.name == 'nt' else 'clear')
    print effect.green + "Computer2Phone" + effect.end
    print effect.yellow + "========================================="
    print effect.purple + "What would you like to do?" + effect.end
    print effect.cyan + "1) Send text." + effect.end
    print effect.cyan + "2) Send a link." + effect.end
    print effect.cyan + "3) Send a file."
    print effect.cyan + "4) List all devices" + effect.end
    print effect.cyan + "5) Reconfigure your Pushbullet API key." + effect.end
    print effect.cyan + "6) Remove your API key." + effect.end
    a = input("Input number: ")
    
    if a == 1:
        title = raw_input(effect.red + "What would you like the title to be? " + effect.end)
        data = raw_input(effect.red + "What text would you like to send? " + effect.end)
        push = pb.push_note(title, data)
        again()
        
    elif a == 2:
        link = raw_input(effect.red + "What link would you like to send? " + effect.end)
        text = raw_input(effect.red + "What do you want the link text to be? " + effect.end)
        push = pb.push_link(text, link)
        again()
        
    elif a == 3:
        fileph = raw_input(effect.red + "Please type file path. " + effect.end)
        filenm = raw_input(effect.red + "What would you like your file name to be? " + effect.end)
        
        with open(path, "rb") as file:
            data = pb.upload_file(file, name)
            
        push = pb.push_file(**data)
        
    elif a == 4:
        print effect.green + "All Devices" + effect.end
        print effect.yellow + "=========================================" + effect.end
        print pb.devices 
    
    elif a == 5:
        print effect.red + "If you don't know how to find your API key visit this link: http://bit.ly/2e6xn40" + effect.end
        key = raw_input(effect.yellow + "What is your Pushbullet API key? " + effect.end)
        f = file("api-key.txt", "w")
        f.write(key)
        f.close()
        print effect.red + "For changes to take effect the program will close." + effect.end
        sys.exit()
        
    elif a == 6:
        confirm = raw_input( effect.red + "Are you sure you want to remove your API key? You'll have to re-run the install.sh script or manually re-edit the api-key.txt file. (Y/N) " + effect.end).lower()
        
        if confirm == "y":
            f = file("api-key.txt", "w")
            f.write("")
            f.close()
            
        else:
            push()
            
    else:
        push()

## Repeat
def again():

    g = raw_input(effect.red + "Would you like to send another? (y/n) " + effect.end).lower()
    if g == "y":
        push()

    elif g == "n":
            sys.exit()

    else: 
            again()

## Loads in API Key
f = file("api-key.txt", "r")
key = f.read()
if not len(key) > 0:
    print "Error, API key doesn't exist or is corrupt."
pb = Pushbullet(key)

push()
