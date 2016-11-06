# Computer2Phone
This is a simple python program that sends custom messages or links to your other devices via the Pushbullet API.

## Intentions
This project was made as a simple test to show how useful the Pushbullet API can be.

## Installation
  This project is (currently) only optimized for Debian based Linux distributions meaning it only comes with a bash install script. 
To install simply run the bash script (preferably as superuser.) The bash script will then install the dependencies and prompt you for 
your Pushbullet API key. To obtain your pushbullet API key simply log in to your Pushbullet account and navigate to "Settings>Account"
then scroll down to "Access Token" click "Create new access token" and a long string will be generated.
Copy then paste that into the install prompt. That should finish up and you should be able to run computer2phone.py (python computer2phone.py)

If you're running something besides Linux you can still use this program. To do so you must install the following dependencies via PIP:
  
  1. requests
  2. python-magic
  3. pushbullet.py
  
Then you'll need to create a text file called "api-key.txt" and paste your API key in making sure there aren't any line breaks, tabs, or spaces. 
You then should be able to run the python file.

## Troubleshooting
#### Here are a list of common errors you may encounter

    Traceback (most recent call last):
      File "computer2phone.py", line 72, in <module>
        f = file("api-key.txt", "r")
    IOError: [Errno 2] No such file or directory: 'api-key.txt'
This error indicates that no api-key.txt was found. This usually happens because you forgot to run the install.sh. 
This can be fixed by simply running the install.sh or creating an empty file called "api-key.txt"

    E: Unable to locate package python-pip
This error usually occurs because your system repositories aren't up to date. 
This can usually be fixed by running `sudo apt-get update`.

    Error, API key doesn't exist or is corrupt.
    Traceback (most recent call last):
      File "computer2phone.py", line 76, in <module>
        pb = Pushbullet(key)
      File "/usr/local/lib/python2.7/dist-packages/pushbullet/pushbullet.py", line 29, in __init__
        self.refresh()
      File "/usr/local/lib/python2.7/dist-packages/pushbullet/pushbullet.py", line 288, in refresh
        self._load_devices()
      File "/usr/local/lib/python2.7/dist-packages/pushbullet/pushbullet.py", line 42, in _load_devices
        resp_dict = self._get_data(self.DEVICES_URL)
      File "/usr/local/lib/python2.7/dist-packages/pushbullet/pushbullet.py", line 35, in _get_data
        raise InvalidKeyError()
    pushbullet.errors.InvalidKeyError
This error occurs because "api-key.txt" either exists and is empty or is corrupt. To fix this simply paste the correct API key making sure no spaces, line breaks, or tabs exist.