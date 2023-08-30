# apple-ble-spoof-poc

A simple Apple BLE Airpods spoofing POC based on Scapy; Inspired on DEFCON 31's Apple TV spoof attacks.

https://techcrunch.com/2023/08/16/this-70-device-can-spoof-an-apple-device-and-trick-you-into-sharing-your-password/

* util/ibeacon.py contains slightly modified scapy contrib code based on the original: https://github.com/secdev/scapy/blob/master/scapy/contrib/ibeacon.py

* util/ibeacon.py substitutes the original ibeacon.py that is located in the filesystem in my case the path was /usr/local/lib/python3.7/dist-packages/scapy/contrib/ibeacon.py


* util/btconfig.sh helps reset the bluetooth interface of a Raspberry Pi Zero W before running the spoof POC.


* spoof/apple-airpods-spoof.py is the script that performs THE spoof attack itself, handles the Pi's bluetooth interface and sends out the airpods' advertising packets. Should be run with sudo.




