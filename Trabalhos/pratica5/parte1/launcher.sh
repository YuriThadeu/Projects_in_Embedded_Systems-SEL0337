#!/bin/bash

# Pausa de 10s para garantir que a Interface Gráfica carregou totalmente
# Isso evita o erro de "Display not found"
echo "Aguardando sistema grafico..."
sleep 10

# --- FASE 1: Reconhecimento Facial ---
cd /home/embarcados/embarcados/pratica5/git/Projects_in_Embedded_Systems-SEL0337/Trabalhos/pratica5/parte3/

echo "Tentando iniciar Reconhecimento Facial..."
python3 pvc_rasp.py

# Captura o resultado: Se fechou com erro, avisa no log
if [ $? -ne 0 ]; then
    echo "ERRO CRITICO: O programa de reconhecimento fechou com erro!"
    echo "Verifique se a câmera está conectada ou se há erro de código."
    # Pausa para você conseguir ler o erro se estiver testando no terminal
    sleep 5
else
    echo "Reconhecimento finalizado com sucesso."
fi

# --- FASE 2: Blink ---
cd /home/embarcados/embarcados/pratica5/git/Projects_in_Embedded_Systems-SEL0337/Trabalhos/pratica5/parte1/

echo "Iniciando Blink..."
python3 blink_final.py