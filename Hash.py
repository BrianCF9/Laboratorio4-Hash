
import requests
import time
from datetime import date, datetime
import json
import math
import hashlib
import csv



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
    while decision!=6:
        print("Bienvenido al mecanismo de hashing de Brian Nasheeee:\nOpción 1: Hashear una cadena de texto \nOpción 2: Hashear un archivo de texto \nOpción 3: Calcular entropía de una cadena de texto\nOpción 4: Comparación entropy vs SHA1,SHA2,MD5\nOpción 5: Comparación time vs SHA1,SHA2,MD5 \nOpción 6: Salir del programa:)\n")
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
            print("Ingrese la ruta de su archivo de Texto:\n")
            ruta=str(input())
            f = open (ruta,'r', encoding='utf-8')
            mensaje = f.readlines()
            lista=list()
            encabezado=list()
            encabezado.append('Cadena')
            encabezado.append('HashBrian')
            encabezado.append('Entropy')
            encabezado.append('SHA1')
            encabezado.append('Entropy')
            encabezado.append('SHA256')
            encabezado.append('Entropy')
            encabezado.append('MD5')
            encabezado.append('Entropy')
            lista.append(encabezado)

            for i in mensaje:
                if mensaje!='':
                    lista2=list()
                    aux=HashBrianNasheeeeeeeeee(i)
                    print('HashBrian: '+aux+', entropy: '+str(Entropia(aux)))
                    sha1 = hashlib.new("sha1", bytes(i, encoding = "utf-8"))
                    sha1e=Entropia(sha1.hexdigest())
                    print('SHA1: '+sha1.hexdigest()+', entropy: '+str(sha1e))
                    sha256 = hashlib.new("sha3_256", bytes(i, encoding = "utf-8"))
                    sha256e=Entropia(sha256.hexdigest())
                    print('SHA256: '+sha256.hexdigest()+', entropy: '+str(sha256e))
                    md5 = hashlib.new("md5", bytes(i, encoding = "utf-8"))
                    md5e=Entropia(md5.hexdigest())
                    print('MD5: '+md5.hexdigest()+', entropy: '+str(md5e))
                    print('\n')
                    lista2.append(i)
                    lista2.append(aux)
                    lista2.append(str(Entropia(i)))
                    lista2.append(sha1.hexdigest())
                    lista2.append(sha1e)
                    lista2.append(sha256.hexdigest())
                    lista2.append(sha256e)
                    lista2.append(md5.hexdigest())
                    lista2.append(md5e)
                    lista.append(lista2)
            
            with open('comparacion.csv', 'w',encoding='utf-8',newline='') as file:
                writer = csv.writer(file, delimiter=';')
                writer.writerows(lista)
        
        elif decision==5:
            print("Ingrese la ruta de su archivo de Texto:\n")
            ruta=str(input())
            f = open (ruta,'r', encoding='utf-8')
            mensaje = f.readlines()
            lista=list()
            encabezado=list()
            encabezado.append('Nombre Hash')
            encabezado.append('Cantidad de Strings')
            encabezado.append('Tiempo en segundos')
            lista.append(encabezado)


            contador=0
            time1=time.time()
            for i in mensaje:
                if mensaje!='':
                    aux=HashBrianNasheeeeeeeeee(i)
                    contador+=1
            time2=time.time()        
            lista2=list()
            lista2.append('HashBrian')
            lista2.append(contador)
            lista2.append(str(round(time2-time1,2)).replace('.',','))
            lista.append(lista2)

            contador=0
            time1=time.time()
            for i in mensaje:
                if mensaje!='':
                    sha1 = hashlib.new("sha1", bytes(i, encoding = "utf-8"))
                    contador+=1
            time2=time.time()        
            lista2=list()
            lista2.append('SHA1')
            lista2.append(contador)
            lista2.append(str(round(time2-time1,2)).replace('.',','))
            lista.append(lista2)

            contador=0
            time1=time.time()
            for i in mensaje:
                if mensaje!='':
                    sha256 = hashlib.new("sha3_256", bytes(i, encoding = "utf-8"))
                    contador+=1
            time2=time.time()        
            lista2=list()
            lista2.append('SHA256')
            lista2.append(contador)
            lista2.append(str(round(time2-time1,2)).replace('.',','))
            lista.append(lista2)

            contador=0
            time1=time.time()
            for i in mensaje:
                if mensaje!='':
                    md5 = hashlib.new("md5", bytes(i, encoding = "utf-8"))
                    contador+=1
            time2=time.time()        
            lista2=list()
            lista2.append('MD5')
            lista2.append(contador)
            lista2.append(str(round(time2-time1,2)).replace('.',','))
            lista.append(lista2)


                    
            
            with open('comparaciontiempos.csv', 'w',encoding='utf-8',newline='') as file:
                writer = csv.writer(file, delimiter=';')
                writer.writerows(lista)

        elif decision==6:
            print("Saludos!")
        else:
            print("Por favor ingrese una opción válida")

    

