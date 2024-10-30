#!/usr/bin/python3
from scapy.all import *
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style
import time

print('connecting to local bluetooth interface')
bt = BluetoothHCISocket(0)

def test_bt(bt):

        ans, unans = bt.sr(HCI_Hdr()/HCI_Command_Hdr())
        p = ans[0][1]
        p.show()

def enable_ble_discovery_mode(bt):
        bt.sr(HCI_Hdr()/HCI_Command_Hdr()/HCI_Cmd_LE_Set_Scan_Parameters(type=1))
        bt.sr(HCI_Hdr()/HCI_Command_Hdr()/HCI_Cmd_LE_Set_Scan_Enable(enable=True,filter_dups=True))

def disable_ble_discovery_mode(bt):
        bt.sr(HCI_Hdr()/HCI_Command_Hdr()/HCI_Cmd_LE_Set_Scan_Enable(enable=False))

def read_ble_adverts(bt):
        print('\nsniffing adverts now:\ninterrupt to finish sniffing')
        adverts = bt.sniff(lfilter=lambda p: HCI_LE_Meta_Advertising_Reports in p)
        return adverts

def analyze_advertising_report(adverts):
        from itertools import chain
        reports = chain.from_iterable(p[HCI_LE_Meta_Advertising_Reports].reports for p in adverts)
        devices = {}
        for report in reports:
                device = devices.setdefault(report.addr, [])
                device.append(report)
        apple = {}
        for mac, reports in devices.items():
                for report in reports:
                        if (EIR_Manufacturer_Specific_Data in report):
                                #print(f"Device Manufacturer 16 bit uuid: {report[EIR_Manufacturer_Specific_Data].company_id}")
                                ...
                        if (EIR_Manufacturer_Specific_Data in report and report[EIR_Manufacturer_Specific_Data].company_id == 76):
                                atype = 'public'
                                if report.atype == 1:
                                        atype = 'random'
                                time.sleep(2)
                                print(f"{Fore.LIGHTGREEN_EX}APPLE DEVICE MAC ADDRESS:{Style.RESET_ALL} {Fore.LIGHTWHITE_EX}{mac}{Style.RESET_ALL} | {Fore.LIGHTBLUE_EX}ADDRESS PRIVACY SETTING:{Style.RESET_ALL} {Fore.LIGHTWHITE_EX}{atype}{Style.RESET_ALL} |  {Fore.LIGHTMAGENTA_EX}SIGNAL STRENGTH RSSI:{Style.RESET_ALL} {Fore.LIGHTWHITE_EX}{report.rssi}{Style.RESET_ALL} | {Fore.LIGHTCYAN_EX}ADVERTISEMENT TYPE:{Style.RESET_ALL} {Fore.LIGHTWHITE_EX}{report.type}{Style.RESET_ALL} | {Fore.LIGHTRED_EX}DATA:{Style.RESET_ALL}  {Fore.LIGHTYELLOW_EX}{report.data}{Style.RESET_ALL}")
                                apple[mac] = report




enable_ble_discovery_mode(bt)
adverts = read_ble_adverts(bt)
colorama_init()
analyze_advertising_report(adverts)
disable_ble_discovery_mode(bt)
