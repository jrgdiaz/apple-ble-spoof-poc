# apple-ble-spoof-poc

Apple BLE Spoof PoC implemented with Scapy.

In the news:

https://techcrunch.com/2023/08/16/this-70-device-can-spoof-an-apple-device-and-trick-you-into-sharing-your-password/

Setup:

* util/ibeacon.py contains slightly modified scapy code but it's still based on the original and can be found here: https://github.com/secdev/scapy/blob/master/scapy/contrib/ibeacon.py

* Substitute the original ibeacon.py with util/ibeacon.py. Which is located in the filesystem, in my case the path was /usr/local/lib/python3.7/dist-packages/scapy/contrib/ibeacon.py


* util/btconfig.sh bash script helps configure & reset the bluetooth interface of the Raspberry Pi Zero W before running the spoof PoC script.


* spoof/apple-airpods-spoof.py is the script that performs THE spoof attack itself, handles the Pi's bluetooth interface and sends out spoofed airpods' advertising packets. Should be run with sudo.




