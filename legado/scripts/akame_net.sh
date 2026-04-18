#!/data/data/com.termux/files/usr/bin/bash
echo "🌐 [ESCANEANDO REDE OMNI...]"
nmap -sn 192.168.1.0/24 | grep "Nmap scan report"
