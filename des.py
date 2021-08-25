# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 20:03:48 2020

@author: mohamed
"""


#Initial permut matrix for the datas
PI = [58, 50, 42, 34, 26, 18, 10, 2,
      60, 52, 44, 36, 28, 20, 12, 4,
      62, 54, 46, 38, 30, 22, 14, 6,
      64, 56, 48, 40, 32, 24, 16, 8,
      57, 49, 41, 33, 25, 17, 9, 1,
      59, 51, 43, 35, 27, 19, 11, 3,
      61, 53, 45, 37, 29, 21, 13, 5,
      63, 55, 47, 39, 31, 23, 15, 7]

#Initial permut made on the key
CP_1 = [57, 49, 41, 33, 25, 17, 9,
        1, 58, 50, 42, 34, 26, 18,
        10, 2, 59, 51, 43, 35, 27,
        19, 11, 3, 60, 52, 44, 36,
        63, 55, 47, 39, 31, 23, 15,
        7, 62, 54, 46, 38, 30, 22,
        14, 6, 61, 53, 45, 37, 29,
        21, 13, 5, 28, 20, 12, 4]

#Permut applied on shifted key to get Ki+1
CP_2 = [14, 17, 11, 24, 1, 5, 3, 28,
        15, 6, 21, 10, 23, 19, 12, 4,
        26, 8, 16, 7, 27, 20, 13, 2,
        41, 52, 31, 37, 47, 55, 30, 40,
        51, 45, 33, 48, 44, 49, 39, 56,
        34, 53, 46, 42, 50, 36, 29, 32]

#Expand matrix to get a 48bits matrix of datas to apply the xor with Ki
E = [32, 1, 2, 3, 4, 5,
     4, 5, 6, 7, 8, 9,
     8, 9, 10, 11, 12, 13,
     12, 13, 14, 15, 16, 17,
     16, 17, 18, 19, 20, 21,
     20, 21, 22, 23, 24, 25,
     24, 25, 26, 27, 28, 29,
     28, 29, 30, 31, 32, 1]

#SBOX
s_box = [
    ['0010','1100','0100','0001','0111','1010','1011','0110','1000','0101','0011','1111','1101','0000','1110','1001'],
    ['1110','1011','0010','1100','0100','0111','1101','0001','0101','0000','1111','1010','0011','1001','1000','0110'],
    ['0100','0010','0001','1011','1010','1101','0111','1000','1111','1001','1100','0101','0110','0011','0000','1110'],
    ['1011','1000','1100','0111','0001','1110','0010','1101','0110','1111','0000','1001','1010','0100','0101','0011']
    ]
#Permut made after each SBox substitution for each round
P = [16, 7, 20, 21, 29, 12, 28, 17,
     1, 15, 23, 26, 5, 18, 31, 10,
     2, 8, 24, 14, 32, 27, 3, 9,
     19, 13, 30, 6, 22, 11, 4, 25]

#Final permut for datas after the 16 rounds
PI_1 = [40, 8, 48, 16, 56, 24, 64, 32,
        39, 7, 47, 15, 55, 23, 63, 31,
        38, 6, 46, 14, 54, 22, 62, 30,
        37, 5, 45, 13, 53, 21, 61, 29,
        36, 4, 44, 12, 52, 20, 60, 28,
        35, 3, 43, 11, 51, 19, 59, 27,
        34, 2, 42, 10, 50, 18, 58, 26,
        33, 1, 41, 9, 49, 17, 57, 25]

#Matrix that determine the shift for each round of keys
SHIFT = [1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]

def shiftStringLeft(line,weight):#shifts a weight number of characters to the left of the string
    tempLine = ''
    cursor = weight
    for i in range(len(line)): # 1 0 1 0 0 --> shift 1 --> 0 1 0 0 1
        if(cursor < len(line)):
            tempLine = tempLine + line[cursor]
            cursor = cursor + 1;
    if(weight == 1):
                tempLine = tempLine+line[0]
    if(weight == 2):
                tempLine = tempLine+line[0]
                tempLine = tempLine+line[1]
    return tempLine;

def textToBinary(text):#to be replaced 
    binaryCode = ''
    for element in text:
        binaryCode = binaryCode + bin(ord(element)).strip('0b')
    return binaryCode

#11100001100110010101010111111010101011001100111100011110
#000110110000001011101111111111000111000001110010
#1010101100110011110001111010
#111000011001100101010101111
def binaryToText(code):
    plainText = ''
    
        
    return code
def permutationUsingMatrix(code,matrix):#permuts the codes using a given matrix
    permutedCode = ''
    for element in matrix:
        permutedCode = permutedCode + code[element-1]
    return permutedCode

def generateKeys(key): #generates keys to be used in the feistel function
    defaultKey = key #this is the key to be used in the first iteraction
    generatedKeys = []
    key_size = len(key)
    if(key_size == 64):#check for the key is valide in case it had the extra 8 bits 
        if(key[0]^key[1]^key[2]^key[3]^key[4]^key[5]^key[6] == key[7]):
          defaultKey = key[7:]
        else:
          print("error in given key")
          return [];
    #this is where the loop goes 
    for i in range(15):
        leftKey = defaultKey[:28]
        #print('left key is : ' + leftKey)
        rightKey = defaultKey[28:]
        #print('right key is : ' + rightKey)
        #shift left the characters based on the shifting matrix SHIFT
        leftkey = shiftStringLeft(leftKey,SHIFT[i])
        #print('left key is : ' + leftKey)
        rightKey = shiftStringLeft(rightKey,SHIFT[i])
       # print('right key is : ' + rightKey)
        #tempKey = permutationUsingMatrix(leftKey + rightKey,CP_2)#bind the two parts of the key and undergo the permutation to go from 56 to 48 bits
        #print(tempKey)
        defaultKey = leftKey+rightKey 
        generatedKeys.append(permutationUsingMatrix(defaultKey,CP_2)) #keys down from 56 bits to 48 throught permutation CP-2
    return  generatedKeys;
#000110110000001011101111000011100001011111110101

def xor(x,y):#do the XOR operation on two elements x and y 
     xorCode = ''
     for element in range(len(x)) :
        xorCode = xorCode + str((int(x[element])^int(y[element])))
     return xorCode
 
def extendCode(code):
     extendedCode = permutationUsingMatrix(code,E)#we can simply use the permutation function and get the same results
     return extendedCode
 
def reductionWithSbox(code):
    rows = ['00','01','10','11']
    columns = ['0000','0001','0010','0011','0100','0101','0110','0111','1000','1001','1010','1011','1100','1101','1110','1111']
    rowDigits = code[0] + code[5]
    columnsDigits = code[1:5]
    return s_box[rows.index(rowDigits)][columns.index(columnsDigits)]

def reduceCodeAfterXor(code):
    reducedCode = ''
    for element in [code[i:i+6] for i in range(0, len(code), 6)]:#↕split the code to 8 msgs of 6 bits
        reducedCode = reducedCode + reductionWithSbox(element)
    return reducedCode

def feister(msg,usedKey):
    IPmsg = permutationUsingMatrix(msg,PI) #initial permuation of the code
    leftMsg = IPmsg[:32] #getting the L0 and R0
    rightMsg = IPmsg[32:]
    leftMsgI = leftMsg
    rightMsgI = rightMsg
    key = generateKeys(usedKey)
    for element in range(16):
        leftMsgI = rightMsgI
        rightMsgI = reduceCodeAfterXor(xor(leftMsgI ,xor(extendCode(rightMsgI),key[element])))
    finalMsg = permutationUsingMatrix(leftMsgI + rightMsgI,PI_1)
    return finalMsg

def des(msg,key):
    binaryMsg = textToBinary(msg)
    return feister(binaryMsg,key)