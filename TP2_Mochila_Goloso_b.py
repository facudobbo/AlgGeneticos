objetos= [[1800,72],[600,36],[1200,60]]

heuristica=[]
resultado=[]

for i in range(3):
   funcion = objetos[i][0] / objetos[i][1]
   heuristica.append((funcion,objetos[i][0],objetos[i][1],i+1))

heuristica.sort(key = lambda x : x[0], reverse=True)
proxPeso=0
pesoAct=0
valorTot=0

for i in range(0,3):
   proxPeso = pesoAct + heuristica[i][1]
   if proxPeso <= 3000:
        resultado.append(heuristica[i][3])
        pesoAct+=heuristica[i][1]
        valorTot=heuristica[i][2]

resultado.sort()

print('Los objetos a cargar en la mochila son los nro:',resultado)
