## Imports
import string
import subprocess as sp
import sys
import magic
from pushbullet import Pushbullet

## Clear Screen
tmp = sp.call('clear',shell=True)

## Start of Program
def push():
    
    print "Computer2Phone"
    print "========================================="
    print "What would you like to do?"
    print "1) Send text."
    print "2) Send a link."
    print "3) Reconfigure your Pushbullet API key."
    print "4) Remove your API key."
    ans = float(input("(Default is 1) "))
    
    if ans == 1:
        title = raw_input("What would you like the title to be? ")
        data = raw_input("What text would you like to send? ")
        push = pb.push_note(title, data)
        again()
        
    elif ans == 2:
        link = raw_input("What link would you like to send? ")
        text = raw_input("What do you want the link text to be? ")
        push = pb.push_link(text, link)
        again()
        
    elif ans == 3:
        print "If you don't know how to find your API key visit this link: http://bit.ly/2e6xn40"
        key = raw_input("What is your Pushbullet API key? ")
        f = file("api-key.txt", "w")
        f.write(key)
        f.close()
        print "For changes to take effect the program will close."
        sys.exit()
        
    elif ans == 4:
        confirm = raw_input("Are you sure you want to remove your API key? You'll have to rerun the install.sh script or manually re-edit the api-key.txt file. (Y/N) ").lower()
        
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
    
	again = raw_input("Would you like to send another? (y/n) ").lower()
	if again == "y":
		push()
        
	elif again == "n":
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