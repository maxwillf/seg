import sys

alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
textoPath = sys.argv[1]
textoClaro = open(textoPath,"r").read()
chave = sys.argv[2]

mensagemDecifrada = ""
chaveIndex = 0
for index,letter in enumerate(textoClaro):
    
    if not letter.isalpha() or letter.upper() not in alfabeto:
       mensagemDecifrada += letter
       continue 
    
    if letter.islower():
        letterIndex = alfabeto.find(letter.upper())
    else:
        letterIndex = alfabeto.find(letter)

    newChaveIndex = alfabeto.find(chave[chaveIndex])
    newIndex = (letterIndex - newChaveIndex) % len(alfabeto)
    
    if letter.islower():
        mensagemDecifrada += alfabeto[newIndex].lower()
    else:
        mensagemDecifrada += alfabeto[newIndex]

    chaveIndex += 1
    chaveIndex = chaveIndex % len(chave)

print(mensagemDecifrada)
