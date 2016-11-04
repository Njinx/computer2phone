# Computer2Phone
This is a simple python program that send custom messages or links to your other devices via the Pushbullet API.

# Intentions
This project was made as a simple test to show how useful the Pushbullet API can be.

# Installation
  This project is (currently) only optimized for Debian based Linux distrobutions meaning it only comes with a bash install script. 
To install simply run the bash script (preferably as superuser.) The bash script will then install the dependencies and prompt you for 
your Pushbullet API key. To obtain your pushbullet API key simply log in to your Pushbullet account and navigate to "Settings>Account"
then scroll down to "Access Token" click "Create new access token" and a long string will be generated.
Copy then paste that into the install prompt. That should finish up and you should be able to run computer2phone.py (python computer2phone.py)

If you're running something besides Linux you can still use this program. To do so you must install the following dependencies via PIP:
  
  1. requests
  2. python-magic
  3. pushbullet.py
  
Then you'll need to edit the "api-key.txt" file and paste your API key in making sure there aren't any line breaks, tabs, or spaces. 
You then should be able to run the python file.
