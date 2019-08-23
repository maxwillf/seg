import cv2,sys

def changeLastBit(byte,bitChar):
    if bitChar == '0':
        return byte & 0b11111110
    else:
        return byte | 0b00000001
def getLastBit(byte):
    return '{0:08b}'.format(byte)[7]
def getLetterAsByte(char):
    return '{0:08b}'.format(ord(char))


src = sys.argv[1]
message = sys.argv[2]

bitsNeededForMessage = len(message) * 8
image = cv2.imread(src)
imageSize = len(image) * len(image[0])

print(getLastBit(ord('S')))
line = image[0]

lineIndex = 0
columnIndex = 0
pixelIndex = 0

amountOfLines = len(image)
sizeOfLine = len(line[0])

for letters in message:
    for bit in getLetterAsByte(letters):
        image[lineIndex][columnIndex][pixelIndex] = \
                changeLastBit(image[lineIndex][columnIndex][pixelIndex],bit)

        pixelIndex += 1;
        if pixelIndex >= 3:
            pixelIndex = 0
            columnIndex += 1;
        if columnIndex >= sizeOfLine:
            columnIndex = 0
            lineIndex += 1;

status = cv2.imwrite("./out.bmp",image)
print("Succesfully hidden message: ", status)

image = cv2.imread("./out.bmp")

lineIndex = 0
columnIndex = 0
pixelIndex = 0


messaSize = len(message)
decodedWord = ""
readByte = ""
for letters in message:
    for bit in getLetterAsByte(letters):
        readByte += getLastBit(image[lineIndex][columnIndex][pixelIndex])
        if len(readByte) == 8:
            decodedWord += chr(int(readByte,2))
            readByte = ""
        if(decodedWord == message):
            print("Message found in file: ", decodedWord)
            break

        pixelIndex += 1;
        if pixelIndex >= 3:
            pixelIndex = 0
            columnIndex += 1;
        if columnIndex >= sizeOfLine:
            columnIndex = 0
            lineIndex += 1;
