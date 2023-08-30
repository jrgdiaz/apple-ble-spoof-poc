sudo hciconfig hci0 down
sudo hciconfig hci0 up
sudo hciconfig hci0 leadv 3
sudo hciconfig hci0 noscan
sudo ./spooftooph-bin -a <spoofed-ble-mac-address-here>
sudo hciconfig hci0 reset
