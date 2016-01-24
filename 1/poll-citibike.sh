#/usr/bin/env bash
while true; do curl -s https://www.citibikenyc.com/stations/json | jq -c .stationBeanList[0]; sleep 2; done
