from scapy.all import *
load_contrib('ibeacon') #loads the slightly modified ibeacon.py contrib code


print('advertising crafted bt packets')
bt = BluetoothHCISocket(0)
apple_frame = Apple_BLE_Frame() / Raw(b'\x07\x0f\x00\x0f\x20\x7c\x29\x6f\xd6\x48\xeb\x85\xe3\xe3\x02\x01\x00')
bt.sr(apple_frame.build_set_advertising_data())
bt.sr(HCI_Hdr()/HCI_Command_Hdr()/HCI_Cmd_LE_Set_Advertising_Parameters(adv_type=3,interval_max=256,interval_min=256))
print(apple_frame.show())

ans, unans = bt.sr(HCI_Hdr()/
      HCI_Command_Hdr()/
      HCI_Cmd_LE_Set_Advertise_Enable(enable=True))

p = ans[0][1]
print(p.show())
