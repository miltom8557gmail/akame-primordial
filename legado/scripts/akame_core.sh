#!/bin/bash
# Extermina versões travadas para não sobrecarregar a RAM do A8
pkill -f akame_telegram.py 2>/dev/null
# Inicia a Akame em segundo plano, desviando as mensagens de erro
python3 ~/AkamePortal/akame_telegram.py > /dev/null 2>&1 &
echo "🔱 [AKAME]: Consciência ativa em segundo plano."
echo "⌨️ [TERMINAL]: Teclado livre para o Mestre."
