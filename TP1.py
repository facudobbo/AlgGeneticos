# dos a la treinta menos 1 (2^30)-1
#Poblacion inicial 10 cromosomas
# 30 genes en el
# Crossover: 0.75
# Mutacion: 0.05
# Funcion
from random import *
import numpy as np
from prettytable import PrettyTable

pretabla= np.zeros((10,4))
tabla = PrettyTable()
tabla.field_names =["Cromosoma", "Decimal" , "F.obj", "Fit"]


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


def binadec ():
    j=0
    for cromosoma in Poblacion:
        print(cromosoma)
        strOfNumbers=''.join(str(n) for n in cromosoma)
        crom=(int(strOfNumbers))
        pretabla[j][0]=crom
        dec=(int(strOfNumbers,2))
        pretabla[j][1]=dec
        j+=1




def cuentas ():
    sum=0
    for j in range(10):
        dec = int(pretabla[j][1])
        crom = pretabla[j][0]
        fobj =((dec/((2**30)-1))**2)
        pretabla[j][2] = fobj

    for x in range (9):
        sum=(sum+(pretabla[x][2]+pretabla[x+1][2]))
    for i in range (10):
        fit = (pretabla[i][2]/sum)
        pretabla[i][3]=fit
    for i in range (10):
        tabla.add_row([pretabla[i][0], pretabla[i][1],pretabla[i][2], pretabla[i][3]])


    print(tabla)

Poblacion=PoblacionInicial()
binadec()
cuentas()
