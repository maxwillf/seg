import cv2
import sys
import numpy as np

def changeLastBit(byte, bitChar):
    if bitChar == '0':
        return byte & 0b11111110
    else:
        return byte | 0b00000001

def getLastBit(byte):
    return '{0:08b}'.format(byte)[7]

def getLetterAsByte(char):
    return '{0:08b}'.format(ord(char))

def cipher():
  src = sys.argv[1]
  message = sys.argv[3]
  message += '\x03'

  image = cv2.imread(src)

  old_shape = image.shape

  image = image.reshape(np.prod(image.shape))

  pixelIndex = 0

  for letter in message:
    for bit in getLetterAsByte(letter)[::-1]:
      image[pixelIndex] = changeLastBit(image[pixelIndex],bit)
      pixelIndex += 1
    pixelIndex += 1
  image = image.reshape(old_shape)

  outputPath = sys.argv[2]
  status = cv2.imwrite(outputPath, image)
  print("Succesfully hidden message: ", status)


def decipher():
  image = cv2.imread("./out.bmp")
  pixelIndex = 0
  imageSize = np.prod(image.shape)
  image = image.reshape(imageSize)
  decodedWord = ""
  readByte = ""

  # while readByte isn't End Of Text Character
  while(pixelIndex < imageSize):
    #readByte = getLastBit(image[pixelIndex]) + readByte
    LastBit = getLastBit(image[pixelIndex])

    readByte = LastBit + readByte
    pixelIndex += 1

    if(len(readByte) == 8):
      if int(readByte,2) == 3:
          print("Message found in file:", decodedWord)
          exit(0)
      decodedWord += chr(int(readByte,2))
      readByte = "" 
      # pular o nono byte
      pixelIndex += 1
  print("No message was found")

if __name__ == "__main__":
  if "-d" in sys.argv:
    decipher()
  else:
    cipher()
