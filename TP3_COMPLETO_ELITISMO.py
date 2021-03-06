import random
from matplotlib import pyplot
from pylab import plot, show
import numpy as np
from prettytable import PrettyTable
import os
from skimage import io , transform , draw
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
img = io.imread("C:\\Users\\Facu\\Pictures\\TSM\\mapaArg.png")
img=transform.resize(img,(500, 400))
ciudades=['Cdad de Bs As', 'Cordoba', 'Corrientes','Formosa', 'La Plata', 'La Rioja', 'Mendoza', 'Neuquen', 'Parana', 'Posadas', 'Rawson', 'Resistencia', 'Rio Gallegos', 'FdVd Catamarca', 'SM de Tucuman','SS Jujuy', 'Salta', 'San Juan', 'San Luis', 'Santa Fe', 'Santa Rosa', 'Sgo del Estero','Usuahia','Viedma']
coordenadas=[(193,242),(138,146),(84,238),(64,245),(198,248),(120,105),(166,75),(253,87),(148,211),(86,288),(315,137),(82,231),(440,100),(99,116),(77,127),(38,127),(46,125),(148,77),(164,117),(145,203),(221,147),(87,160),(483,122),(280,166)]
funObj = []
fit = []
fitaux=[]
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
        a=aleatorioC(0,23,24)
        poblacion.append(a)
    return poblacion

def carga ():
    poblacion.clear()
    for i in range (0,50):
        poblacion.append(Poblacion[i])

def cuentas ():

    funObj.clear()
    fit.clear()
    sum=0
    max=0
    min=99999999
    maxfituno = 0
    maxfitdos = 0

    for j in range(50):

        fobj=0
        for i in range(0,23):
            c1=int(poblacion[j][i])
            c2=int(poblacion[j][i+1])
            d=int(distancias[c1][c2])
            fobj+=d
            if i ==23:
                cu=poblacion[-1]
                ci=poblacion[0]
                du=int(distancias[cu][ci])
                fobj+=du
        funObj.append(fobj)
        if max<fobj:
            max=fobj
        if min>fobj:
            min=fobj
        sum += fobj
        prom = (sum/50)
        sumfaux = 0
        sumf = 0
        ruleta.clear()
    for j in range(50):
        faux = funObj[j]/sum
        f=(1-faux)
        sumfaux+= f
        fitaux.append(f)
    for j in range(50):
        freal=(fitaux[j]/sumfaux)
        sumf = sumf+freal
        fit.append(freal)
        if maxfituno<freal:
            maxfituno=freal
            mejorfituno=poblacion[j]

    for j in range(10):
        if maxfitdos<fit[j] and poblacion[j]!=mejorfituno:
            maxfitdos=fit[j]
            mejorfitdos=poblacion[j]



        for i in range(int(np.round(f*100))):
            ruleta.append(poblacion[j])

    for i in range(50):
        tabla.add_row([poblacion[i], funObj[i], fit[i]])

    print(tabla)
    tabla.clear_rows()
    print("Suma Funcion Objetivo: " , sum)
    print("Suma Fit: ", sumf)
    print("Maximo: " , max)
    print("Minimo: " , min)
    print("Promedio: ", prom)
    for i in range(50):
        if funObj[i] == min:
            print('Menor Distancia : ',funObj[i])
            print('Menor Recorrido : ',poblacion[i])
            break

    promedios.append(prom)
    maximos.append(max)
    minimos.append(min)
    mejores.append(mejorfituno)
    mejores.append(mejorfitdos)

def giraruleta():

    poblacion.clear()
    poblacion.append(mejores[0])
    poblacion.append(mejores[1])

    l=len(ruleta)

    b = aleatorioC(0,l-1,48)

    for al in range(48):
        n=b[al]
        poblacion.append(ruleta[n])


    for i in range(0, 50, 2):
        c= random.random()
        if c <= 0.75:
            c1=poblacion[i].copy()
            c2=poblacion[i+1].copy()

            h1=[25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25]
            h2=[25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25]

            h1[0]=c1[0]
            h2[0]=c2[0]
            aux=c2[0]
            while (aux!=c1[0]):
                for i in range(len(c1)):

                    if (c1[i]!= aux):
                        i+=1
                    else:
                        h1[i]=c1[i]
                        h2[i]=c2[i]
                        aux=c2[i]

            for i in range(len(c1)):
                if (h1[i]==25):
                    h1[i]=c2[i]
                if (h2[i]==25):
                    h2[i]=c1[i]

            poblacion[i]=h1.copy()
            poblacion[i+1]=h2.copy()


    for i in range(50):
        c=random.random()
        if c <=0.05:

            cromo=poblacion[i].copy()
            cambiar=aleatorioC(0,23,2)
            j=cambiar[0]
            k=cambiar[1]
            a=cromo[j]
            cromo[j]=cromo[k]
            cromo[k]=a
            poblacion[i]=cromo




