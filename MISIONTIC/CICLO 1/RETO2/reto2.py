var_numper=int(input())
salario=908526
var_puntaje=0
var_contador=0
var_contsin=0
var_contafro=0
var_contind=0
var_contrai=0
var_contpal=0
var_contgit=0
for i in range(var_numper):
    var_etnico=str(input())
    var_estrato=int(input())
    var_ingreso=int(input())
    if (var_etnico=="sin reconocimiento"):
        puntaje=0
        var_contsin+=1
        if (var_estrato==1):
            puntaje=puntaje+15
        elif (var_estrato==2):
            puntaje=puntaje+13
        elif (var_estrato==3):
            puntaje=puntaje+11
        elif (var_estrato==4):
            puntaje=puntaje+7
        elif (var_estrato==5):
            puntaje=puntaje+0
        elif (var_estrato==6):
            puntaje=puntaje+0
        else:
            puntaje=9999999999
            var_contsin-=1
    elif (var_etnico=="afrodescendiente"):
        puntaje=9
        var_contafro+=1
        if (var_estrato==1):
            puntaje=puntaje+15
        elif (var_estrato==2):
            puntaje=puntaje+13
        elif (var_estrato==3):
            puntaje=puntaje+11
        elif (var_estrato==4):
            puntaje=puntaje+7
        elif (var_estrato==5):
            puntaje=puntaje+0
        elif (var_estrato==6):
            puntaje=puntaje+0
        else:
            puntaje=9999999999
            var_contafro-=1
    elif (var_etnico=="indigena"):
        puntaje=10
        var_contind+=1
        if (var_estrato==1):
            puntaje=puntaje+15
        elif (var_estrato==2):
            puntaje=puntaje+13
        elif (var_estrato==3):
            puntaje=puntaje+11
        elif (var_estrato==4):
            puntaje=puntaje+7
        elif (var_estrato==5):
            puntaje=puntaje+0
        elif (var_estrato==6):
            puntaje=puntaje+0
        else:
            puntaje=9999999999
            var_contind-=1
    elif (var_etnico=="raizal"):
        puntaje=11
        var_contrai+=1
        if (var_estrato==1):
            puntaje=puntaje+15
        elif (var_estrato==2):
            puntaje=puntaje+13
        elif (var_estrato==3):
            puntaje=puntaje+11
        elif (var_estrato==4):
            puntaje=puntaje+7
        elif (var_estrato==5):
            puntaje=puntaje+0
        elif (var_estrato==6):
            puntaje=puntaje+0
        else:
            puntaje=9999999999
            var_contrai-=1
    elif (var_etnico=="palenquero"):
        puntaje=12
        var_contpal+=1
        if (var_estrato==1):
            puntaje=puntaje+15
        elif (var_estrato==2):
            puntaje=puntaje+13
        elif (var_estrato==3):
            puntaje=puntaje+11
        elif (var_estrato==4):
            puntaje=puntaje+7
        elif (var_estrato==5):
            puntaje=puntaje+0
        elif (var_estrato==6):
            puntaje=puntaje+0
        else:
            puntaje=9999999999
            var_contpal-=1
    elif (var_etnico=="gitano"):
        puntaje=13
        var_contgit+=1
        if (var_estrato==1):
            puntaje=puntaje+15
        elif (var_estrato==2):
            puntaje=puntaje+13
        elif (var_estrato==3):
            puntaje=puntaje+11
        elif (var_estrato==4):
            puntaje=puntaje+7
        elif (var_estrato==5):
            puntaje=puntaje+0
        elif (var_estrato==6):
            puntaje=puntaje+0
        else:
            puntaje=9999999999
            var_contgit-=1
    else:
        puntaje=9999999999

    
        

    if (var_ingreso<salario):
        puntaje=puntaje+20
    elif (var_ingreso>=salario and var_ingreso<2*salario):
        puntaje=puntaje+14
    elif (var_ingreso>=2*salario and var_ingreso<4*salario):
        puntaje=puntaje+12
    elif (var_ingreso>=4*salario and var_ingreso<5*salario):
        puntaje=puntaje+9
    elif (var_ingreso>=5*salario):
        puntaje=puntaje+0
    else:
        puntaje=9999999999
        

    if (puntaje>=30 and puntaje<999999999):
        #print ("El candidato continua en el proceso de seleccion")
        var_contador+=1
    
        
        
    
print(f'{var_contador}')
print(f'sin reconocimiento {var_contsin}\nafrodescendiente {var_contafro}\nindigena {var_contind}\nraizal {var_contrai}\npalenquero {var_contpal}\ngitano {var_contgit}')

