#!/bin/bash
# Limpa qualquer resíduo de imagem ou vídeo temporário do A8
echo "🧹 [VITRINE]: Limpando cache de exibição tática..."
rm -rf app/src/main/res/drawable/temp_*
rm -rf app/src/main/assets/stream_*
echo "✅ [STATUS]: O celular continua limpo. Tudo reside na Nuvem."
