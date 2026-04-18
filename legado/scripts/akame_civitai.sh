#!/data/data/com.termux/files/usr/bin/bash
MODEL_ID=$1
TOKEN="748342468305886d9428599426f43e4b"
echo "🧬 [AKAME]: Extraindo modelo $MODEL_ID do Civitai..."
curl -L -H "Authorization: Bearer $TOKEN" "https://civitai.com/api/download/models/$MODEL_ID" --output "~/Akame_Omni_20260405/model_$MODEL_ID.safetensors"
echo "✅ [STATUS]: Modelo assimilado localmente."
