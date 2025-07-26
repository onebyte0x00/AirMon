#!/usr/bin/env python3
import json
import time
import logging
from bluetooth import discover_devices

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class BluetoothScanner:
    def __init__(self, scan_interval=60):
        self.scan_interval = scan_interval
    
    def scan_devices(self):
        try:
            nearby_devices = discover_devices(lookup_names=True, duration=8)
            return [
                {"address": addr, "name": name} 
                for addr, name in nearby_devices
            ]
        except Exception as e:
            logging.error(f"Bluetooth scan failed: {e}")
            return []

    def run(self):
        while True:
            devices = self.scan_devices()
            if devices:
                log_entry = {
                    "timestamp": int(time.time()),
                    "event_type": "bluetooth_scan",
                    "devices": devices,
                    "count": len(devices)
                }
                print(json.dumps(log_entry))
            
            time.sleep(self.scan_interval)

if __name__ == "__main__":
    scanner = BluetoothScanner()
    scanner.run()
