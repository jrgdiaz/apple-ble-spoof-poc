from scapy.all import *
# Load the contrib module for iBeacon
load_contrib('ibeacon')
bt = BluetoothHCISocket(0)
# Beacon data consists of a UUID, and two 16-bit integers: "major" and
# "minor".
#
# iBeacon sits on top of Apple's BLE protocol.
p = Apple_BLE_Submessage()/IBeacon_Data(
   uuid='2f234454-cf6d-4a0f-adf2-f4911ba9ffa6',
   major=1, minor=2)
print(p.show())
# build_set_advertising_data() wraps an Apple_BLE_Submessage or
# Apple_BLE_Frame into a HCI_Cmd_LE_Set_Advertising_Data payload, that can
# be sent to the BLE controller.
bt.sr(p.build_set_advertising_data())
bt.sr(HCI_Hdr()/HCI_Command_Hdr()/HCI_Cmd_LE_Set_Advertising_Parameters(adv_type=3,interval_min=1048,interval_max=1048,oatype=0))
ans, unans = bt.sr(HCI_Hdr()/
      HCI_Command_Hdr()/
      HCI_Cmd_LE_Set_Advertise_Enable(enable=True), inter=1.5, retry=10)


x = ans[0][1]
print(x.show())
