import sys
import math
import struct
import os.path

###################################################
# Funções de suporte - todas retiradas da internet!
###################################################


def shift_list(array, s):
    """Shifts the elements of a list to the left or right.

    Args:
        array - the list to shift
        s - the amount to shift the list ('+': left-shift, '-': right-shift)

    Returns:
        shifted_array - the shifted list
    """
    # calculate actual shift amount (e.g., 11 --> 1 if length of the array is 5)
    s %= len(array)

    # uncomment this line to reverse the shift direction
    # s *= -1

    # shift array with list slicing
    shifted_array = array[s:] + array[:s]

    return shifted_array

# funcao para usar inteiros negativos para hexadecimal
# https://stackoverflow.com/a/7823051

def tohex(val, nbits):
  return hex((val + (1 << nbits)) % (1 << nbits))


# https://stackoverflow.com/a/23624284

def float_to_hex(f):
    return hex(struct.unpack('<I', struct.pack('<f', f))[0])


##################
# Começo do script
##################


num = int(input("Qual é o teu numero de aluno?  "))

if (not isinstance(num, int)):
    print ("Tens que inserir o teu número! \n")
    quit()

print ("As tuas variáveis são:")
print ("NUM: ", num)
var1 = num % 1000
print ("VAR1: ", var1)
var2 = int(num/1000)
print ("VAR2: ", var2)
var3 = var1 + var2
print ("VAR3: ", var3)


#############
# Exercício 1
#############


numBin = str(bin(num))[2:]
print ("Exercício 1")
print ("a)" , numBin[-16:])
var1a = numBin[-16:]

numHexa = hex(num)[2:]  #devolve em str

numBin20 = '{:020d}'.format(int(numBin))

newBin = list(numBin20)

for i in range(0,16):
    newBin[i] = '0'

newBin20 = int(''.join(newBin), 2)  #returns int

print("b)", '{:0>5}'.format(hex(newBin20)[2:]))
var1b = '{:0>5}'.format(hex(newBin20)[2:])

print("c)", bin(var3)[-8:]) #returns str
var1c = bin(var3)[-8:]

print("d)", hex(var3)[-2:]) #returns str
var1d = hex(var3)[-2:]

#############
# Exercício 2
#############

print ("Exercício 2")

# RESPOSTAS SEMPRE COM 16bits, ou seja, 4 digitos em hexadecimal
# var3 ja e hexadecimal.

var3Hexa = hex(var3)[2:] #return str
var3Bin = bin(var3)[2:] #returns str

var3ToDec = int(str(var3), 16)
test =  var3ToDec >> 8
print ("a)", '{:0>4}'.format(hex(test)[2:]))
var2a = '{:0>4}'.format(hex(test)[2:])

test = var3ToDec >> 2
print ("b)", '{:0>4}'.format(hex(test)[2:]))
var2b = '{:0>4}'.format(hex(test)[2:])

test = var3ToDec << 5
test1 = hex(test)[2:]    # without the 0x
print ("c)", '{:0>4}'.format(hex(test)[2:]) + " --> " + test1[-4:])
var2c = test1[-4:]

aux = list('{:0>16}'.format(bin(var3ToDec)[2:]))
aux = shift_list(aux, +8)
aux = int(''.join(aux), 2)

print ("d)", '{:0>4}'.format(hex(aux)[2:]))
var2d = '{:0>4}'.format(hex(aux)[2:])

var3BinInt = int(var3Bin)
valueToSum = int('82', 16)
newValue = '{:0>4}'.format(hex(var3ToDec + valueToSum)[2:])

print ("e)", newValue)
var2e = newValue

valueToSum = 82
newValue = '{:0>4}'.format(hex(var3ToDec - valueToSum)[2:])
print ("f)", newValue)
var2f = newValue

print ("g)", tohex(-var3ToDec, 16)[2:])
var2g = tohex(-var3ToDec, 16)[2:]

print ("h)", tohex(-var3ToDec, 32)[2:])
var2h = tohex(-var3ToDec, 32)[2:]

print ("i)", '{:0>4}'.format(hex(int(var3ToDec/4))[2:]))
var2i = '{:0>4}'.format(hex(int(var3ToDec/4))[2:])


#############
# Exercício 3
#############


print ("Exercício 3")

var3Hex = '{:0>16}'.format(hex(var3)[2:])
var1Hex = '{:0>16}'.format(hex(var1)[2:])

A = var3Hex[-2:]    # 8 less significant bits of var3 in hexa, meaning, the first two characters
B = var1Hex[-2:]    # 8 less significant bits of var1 in hexa, meaning, the first two characters

C = A + B + '0000'

print ("a)", C)
var3a = C

# https://stackoverflow.com/a/1592362
test = struct.unpack('!f', bytes.fromhex(C))[0]

print ("b)", format(test, '.2g') + " <-- Lembra-te de contar so os algarismos antes do e")
lel = str(format(test, '.2g'))
print(lel)
var3b = "" + lel[0] + lel[2]


aux = 1.05*(2**(-var2))
auxHex = float_to_hex(aux)[2:]
auxBin = '{:0>32}'.format(bin(int(auxHex,16))[2:])
exp = auxBin[1:9]

print("c)", hex(int(exp, 2))[2:])
var3c = hex(int(exp, 2))[2:]


####################################
# Criação do ficheiro para submissao
####################################

print ("")
raite = str(input("Queres criar um ficheiro para submeter? (y \ n)  " ))

if (not isinstance(raite, str) or not (raite == 'y')):
    print ("")
    print("Ficheiro nao foi criado. O programa terminou.")
    print ("")

    quit()
elif (raite == 'y'):
    print("")
    print("Vou guardar um ficheiro para submissao no Fénix ...")
    print ("")

    filename = "" + str(num) + "-TPC2.txt"
    print(filename)
    file = open(filename, "+w")
    textToWrite=["" + str(num) + "; " + str(var1a) + "; " + str(var1b) + "; " + str(var1c) + "; " + str(var1d) + "; " + str(var2a) + "; " + str(var2b) + "; " + str(var2c) + "; " + str(var2d) + "; " + str(var2e) + "; " + str(var2f) + "; " + str(var2g) + "; " + str(var2h) + "; " + str(var2i) + "; " + str(var3a) + "; " + str(var3b) + "; " + str(var3c) + "; \n"]

    file.write("".join(textToWrite))

    print ("")
    print ("Ficheiro foi escrito com sucesso no PATH actual.")
    print ("")
    print ("Não te esqueças de verificar as respostas antes de submeter, posso ter um bug :)")
    print ("")
    print ("O programa terminou.")
    print ("")
