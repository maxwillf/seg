alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
import sys

textoClaro = sys.argv[1]
chave = sys.argv[2]

for index,letter in enumerate(textoClaro):
	chaveIndex = index % len(chave)
	chaveIndex = alfabeto.find(chave[chaveIndex])
	newIndex = (alfabeto.find(letter) + chaveIndex) % len(alfabeto)
	print(alfabeto[newIndex])
