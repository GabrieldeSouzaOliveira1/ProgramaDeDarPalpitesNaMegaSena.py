import time
import random

quantidade = int(input("Quantos jogos você quer que eu sorteie? "))
jogos = []

for _ in range(quantidade):
    mega = random.sample(range(1, 61), 6)  # Gera 6 números únicos entre 1 e 60
    mega.sort()  # Ordena os números para facilitar a visualização
    jogos.append(mega)
    print(f"Jogo {_ + 1}: {mega}")
    time.sleep(1)

# Simulação da Mega-Sena
megasena = [27, 30, 37, 40, 46, 47]

# Verifica se algum jogo ganhou
if megasena in jogos:
    print("\nParabéns! Um dos jogos acertou os números da Mega-Sena!")
else:
    print("\nNenhum jogo ganhou desta vez.")

print("\nNúmeros da Mega-Sena:", megasena)
