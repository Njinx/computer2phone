#!/bin/sh
echo "Install Python/PIP..."
sudo apt-get install python-pip
echo "Installing python-requests..."
pip install requests
echo "Installing python-magic..."
pip install python-magic
echo "Installing pushbullet.py..."
pip install pushbullet.py
keygen() {
    echo "==============================================================================================="
    echo "To use the pushbullet API we need your API key. If you aren't sure how to get your API key, visit this site: https://docs.pushbullet.com/#api-quick-start"
    echo "Please type your API key here:"
    read key
    echo -n $key > api-key.txt
}
if [ -a api-key.txt ]; then
    keygen
else
    touch api-key.txt
    keygen
fi
echo "Finished Installing!"