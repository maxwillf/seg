import sys

alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
textoClaro = sys.argv[1]
chave = sys.argv[2]

mensagemDecifrada = ""
for index,letter in enumerate(textoClaro):
    chaveIndex = index % len(chave)
    letterIndex = alfabeto.find(letter)
    print(letterIndex)
    if letterIndex == -1:
       mensagemDecifrada += letter
       continue 
    print(letterIndex,alfabeto[letterIndex])
    newChaveIndex = alfabeto.find(chave[chaveIndex])
    newIndex = (letterIndex + newChaveIndex) % len(alfabeto)
    mensagemDecifrada += alfabeto[newIndex]
print(mensagemDecifrada)
