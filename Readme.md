# 🛡️ Firewall Log Generator & Security Analyzer

Este repositório contém um ecossistema em Python desenvolvido para simular e analisar tráfego de rede em cenários de Cibersegurança. O projeto foi criado para exercitar a lógica de programação aplicada à **Defesa Cibernética (Blue Team)**.

## 📝 Descrição do Projeto

O projeto é dividido em duas frentes principais:
1. **Gerador de Massa de Dados:** Um script que utiliza funções modulares para gerar logs estruturados em JSON, simulando conexões de firewall com IPs aleatórios, portas de serviços comuns e ações de segurança (ALLOW/BLOCK).
2. **Analisador de Incidentes:** Um script de monitoramento em tempo real que filtra eventos críticos, como tentativas de invasão via SSH (Porta 22).



## 🛠️ Tecnologias Utilizadas

* **Python 3.x**
* **Bibliotecas nativas:** `json`, `random`, `datetime`, `time`.

## 🚀 Funcionalidades

- [x] **Geração de IPs Dinâmicos:** Função customizada para criar endereços IPv4 aleatórios.
- [x] **Simulação de Serviços:** Monitoramento de portas padrão como 22 (SSH), 80 (HTTP), 443 (HTTPS), entre outras.
- [x] **Filtros Avançados:** Lógica booleana para isolar comportamentos suspeitos no tráfego.
- [x] **Leitura Real-time:** Sistema de leitura contínua de arquivos para monitoramento de eventos conforme eles ocorrem.

## Desenvolvido por Igor Pires
- **LinkeDin** https://www.linkedin.com/in/igor-aparecido-marque-pires/

## 📊 Exemplo de Log Gerado

```json
{"timestamp": "19:05:12", "ip": "172.16.254.1", "porta": 22, "acao": "BLOCK"}