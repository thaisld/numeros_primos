import threading

# Função que verifica se um número é primo
def eh_primo(numero):
    if numero <= 1:
        return False
    if numero == 2:
        return True
    if numero % 2 == 0:
        return False
    for i in range(3, int(numero**0.5) + 1, 2):
        if numero % i == 0:
            return False
    return True

# Função que encontra primos em um intervalo
def encontrar_primos(inicio, fim, resultado, lock):
    primos = []
    for numero in range(inicio, fim):
        if eh_primo(numero):
            primos.append(numero)
    # Usando o lock para proteger o acesso à lista de resultado
    with lock:
        resultado.extend(primos)

def main():
    # Intervalo para busca de primos
    intervalo_inicial = 1
    intervalo_final = 10000

    # Número de threads
    num_threads = 4
    tamanho_intervalo = (intervalo_final - intervalo_inicial) // num_threads

    # Lista para armazenar os números primos encontrados
    resultado = []

    # Lock para sincronizar o acesso à lista de resultados
    lock = threading.Lock()

    # Lista de threads
    threads = []

    # Criando e iniciando threads
    for i in range(num_threads):
        inicio = intervalo_inicial + i * tamanho_intervalo
        fim = inicio + tamanho_intervalo if i != num_threads - 1 else intervalo_final
        thread = threading.Thread(target=encontrar_primos, args=(inicio, fim, resultado, lock))
        threads.append(thread)
        thread.start()

    # Aguardando todas as threads terminarem
    for thread in threads:
        thread.join()

    # Exibindo os números primos encontrados
    print(f"Números primos encontrados no intervalo de {intervalo_inicial} a {intervalo_final}:")
    print(resultado)

if __name__ == "__main__":
    main()
