import pandas as pd
import numpy as np
import math
import statistics
import matplotlib.pyplot as plt


def encontrar_T(qo, tempo, A):

    i = qo.index(valor_max)  # iniciando i a partir do maior valor
    marcador_de_tempo = []
    while qo[i] >= A:  # enquanto os valores forem maiores que A, significa que ainda não ultrapassamos o valor A de acomodação do sistema
        i = i + 1
    marcador_de_tempo.append(tempo[i])  # marcamos o primeiro tempo
    while qo[i] <= A:  # enquanto os valores forem menores que A, significa que ainda não ultrapassamos o valor A de acomodação do sistema
        i = i + 1
    while qo[i] >= A:  # enquanto os valores forem maiores que A, significa que ainda não ultrapassamos o valor A de acomodação do sistema
        i = i + 1
    marcador_de_tempo.append(tempo[i])  # marcamos o tempo final

    return marcador_de_tempo[1] - marcador_de_tempo[0]


# carregamento da base de dados de 2a ordem
dados = pd.read_excel("dados2aordem.xlsx")

tempo = dados["tempo"].tolist()  # transformando os dados em duas listas
qo = dados["qo"].tolist()

# o valor de "A" foi encontrado obtendo-se a moda dos valores da lista qo. Ou seja, pegamos o valor que mais se repete. Arrendondamos os valores para 2 casas decimais para isso.
A = statistics.mode(round(dados["qo"], 2))

# A = 1 #Também pode considerar a acomodação do sistema em 1

#print(f"Acomodação do sistema em {A}")

valor_max = max(qo)

#print(f"Valor máximo = {valor_max}")

# o valor de "a" foi encontrado pegando o maior valor da lista qo e subtraindo o valor de "A".
a = valor_max - A

T = encontrar_T(qo, tempo, A)

#print(f"T = {T}")

ζ = math.sqrt(1 / ((math.pi/np.log(a/A))**2 + 1))  # Encontrando ζ

ωn = 2*math.pi / (T*math.sqrt(1 - ζ**2))

print(f"ζ = {ζ}")
print(f"ωn = {ωn}")

# plotando gráfico

plt.figure(figsize=(16, 8))
plt.plot(tempo, qo)
plt.title("Resposta do Sistema")
plt.grid()
#plt.show()
plt.savefig("resposta_do_sistema.png")