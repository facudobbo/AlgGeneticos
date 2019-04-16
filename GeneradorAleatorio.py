
# dos a la treinta menos 1 (2^30)-1
#Poblacion inicial 10 cromosomas
# 30 genes en el
# Crossover: 0.75
# Mutacion: 0.05
# Funcion
from random import *

hola=0
def aleatorioC(a,b,c):
    cromosoma=[]
    for i in range(0,c):
        r=randint(a,b)
        cromosoma.append(r)
    return cromosoma

def PoblacionInicial():
    poblacion=[]
    for i in range (0,10) :
        a=aleatorioC(0,1,30)
        poblacion.append(a)
    return poblacion

Poblacion=PoblacionInicial()
def binadec ():
    for cromosoma in Poblacion:
        print(cromosoma)
        strOfNumbers=''.join(str(n) for n in cromosoma)
        print (int(strOfNumbers))
        print(int(strOfNumbers,2))



binadec()






















