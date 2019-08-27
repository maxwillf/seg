import cv2
import sys
import numpy as np
import argparse

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
	message = sys.argv[2]
	message += '\x03'

	print(getLetterAsByte(message[-1]))

	bitsNeededForMessage = len(message) * 8
	image = cv2.imread(src)
	imageSize = np.prod(image.shape)

	old_shape = image.shape

	image = image.reshape(np.prod(image.shape))

	pixelIndex = 0

	amountOfLines = old_shape[0]
	sizeOfLine = old_shape[1]

	for letters in message:
	    for bit in getLetterAsByte(letters)[::-1]:
		image[pixelIndex] = changeLastBit(image[pixelIndex],bit)
		pixelIndex += 1
	    pixelIndex += 1


	status = cv2.imwrite("./out.bmp", image.reshape(old_shape))
	print("Succesfully hidden message: ", status)


def decipher():
	image = cv2.imread("./out.bmp")

	pixelIndex = 0

	image = image.reshape(np.prod(image.shape))

	decodedWord = ""
	readByte = ""

	for letters in message:
	    for bit in getLetterAsByte(letters):

		readByte = getLastBit(image[pixelIndex]) + readByte

		if bit == 3:
		    print("Message found in file:", decodedWord)
		    break

		readByte = getLastBit(image[pixelIndex]) + readByte

		if(decodedWord == message):
		    print("Message found in file:", decodedWord)
		    break
		pixelIndex += 1

	    # pular o nono byte
	    pixelIndex += 1


if "-d" in sys.argv:
	decipher()
else:
	cipher()
