#N=50 (Numero de cromosomas de las poblaciones)
#M=200 (ciclos)
#Cromosomas: permutaciones de 23 números naturaes de 1 a 23 donde cada gen es una ciudad.
#Crossover ciclico

import random
from matplotlib import pyplot
from pylab import plot, show
import numpy as np
from prettytable import PrettyTable

distancias=[[0,646,792,933,53,986,985,989,375,834,1127,794,2082,979,1080,1334,1282,1005,749,393,579,939,2373,799],
            [646,0,677,824,698,340,466,907,348,919,1321,669,2281,362,517,809,745,412,293,330,577,401,2618,1047],
            [792,677,0,157,830,814,1131,1534,500,291,1845,13,2819,691,633,742,719,1039,969,498,1136,535,3131,1527],
            [933,824,157,0,968,927,1269,1690,656,263,1999,161,2974,793,703,750,741,1169,1117,654,1293,629,3284,1681],
            [53,698,830,968,0,1038,1029,1005,427,857,1116,833,2064,1030,1132,1385,1333,1053,795,444,602,991,2350,789],
            [986,340,814,927,1038,0,427,1063,659,1098,1548,802,2473,149,330,600,533,283,435,640,834,311,2821,1311],
            [985,466,1131,1269,1029,427,0,676,790,1384,1201,1121,2081,569,756,1023,957,152,235,775,586,713,2435,1019],
            [989,907,1534,1690,1005,1063,676,0,1053,1709,543,1529,1410,1182,1370,1658,1591,824,643,1049,422,1286,1762,479],
            [375,348,500,656,427,659,790,1053,0,658,1345,498,2320,622,707,959,906,757,574,19,642,566,2635,1030],
            [834,919,291,263,857,1098,1384,1709,658,0,1951,305,2914,980,924,1007,992,1306,1200,664,1293,827,3207,1624],
            [1127,1321,1845,1999,1116,1548,1201,543,1345,1951,0,1843,975,1647,1827,2120,2054,1340,1113,1349,745,1721,1300,327],
            [794,669,13,161,833,802,1121,1529,498,305,1843,0,2818,678,620,729,706,1029,961,495,1132,523,3130,1526],
            [2082,2281,2819,2974,2064,2473,2081,1410,2320,2914,975,2818,0,2587,2773,3063,2997,2231,2046,2325,1712,2677,359,1294],
            [979,362,691,793,1030,149,569,1182,622,980,1647,678,2587,0,189,477,410,430,540,602,915,166,2931,1391],
            [1080,517,633,703,1132,330,756,1370,707,924,1827,620,2773,189,0,293,228,612,727,686,1088,141,3116,1562],
            [1334,809,742,750,1385,600,1023,1658,959,1007,2120,729,3063,477,293,0,67,874,1017,942,1382,414,3408,1855],
            [1282,745,719,741,1333,533,957,1591,906,992,2054,706,2997,410,228,67,0,808,950,889,1316,353,3341,1790],
            [1005,412,1039,1169,1053,283,152,824,757,1306,1340,1029,2231,430,612,874,808,0,284,740,686,583,2585,1141],
            [749,293,969,1117,795,435,235,643,574,1200,1113,961,2046,540,727,1017,950,284,0,560,412,643,2392,882],
            [393,330,498,654,444,640,775,1049,19,664,1349,495,2325,602,689,942,889,740,560,0,641,547,2641,1035],
            [579,577,1136,1293,602,834,586,422,642,1293,745,1132,1712,915,1088,1382,1316,686,412,641,0,977,2044,477],
            [939,401,535,629,991,311,713,1286,566,827,1721,523,2677,166,141,414,353,583,643,547,977,0,3016,1446],
            [2373,2618,3131,3284,2350,2821,2435,1762,2635,3207,1300,3130,359,2931,3116,3408,3341,2585,2392,2641,2044,3016,0,1605],
            [799,1047,1527,1681,789,1311,1019,479,1030,1624,327,1526,1294,1391,1562,1855,1790,1141,882,1035,477,1446,1605,0]]

