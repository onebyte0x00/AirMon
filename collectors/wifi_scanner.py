#!/usr/bin/env python33
from scapy.all import *
import json
import time
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class WiFiScanner:
    def __init__(self, interface="wlan0", scan_duration=10):
        self.interface = interface
        self.scan_duration = scan_duration
        self.seen_devices = set()

    def packet_handler(self, pkt):
        if pkt.haslayer(Dot11):
            mac = pkt.addr2
            if mac not in self.seen_devices:
                self.seen_devices.add(mac)
                log_entry = {
                    "timestamp": int(time.time()),
                    "event_type": "wifi_probe",
                    "mac": mac,
                    "ssid": pkt.info.decode() if pkt.info else None,
                    "signal_strength": pkt.dBm_AntSignal if hasattr(pkt, 'dBm_AntSignal') else None,
                    "channel": pkt.Channel if hasattr(pkt, 'Channel') else None
                }
                print(json.dumps(log_entry))

    def run(self):
        logging.info(f"Starting WiFi monitoring on interface {self.interface}")
        sniff(
            iface=self.interface,
            prn=self.packet_handler,
            monitor=True,
            timeout=self.scan_duration
        )

if __name__ == "__main__":
    while True:
        scanner = WiFiScanner()
        scanner.run()
        time.sleep(5)  # Brief pause between scans
