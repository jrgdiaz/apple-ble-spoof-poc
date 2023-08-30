from scapy.all import *

print('connecting to local bluetooth interface')
bt = BluetoothHCISocket(0)

def begin_sniff(bt):
        print('\nsniffing now:\ninterrupt to finish sniffing')
        pkts = bt.sniff()
        print(pkts)
        print('\nsaving capture to file')
        wrpcap("/tmp/pkts.pcap", pkts)
        #to read back -> pkts = rdpcap("/tmp/bluetooth.pcap")

def test_bt(bt):
        print('test bluetooth communication stack')
        ans, unans = bt.sr(HCI_Hdr()/HCI_Command_Hdr())
        p = ans[0][1]
        p.show()

def enable_ble_discovery_mode(bt):
        # type=1: Active scanning mode
        print('enabling ble discovery mode')
        bt.sr(HCI_Hdr()/HCI_Command_Hdr()/HCI_Cmd_LE_Set_Scan_Parameters(type=1))
        # filter_dups=False: Show duplicate advertising reports, because these sometimes contain different data!
        bt.sr(HCI_Hdr()/HCI_Command_Hdr()/HCI_Cmd_LE_Set_Scan_Enable(enable=True,filter_dups=False))

def disable_ble_discovery_mode(bt):
        print('disabling ble discovery mode')
        bt.sr(HCI_Hdr()/HCI_Command_Hdr()/HCI_Cmd_LE_Set_Scan_Enable(enable=False))

def read_ble_adverts(bt):
        #The lfilter will drop anything that's not an advertising report.
        print('\nsniffing adverts now:\ninterrupt to finish sniffing')
        adverts = bt.sniff(lfilter=lambda p: HCI_LE_Meta_Advertising_Reports in p)
        print(adverts)
        print('\nsaving adverts to capture to file')
        wrpcap("/tmp/adverts.pcap", adverts)
        return adverts

def filter_ble_adverts(adverts):
        from itertools import chain
        reports = chain.from_iterable(p[HCI_LE_Meta_Advertising_Reports].reports for p in adverts)
        # Group reports by MAC address (consumes the reports generator)
        devices = {}
        for report in reports:
                device = devices.setdefault(report.addr, [])
                device.append(report)
        # Packet counters
        devices_pkts = dict((k, len(v)) for k, v in devices.items())
        print(devices_pkts)
        # {'xx:xx:xx:xx:xx:xx': 408, 'xx:xx:xx:xx:xx:xx': 2}
        return devices

def filter_ble_adverts_by_uuid(devices, uuid):
        # Get one packet for each device that broadcasted short UUID 0xfe50 (Google).
        # Android devices broadcast this pretty much constantly.
        google = {}
        for mac, reports in devices.items():
                for report in reports:
                        if (EIR_CompleteList16BitServiceUUIDs in report and uuid in report[EIR_CompleteList16BitServiceUUIDs].svc_uuids):
                                google[mac] = report
                                break
        # List MAC addresses that sent such a broadcast
        print(google.keys())
        # dict_keys(['xx:xx:xx:xx:xx:xx', 'xx:xx:xx:xx:xx:xx'])

def analyze_advertising_report(adverts):
        from itertools import chain
        reports = chain.from_iterable(p[HCI_LE_Meta_Advertising_Reports].reports for p in adverts)
        # Group reports by MAC address (consumes the reports generator)
        devices = {}
        for report in reports:
                device = devices.setdefault(report.addr, [])
                device.append(report)
        apple = {}
        for mac, reports in devices.items():
                for report in reports:
                        if (EIR_Manufacturer_Specific_Data in report):
                                print(f"Device Manufacturer 16 bit uuid: {report[EIR_Manufacturer_Specific_Data].company_id}")
                        if (EIR_Manufacturer_Specific_Data in report and report[EIR_Manufacturer_Specific_Data].company_id == 76):
                                atype = 'public'
                                if report.atype == 1:
                                        atype = 'random'
                                print(f"BLE ADVERTISEMENT of Apple device @ {mac} with a {atype} address - RSSI {report.rssi} - ADV TYPE {report.type} - DATA - {report.data} ")
                                apple[mac] = report
        print("apple ble raw advertisement data")
        print(apple.items())


test_bt(bt)
enable_ble_discovery_mode(bt)
adverts = read_ble_adverts(bt)
#devices = filter_ble_adverts(adverts)
#print(devices)
analyze_advertising_report(adverts)
disable_ble_discovery_mode(bt)
