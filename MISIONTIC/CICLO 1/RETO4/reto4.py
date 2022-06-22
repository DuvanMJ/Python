#Número de sucursales y pacientes
import numpy as np
entrada=input()
datos=entrada.split()
n=int(datos[0]) #Sucursales
k=int(datos[1]) #Tipo de medicamento
m=int(datos[2] ) #Número de pacientes
M_nk=[]
#M_entrega=[[],[]]
#si la cantidad de sucursales es menor a 1 se debe leer nuevamente ambos valores hasta que se ingrese un n válido
while n < 1 or k<1:
    n=int(input())
    m=int(input())
#Luego, para las n sucursales (numeradas de 1 a n) 
# se debe leer la cantidad de existencias actuales de todos los tipos de medicamentos 
# en una línea. 
for i in range(n):
    existencia=input().split()
    existenciaint= list(map(int,existencia))
    
        
        #while existencia < 1:
        #    existencia=int(input())
    M_nk.append(existenciaint)
#para los m pacientes se debe leer el número de la sucursal donde será atendido, seguido del tipo 
# de medicamento solicitado y el número de existencias solicitadas del mismo, seguido de la información
#  de las presiones sistólica y diastólica.

M_nkentrega = []
for i in range(m):
    entrada2 = input().split()
    datos2 = list(map(int,entrada2))
    
    #SALIDA
    sucursal=int(datos2[0])
    tipomed=int(datos2[1])
    cantmed=int(datos2[2])
    psis=int(datos2[3])
    pdia=int(datos2[4])
    dosis=0
    b1=0
    if psis < 80 and pdia<60:
        b1=1
    elif psis >= 80 and psis < 120 and pdia >= 60 and pdia < 80:
        b1=1
    elif psis >= 120 and psis < 130 and pdia >= 80 and pdia < 85:
        b1=1
    elif psis >= 130 and psis < 140 and pdia >= 85 and pdia < 90:
        b1=1
    elif psis >= 140 and psis < 160 and pdia >= 90 and pdia < 100:
        b1=1
    elif psis >= 160 and psis < 180 and pdia >= 100 and pdia < 110:
        b1=1
    elif psis >= 180  and pdia >= 110:
        b1=1
    elif psis >= 140 and pdia < 90:
        b1=1
    if b1==0:
        cantmed, datos2[2]=0, 0
    M_nkentrega.append(datos2)
    M_nk[sucursal-1][tipomed-1]-=cantmed
M_nk2=np.array(M_nk)
M_nkentrega2=np.array(M_nkentrega)
#minimos
def minimo (s):
    mini=min(M_nk[s])
    pos=M_nk[s].index(mini)
    return pos, mini
def maximo (s):
    maxi=max(M_nk[s])
    pos=M_nk[s].index(maxi)
    return pos, maxi
import numpy as np

def minpromax (M_nkentrega2,k,m,s):
    M_nkentrega2=np.array(M_nkentrega2)
    lista=[]
    for j in range (m):
        if (s+1) == M_nkentrega2[j][0]:
            lista.append(M_nkentrega2[j,1:3])
    if len(lista)==0:
        lista.append([0,0])
    lista2=np.array(lista)
    #mínimo
    if len(lista) < k:
        mini=0
    else:
        mini=min(lista2[:,1])
    #máximo
    maxi=max(lista2[:,1])
    #promedio
    promedio =0
    for elemento in lista2[:,1]:
        promedio+=elemento
    promedio1=promedio/k
    promedio2=promedio/len(lista)
    return mini, promedio1, maxi, promedio2
def minmaxt1 (M_nkentrega2,M_nk2,n,m):
    M_nkentrega3=np.array(M_nkentrega2)
    M_nk3=np.array(M_nk2)
    lista1=[0]*n
    lista2=M_nk3[:,0]
    lista3=[0]*n
    lista4=[0]*n
    for i in range(m):
        if M_nkentrega2[i][1]==1:
            lista1[M_nkentrega2[i][0]-1]=M_nkentrega2[i][2]

    minimo=min(lista1)
    maximo=max(lista1)
    

    for i in range(n):
        if lista1[i]==minimo:
            lista3[i]=lista2[0]
        else:
            lista3[i]=100000000
    minimo2=min(lista3)

    for i in range(n):
        if lista1[i]==maximo:
            lista4[i]=lista2[0]
        else:
            lista4[i]=100000000
    maximo2=min(lista4)
    
    posmin=lista3.index(minimo2)
    posmax=lista4.index(maximo2)
    return (posmin+1), minimo, (posmax+1), maximo
resultado=minmaxt1(M_nkentrega2,M_nk2,n,m)

for i in range(n):
    mini=minimo(i)
    maxi=maximo(i)
    print(f"{i+1}\n{mini[0]+1} {mini[1]}\n{maxi[0]+1} {maxi[1]}")
    mpm=minpromax(M_nkentrega2,k,m,i)
    print(f"{mpm[0]:.2f} {mpm[1]:.2f} {mpm[2]:.2f}\n{mpm[3]:.2f}")
print(f"{resultado[0]} {resultado[1]}\n{resultado[2]} {resultado[3]}")



    

    