ciudades=['Cdad de Bs As', 'Cordoba', 'Corrientes','Formosa', 'La Plata', 'La Rioja', 'Mendoza', 'Neuquen', 'Parana', 'Posadas', 'Rawson', 'Resistencia', 'Rio Gallegos', 'FdVd Catamarca', 'SM de Tucuman','SS Jujuy', 'Salta', 'San Juan', 'San Luis', 'Santa Fe', 'Santa Rosa', 'Sgo del Estero','Ushuaia','Viedma']

funObj = []
fit = []

poblacion=[]
decimales=[]
ruleta=[]
elegidos=[]
promedios=[]
maximos=[]
minimos=[]
mejores=[]

def unico(x,L):
  esUnico=True
  for i in range(len(L)):
    if x==L[i]:
      esUnico=False
      break
  return esUnico

def aleatorioC(a,b,c):
    cromo=[]
    j=0
    while j<c:
        r=random.randint(a,b)
        if unico(r,cromo):
            cromo.append(r)
            j+=1

    return cromo

def PoblacionInicial():
    poblacion=[]

    for i in range (0,50) :
        a=aleatorioC(1,23,23)
        poblacion.append(a)
    return poblacion

def carga ():
    poblacion.clear()
    for i in range (0,50):
        poblacion.append(Poblacion[i])

def cuentas ():
    print(poblacion)
    funObj.clear()
    fit.clear()
    sum = 0
    max = 0
    maxfituno=0
    maxfitdos=0

    min = 99999999

    for j in range(50):

        fobj=0
        for i in range(22):
            c1=int(poblacion[j][i])
            c2=int(poblacion[j][i+1])
            d=int(distancias[c1][c2])
            fobj+=d
        funObj.append(fobj)
        if max>(fobj):
            max=(fobj)
        if min<(fobj):
            min=(fobj)
        sum += fobj
        prom = (sum/50)
        sumf = 0
        ruleta.clear()
    for j in range(50):
        f = funObj[j]/sum
        fit.append(f)
        sumf += f
        if maxfituno<f:
            maxfituno=f
            mejorfituno=poblacion[j]
            #print('Uno',j,maxfituno,mejorfituno)

    for j in range(50):
        if maxfitdos<fit[j] and poblacion[j]!=mejorfituno:
            maxfitdos=fit[j]
            mejorfitdos=poblacion[j]
            #print('Dos',j,maxfitdos,mejorfitdos)


        for i in range(int(np.round(f*100))):
            ruleta.append(poblacion[j])

    for i in range(49):
        tabla.add_row([poblacion[i], funObj[i], fit[i]])

    print(tabla)
    tabla.clear_rows()
    print("Suma Funcion Objetivo: " , sum)
    print("Suma Fit: ", sumf)
    print("Maximo: " , max)
    print("Minimo: " , min)
    print("Promedio: ", prom)
    promedios.append(prom)
    maximos.append(max)
    minimos.append(min)
    mejores.append(mejorfituno)
    mejores.append(mejorfitdos)

'''
    for i in range (99):
        print(ruleta[i])
'''
def giraruleta():

    poblacion.clear()
    poblacion.append(mejores[0])
    poblacion.append(mejores[1])
    print('MEJORES', mejores)
    l=len(ruleta)
    #cross1=''
    #cross2=''
    b = aleatorioC(0,l-1,50)
    print(b)
    print(len(ruleta))
    for al in range(50):
        n=b[al]
        poblacion.append(ruleta[n])
    print(poblacion)






tabla = PrettyTable()
tabla.field_names=['Poblacion', 'Funcion Objetivo', 'Fit']

print("Corrida 0")
Poblacion=PoblacionInicial()
decimales.clear()
carga()
cuentas()
for i in range(199):
    print('Corrida', i+1)
    mejores.clear()
    cuentas()
    giraruleta()
print(Poblacion)
print(len(Poblacion))
print(len(Poblacion[0]))


