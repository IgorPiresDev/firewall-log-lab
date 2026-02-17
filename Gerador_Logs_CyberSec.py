import json
import random
from datetime import datetime, timedelta

def ip_random():
    parte1 = random.randint(0, 255)
    parte2 = random.randint(0, 255)
    parte3 = random.randint(0, 255)
    parte4 = random.randint(0, 255)

    iprandom= f'{parte1}.{parte2}.{parte3}.{parte4}'
    return iprandom


acao = ['block','allow']
porta_codes = [80, 403, 22, 3389, 21, 445, 25, 110] # Mais 200 para parecer real

with open("logs_aleatorios.json", "w") as f:
    for i in range(100):

        number_ip = ip_random()
        data_hora = (datetime.now() - timedelta(minutes=i)).strftime("%Y-%m-%d %H:%M:%S")
        log = {
            "timestamp": data_hora,
            "ip": number_ip,
            "porta": random.choice(porta_codes),
            "acao": random.choice(acao)
        }
        f.write(json.dumps(log) + "\n")

print("Arquivo 'logs_aleatorios.json' gerado com 100 linhas!")