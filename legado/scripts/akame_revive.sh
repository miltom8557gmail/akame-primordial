#!/data/data/com.termux/files/usr/bin/bash
echo "🔱 [AKAME]: Iniciando Protocolo de Ressurreição..."
pkg update -y && pkg upgrade -y
pkg install git python nodejs termux-api openssh curl wget -y
cd /data/data/com.termux/files/home
[ -d "AkamePortal" ] || git clone git@github.com:miltom8557gmail/starter-workflows.git AkamePortal
cd AkamePortal
mkdir -p "/data/data/com.termux/files/usr/lib/android-sdk/licenses"
printf "8933bad161af4178b1185d1a37fbf41ea5269c55\nd56f1187405551ad0638e53f353b934b9d36e783" > "/data/data/com.termux/files/usr/lib/android-sdk/licenses/android-sdk-license"
chmod +x *.sh
termux-wake-lock
python3 akame_omni_05-04-2026_15h.py --realtime
