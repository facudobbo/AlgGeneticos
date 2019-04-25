# dos a la treinta menos 1 (2^30)-1
#Poblacion inicial 10 cromosomas
# 30 genes en el
# Crossover: 0.75
# Mutacion: 0.05
# Funcion
from random import *
import numpy as np
from prettytable import PrettyTable

funObj = []
fit = []
coef = (2 ** 30) - 1
cromosoma=[]
decimales=[]



def aleatorioC(a,b,c):
    cromo=[]
    for i in range(0,c):
        r=randint(a,b)
        cromo.append(r)
    return cromo

def PoblacionInicial():
    poblacion=[]
    for i in range (0,10) :
        a=aleatorioC(0,1,30)
        poblacion.append(a)
    return poblacion


def binadec ():
    for i in Poblacion:
        strOfNumbers=''.join(str(n) for n in i)
        crom=(int(strOfNumbers))
        cromosoma.append(crom)
        dec=(int(strOfNumbers,2))
        decimales.append(dec)





def cuentas ():
    sum = 0
    max = 0
    min = 99999999
    for j in range(10):
        fobj =((decimales[j]/coef)**2)
        funObj.append(fobj)
        if max<fobj:
            max=fobj
        if min>fobj:
            min=fobj
        sum += fobj
    prom = sum/10
    sumf = 0
    for j in range (10):
        f = funObj[j] / sum
        fit.append(f)
        sumf += f


    for i in range(10):
        tabla.add_row([cromosoma[i], decimales[i], funObj[i], fit[i]])
    print(tabla)
    print("Suma Funcion Objetivo: " , sum)
    print("Suma Fit: ", sumf)
    print("Maximo: " , max)
    print("Minimo: " , min)
    print("Promedio: ", prom)


tabla = PrettyTable()
tabla.field_names=['Cromosoma','Decimal', 'Funcion Objetivo', 'Fit']
Poblacion=PoblacionInicial()
binadec()
cuentas()

