#!/bin/bash
NOME_BACKUP="Akame_Eterna_$(date +%d-%m-%Y)"
ID_USER="8533891507"
TOKEN="8767431243:AAFVrV-ZKqPr_Qo9bCkcFoNuTsZ4TKlFXpU"

echo "📦 [BACKUP]: Compactando ecossistema..."
zip -r - ~/AkamePortal -x "*.key" "*id_rsa*" "*token*" ".git*" "nexus.log" | split -b 40M - "../${NOME_BACKUP}.zip.part"

for parte in ../${NOME_BACKUP}.zip.part*; do
    echo "📤 Enviando $parte..."
    curl -v -F document=@"$parte" "https://api.telegram.org/bot$TOKEN/sendDocument?chat_id=$ID_USER"
    rm "$parte"
done
echo "✅ [SINCRO]: Backup enviado!"
