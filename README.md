# AirMon
the plan is to  create a FOSS small system to monitors, processes, stores, and visualizes wireless signal (BT and Wifi) then expand it's functionality
it has to be small enough to work on raspberry pi zero W 2, with 512 MB of RAM.

for now, this app's prototype processes the logs, stores them in Elasticsearch, and provides visualization and alerting capabilities.
├── collectors/
│   ├── bluetooth_scanner.py
│   └── wifi_scanner.py
├── config/
│   ├── fluent-bit.conf
│   ├── logstash.conf
│   ├── elastalert_config.yaml
│   └── bluetooth_anomaly.yaml
├── alerts/
    └── custom_alerts.py
docker-compose.yml

## Components
1. Collectors : Python scripts using Scapy and PyBluez
2. Log Processor : Fluent Bit or Logstash 
3. Storage : Elasticsearch
4. Visualization : Grafana
5. Alerting : ElastAlert with custom Python alerts


