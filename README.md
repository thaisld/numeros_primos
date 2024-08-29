# Encontrar Números Primos com Threads em Python

## Descrição
Este projeto implementa um programa em Python que utiliza múltiplas threads para encontrar números primos dentro de um intervalo definido. O intervalo é dividido em partes iguais, e cada parte é processada em paralelo por uma thread diferente.

## Como Funciona
1. *Intervalo de Busca*: O programa procura por números primos no intervalo de 1 a 10.000.
2. *Divisão do Intervalo*: O intervalo é dividido em 4 partes iguais, e cada parte é atribuída a uma thread.
3. *Execução em Paralelo*: Cada thread encontra os números primos no subintervalo que lhe foi atribuído.
4. *Agregação dos Resultados*: Após a conclusão de todas as threads, os números primos encontrados são exibidos.

## Requisitos
- Python 3.11

## Como Executar
1. Clone este repositório:
   ```bash
   git clone <(https://github.com/thaisld/numeros_primos.git)>
