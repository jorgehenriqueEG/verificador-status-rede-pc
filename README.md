# verificador-status-rede-pc

## Descrição do Problema

Avaliar o status de um computador na rede com base em IP, latência e pacotes perdidos para determinar a conectividade.

## Requisitos

* Receber dados de um PC (IP, latência, pacotes perdidos)
* Classificar o status em: Online, Instável ou Offline
* Latência acima de 100ms indica Instável
* Pacotes perdidos acima de 10% indica Instável
* Pacotes perdidos acima de 80% indica Offline

## Exemplo de Uso

Entrada: {"ip": "192.168.1.10", "latencia": 150, "perda": 5}
Saída: Status: Instável