#!/usr/bin/env python3
import sys
import smtplib
from email.mime.text import MIMEText
import logging
from elasticsearch import Elasticsearch

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class AlertHandler:
    def __init__(self):
        self.es = Elasticsearch(['elasticsearch:9200'])
        
    def handle_bluetooth_anomaly(self):
        query = {
            "size": 0,
            "query": {
                "range": {"@timestamp": {"gte": "now-1h/h"}}
            },
            "aggs": {
                "unique_devices": {
                    "cardinality": {"field": "devices.address"}
                }
            }
        }
        
        res = self.es.search(index="bluetooth-wifi-*", body=query)
        count = res['aggregations']['unique_devices']['value']
        self.send_email(
            "Bluetooth Anomaly Detected",
            f"Found {count} unique Bluetooth devices in the last hour"
        )
    
    def send_email(self, subject, body):
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = "alerts@yourdomain.com"
        msg['To'] = "security-team@yourdomain.com"
        
        try:
            with smtplib.SMTP('smtp.yourdomain.com') as server:
                server.send_message(msg)
            logging.info("Alert email sent successfully")
        except Exception as e:
            logging.error(f"Failed to send alert email: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: custom_alerts.py <alert_type>")
        sys.exit(1)
    
    handler = AlertHandler()
    alert_type = sys.argv[1]
    
    if alert_type == "bluetooth_anomaly":
        handler.handle_bluetooth_anomaly()
    else:
        logging.error(f"Unknown alert type: {alert_type}")
