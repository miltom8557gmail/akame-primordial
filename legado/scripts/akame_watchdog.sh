#!/bin/bash
while true; do
  pgrep -f akame_telegram.py > /dev/null || nohup python ~/AkamePortal/akame_telegram.py > ~/AkamePortal/logs/telegram_eterno.log 2>&1 &
  pgrep -f nexus_bridge.py > /dev/null || nohup python ~/AkamePortal/nexus_bridge.py > ~/AkamePortal/logs/nexus_eterno.log 2>&1 &
  sleep 60
done
