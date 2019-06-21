objetos= [[150,20],[325,40],[600,50],[805,36],[430,25],[1200,64],[770,54],[60,18],[930,46],[353,28]]

heuristica=[]
resultado=[]

for i in range(10):
   funcion = objetos[i][0] / objetos[i][1]
   heuristica.append((funcion,objetos[i][0],objetos[i][1],i+1))

heuristica.sort(key = lambda x : x[0], reverse=True)
proxPeso=0
pesoAct=0
valorTot=0

for i in range(0,10):
   proxPeso = pesoAct + heuristica[i][1]
   if proxPeso <= 4200:
        resultado.append(heuristica[i][3])
        pesoAct+=heuristica[i][1]
        valorTot=heuristica[i][2]

resultado.sort()

print('Los objetos a cargar en la mochila son los nro:',resultado)


