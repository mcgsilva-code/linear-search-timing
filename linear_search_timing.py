import time
import matplotlib.pyplot as plt

def linear_search(arr, target):
    """Procura o elemento target na lista arr e retorna o índice ou -1"""
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Tamanhos diferentes de listas
sizes = [10, 100, 1000, 5000, 10000, 20000, 50000, 100000]
times = []

for size in sizes:
    arr = list(range(size))  # cria lista de 0 até size-1
    target = size - 1        # procura o último elemento (pior caso)

    start = time.time()      # início do tempo
    linear_search(arr, target)
    end = time.time()        # fim do tempo

    times.append(end - start)

# Gerar gráfico
plt.plot(sizes, times, marker='o', color='red')
plt.xlabel("List Size (n)")
plt.ylabel("Execution Time (seconds)")
plt.title("Linear Search Time Complexity (O(n))")
plt.grid(True)
plt.tight_layout()
plt.show()
