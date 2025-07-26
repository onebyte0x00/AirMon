# AirMon
the plan is to  create a FOSS small system to monitors, processes, stores, and visualizes wireless signal (BT and Wifi) then expand it's functionality
it has to be small enough to work on raspberry pi zero W 2, with 512 MB of RAM. please take part in the project and contribute with ideas or code, you are welcome :)

for now, this app's prototype processes the logs, stores them in Elasticsearch, and provides visualization and alerting capabilities.
```
├── collectors/
│   ├── bluetooth_scanner.py # Bluetooth device detection
│   └── wifi_scanner.py      # WiFi network scanning
├── config/
│   ├── fluent-bit.conf      # Fluent Bit configuration
│   ├── logstash.conf        # Alternative Logstash config
│   ├── elastalert_config.yaml # ElastAlert main config
│   └── bluetooth_anomaly.yaml # Alert rules
├── alerts/
│   └── custom_alerts.py     # Custom alert scripts
├── docker-compose.yml       # Container orchestration
```

## Components
1. Collectors : Python scripts using Scapy and PyBluez
2. Log Processor : Fluent Bit or Logstash 
3. Storage : Elasticsearch
4. Visualization : Grafana
5. Alerting : ElastAlert with custom Python alerts


