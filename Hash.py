
import requests
import time
from datetime import date, datetime
import json
import math



def ValorUF():
    valor='uf'
    fecha=date.today()
    if(fecha.day<10):
        day='0'+str(fecha.day)
    else:
        day=str(fecha.day)
    if(fecha.month<10):
        month='0'+str(fecha.month)
    else:
        month=str(fecha.month)
    year=str(fecha.year)
    fecha=day+'-'+month+'-'+year
    
    
    # En este caso hacemos la solicitud para el caso de consulta de un indicador en un año determinado
    url = f'https://mindicador.cl/api/{valor}/{fecha}'
    response = requests.get(url)
    data = json.loads(response.text.encode("utf-8"))
    # Para que el json se vea ordenado, retornar pretty_json
    pretty_json = json.dumps(data, indent=2)
    
    return data['serie'][0]['valor']

def HashBrianNasheeeeeeeeee(palabra):
    time=datetime.now()
    uf=int(ValorUF())
    cadena=''
    
    cadena=cadena+str(uf)



    largo=len(palabra)

    ascii_values=list()
    values=list()
    for character in palabra:
        values.append(character)
        ascii_values.append(ord(character))
        
    if str(values[0])=='\n':
        cadena=cadena+str('a')
    else:
        cadena=cadena+str(values[0])

    cadena=cadena+str(int((ascii_values[int(largo/2)])/2))


    if str(values[int(largo/2)])=='\n':
        cadena=cadena+str('e')
    else:
        cadena=cadena+str(values[int(largo/2)])
        
    
    

    cadena=cadena+str(time.year)
    cadena=cadena+str(time.day)


    if str(values[largo-1])=='\n':
        cadena=cadena+str('i')
    else:
        cadena=cadena+str(values[largo-1])
    


    
    cadena=cadena+str(time.month)
    cadena=cadena+str(int((time.hour)/10))
    cadena=cadena+str(int((time.minute)/10))


    if str(values[int(largo/4)])=='\n':
        cadena=cadena+str('o')
    else:
        cadena=cadena+str(values[int(largo/4)])
    




    cadena=cadena+str(int(((ascii_values[int(largo/2)])/2+(ascii_values[largo-1])/10)))
    cadena=cadena+str(time.second+10)
    
    
    

    return cadena
    


def Entropia(cadena):
    largo=len(cadena)
    #base ascii 128 caracteres
    base=128
    entropia=largo*math.log(base,2)
    return entropia


if __name__=="__main__":
    decision=0
    while decision!=4:
        print("Bienvenido al mecanismo de hashing de Brian Nasheeee:\nOpción 1: Hashear una cadena de texto \nOpción 2: Hashear un archivo de texto \nOpción 3: Calcular entropía de una cadena de texto\nOpción 4: Salir del programa:)\n")
        decision=int(input())
        if decision==1:
            print("Ingrese su cadena de Texto:\n")
            cadena=str(input())
            aux=HashBrianNasheeeeeeeeee(cadena)
            print('Hashing: '+aux+', largo'+str(len(aux)))
            print('\n')
        elif decision==2:
            print("Ingrese la ruta de su archivo de Texto:\n")
            ruta=str(input())
            f = open (ruta,'r', encoding='utf-8')
            mensaje = f.readlines()
            for i in mensaje:
                if mensaje!='':
                    print('Mensaje:'+str(i)+'\nHasheando:')
                    aux=HashBrianNasheeeeeeeeee(str(i))
                    largo=len(aux)
                    if largo<25:
                        for i in range(largo,25):
                            aux=aux+'a'
                    print(aux+', largo'+str(len(aux)))
                    print('\n')
                
                
            f.close()
        elif decision==3:
            print("Ingrese la cadena de Texto:\n")
            cadena=str(input())
            aux=Entropia(cadena)
            print('La entropia es: '+str(aux)+'\n')
            
        elif decision==4:
            print("Saludos!")
        else:
            print("Por favor ingrese una opción válida")

    
