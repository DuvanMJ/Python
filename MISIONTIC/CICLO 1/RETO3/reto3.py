#Número de sucursales y pacientes
entrada=input()
datos=entrada.split()
n=int(datos[0])
m=int(datos[1] )
l_existencia=[]
l_entrega=[]
#si la cantidad de sucursales es menor a 1 se debe leer nuevamente ambos valores hasta que se ingrese un n válido
while n < 1 :
    n=int(input())
    m=int(input())
#Luego, para las n sucursales (numeradas de 1 a n) se debe leer la cantidad de existencias actuales del 
#medicamento y esta debe ser mayor o igual a 1, y en caso de que no se cumpla se debe leer valores hasta que
#se ingrese uno válido
for i in range(n):
    existencia=int(input())
    while existencia < 1:
        existencia=int(input())
    l_existencia.append(existencia)
#para los m pacientes se debe leer el número de la sucursal donde será atendido, seguido de información de las 
#presiones sistólica y diastólica del mismo.

l_entrega = [0] * n
for i in range(m):
    entrada2=input()
    datos2=entrada2.split()
    sucursal=int(datos2[0])
    psis=int(datos2[1])
    pdia=int(datos2[2])
    dosis=0
    if psis < 80 and pdia<60:
        dosis=5
    elif psis >= 80 and psis < 120 and pdia >= 60 and pdia < 80:
        dosis=0
    elif psis >= 120 and psis < 130 and pdia >= 80 and pdia < 85:
        dosis=0
    elif psis >= 130 and psis < 140 and pdia >= 85 and pdia < 90:
        dosis=2
    elif psis >= 140 and psis < 160 and pdia >= 90 and pdia < 100:
        dosis=5
    elif psis >= 160 and psis < 180 and pdia >= 100 and pdia < 110:
        dosis=10
    elif psis >= 180  and pdia >= 110:
        dosis=30
    elif psis >= 140 and pdia < 90:
        dosis=20
    l_entrega[sucursal-1]=l_entrega[sucursal-1]+dosis
def restarlistas(lis1,lis2):
    lis3=[]
    for i in range(len(lis1)):
        lis3.append(lis1[i]-lis2[i])
    return lis3
def porcentaje(lis1,lis2):
    lis3=[]
    for i in range(len(lis1)):
        lis3.append(lis1[i]*100/lis2[i])
    return lis3

l_posterior= restarlistas(l_existencia,l_entrega)
maximo = max(l_posterior)
i_max = l_posterior.index(maximo)
minimo = min(l_posterior)
i_min = l_posterior.index(minimo)
l_porcentaje= porcentaje(l_entrega,l_existencia)
print(f"{i_min+1} {minimo}\n{i_max+1} {maximo}")
for i in range(n):
    print(f"{i+1} {l_porcentaje[i]:.2f}%") 
    

    



