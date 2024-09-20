# apple-ble-spoof-poc

Apple BLE spoof PoC implemented with Scapy.

This project is created only for educational purposes

In the news:

https://techcrunch.com/2023/08/16/this-70-device-can-spoof-an-apple-device-and-trick-you-into-sharing-your-password/

Setup:

* Tested on a Raspberry Pi Zero W with USB UD100 Bluetooth Dongle.

* util/ibeacon.py contains slightly modified scapy code but it's still based on the original and can be found here:
   
  https://github.com/secdev/scapy/blob/master/scapy/contrib/ibeacon.py

* Substitute the original ibeacon.py with util/ibeacon.py
  The default ibeacon.py file location can be typically found in:
  
  /usr/local/lib/python{-version}/dist-packages/scapy/contrib/ibeacon.py


* util/btconfig.sh bash script configures & reset the bluetooth interface of the Raspberry Pi Zero W prior to running 
  the spoof PoC script. Uses spooftooph-bin, you can check it here:
  
  https://www.kali.org/tools/spooftooph/


* spoof/apple-airpods-spoof.py is the script that performs THE spoof attack itself, handles the Pi's bluetooth 
  interface and sends out spoofed airpods' advertising packets. Should be run with sudo.

* For the demonstration, btconfig.sh & spoof/apple-airpods-spoof.py were placed in a cronjob to run at boot on the RPi 
  with the Bluetooth dongled connected.




