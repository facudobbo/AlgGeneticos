elementos= [[150,20],[325,40],[600,50],[805,36],[430,25],[1200,64],[770,54],[60,18],[930,46],[353,28]]
sol=[]
solPosible = []


for a in range(1, 11):
    sol.append((a))
    for b in range(a+1, 11):
        sol.append((a,b))
        for c in range(b+1, 11):
            sol.append((a,b,c))
            for d in range(c+1,11):
                sol.append((a,b,c,d))
                for e in range(d+1, 11):
                    sol.append((a,b,c,d,e))
                    for f in range(e+1,11):
                        sol.append((a,b,c,d,e,f))
                        for g in range(f+1,11):
                            sol.append((a,b,c,d,e,f,g))
                            for h in range(g+1,11):
                                sol.append((a,b,c,d,e,f,g,h))
                                for i in range(h+1,11):
                                    sol.append((a,b,c,d,e,f,g,h,i))
                                    for j in range(i+1,11):
                                        sol.append((a,b,c,d,e,f,g,h,i,j))


solucion = 0
for i in range(0, len(sol)):
    solucion = sol[i]
    vSol = 0
    voluSol = 0
    objeto = 0
    indice = 0
    elemento = 0
    longitud = 0
    if(type(solucion) == tuple):
        longitud = len(solucion)
        for j in range(0, longitud):
            objeto = solucion[j]
            indice = objeto - 1
            elemento = elementos[indice]
            vSol = vSol + elemento[1]
            voluSol = voluSol + elemento[0]


    else:
        objeto = solucion
        indice = objeto - 1
        elemento = elementos[indice]
        vSol = vSol + elemento[1]
        voluSol = voluSol + elemento[0]
    if (voluSol <= 4200):
        solPosible.append((solucion,voluSol,vSol))

    solucion = 0

solPosible.sort(key= lambda x: x[2], reverse=True)

print('Solucion: ' + str(solPosible[0][0]))
print('Valor de la solucion: ' + str(solPosible[0][2]))
print('Peso de la solucion: ' + str(solPosible[0][1]))
