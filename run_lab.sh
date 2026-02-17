#!/bin/bash

echo "Inicializing the log generator"

python3 Gerador_Logs_CyberSec.py &
GENERATOR_PID=$!

echo "Generator started! (PID: $GENERATOR_PID). Waiting Logs..."
sleep 2

kill $GENERATOR_PID
echo "Lab finished"