def menu():
    os.system('cls')
    print('Bienvenido. Ingrese la opcion deseada:')
    print('1- Obtener recorrido a partir de una ciudad.')
    print('2- Obtener mejor recorrido (heuristica).')
    print('3- Obtener mejor recorrido (genetico).')
    print('4- Salir')



def recorre(fila):
    recorrido=[]
    auxfila= fila
    recorrido.append(fila)
    aux=distancias[fila].copy()
    aux.remove(0)
    kmacum=0
    while len(recorrido)!= 24:
        for j in range(0,len(distancias[fila])):
            a=min(aux)
            b=distancias[fila][j]
            if (a==b):
                if ((j in recorrido)==False):
                    recorrido.append(j)
                    kmacum=kmacum + distancias[fila][j]
                    cor1=fila
                    fila=j
                    rr,cc, val= draw.line_aa(coordenadas[cor1][0],coordenadas[cor1][1],coordenadas[fila][0],coordenadas[fila][1])
                    img[rr,cc] = 0.25
                    aux=distancias[fila].copy()
                    aux.remove(0)
                    break
                else:
                    aux.remove(a)

    fila=recorrido[-1]
    kmacum= kmacum + distancias[fila][auxfila]
    rr,cc, val= draw.line_aa(coordenadas[fila][0],coordenadas[fila][1],coordenadas[auxfila][0],coordenadas[auxfila][1])
    img[rr,cc] = 1
    recorrido.append(auxfila)
    return recorrido ,kmacum


while True:
    menu()
    print('Opcion: ')
    opc=input()
    if opc == '1':
        img = io.imread("C:\\Users\\Facu\\Pictures\\TSM\\mapaArg.png")
        img=transform.resize(img,(500, 400))
        print('Ingrese ciudad de origen: ')
        ciudad=input()
        a=ciudades.index(ciudad)
        rec,km=recorre(a)
        print('Recorrido:')
        print(rec)
        print('Distancia en km:')
        print(km)
        city=[]
        for i in range(0,len(rec)):
            city.append(ciudades[rec[i]])
        print(city)
        io.imshow(img)
        io.show()

    elif opc == '2':
        recorrido=[]
        dist= []
        for i in range (0,24):

            a,b=recorre(i)
            recorrido.append(a)
            dist.append(b)
            aux=dist.index(min(dist))
        print('Recorrido optimo:')
        print(recorrido[aux])
        city=[]
        for i in range (0,len(recorrido[aux])):
            aux2=recorrido[aux][i]
            city.append(ciudades[aux2])
        print('Ciudades')
        print(city)
        print('Distancia Minima')
        print(dist[aux])
        print('')
        img=io.imread("C:\\Users\\Facu\\Pictures\\TSM\\mapaArg.png")
        img=transform.resize(img,(500, 400))
        for i in range(0,23):
            a=recorrido[aux][i]
            b=recorrido[aux][i+1]
            rr,cc, val= draw.line_aa(coordenadas[a][0],coordenadas[a][1],coordenadas[b][0],coordenadas[b][1])
            img[rr,cc] = 0.25
        a=recorrido[aux][23]
        b=recorrido[aux][24]
        rr,cc, val= draw.line_aa(coordenadas[a][0],coordenadas[a][1],coordenadas[b][0],coordenadas[b][1])
        img[rr,cc] = 1
        io.imshow(img)
        io.show()

    elif opc == '3':
        tabla = PrettyTable()
        tabla.field_names=['Poblacion', 'Funcion Objetivo', 'Fit']

        print("Corrida 0")
        Poblacion=PoblacionInicial()
        carga()
        cuentas()
        for i in range(199):
            print('Corrida', i+1)
            cuentas()
            giraruleta()

    elif opc == '4':
        break
    else:
        print('No ha ingresado ninguna opcion correcta, intente nuevamente.')

