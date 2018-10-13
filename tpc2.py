import sys
import math
import binascii


campos = [ "NUM", "1.a", "1.b", "1.c", "1.d", "2.a", "2.b", "2.c", "2.d", "2.e", "2.f", "2.g", "2.h", "2.i", "3.a", "3.b", "3.c" ]

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


numBin = str(bin(num))[2:]

print ("Exercício 1")
print ("a)" , numBin[-16:])


numHexa = hex(num)[2:]  #devolve em str

numBin20 = '{:020d}'.format(int(numBin))

newBin = list(numBin20);
for i in range(0,16):
    newBin[i] = '0'

# print(''.join(newBin))
newBin20 = int(''.join(newBin), 2)  #returns int


print("b) "'{:0>5}'.format(hex(newBin20)[2:]))


print("c)", bin(var3)[-8:]) #returns str

print("d)", hex(var3)[-2:]) #returns str

print ("Exercício 2")
