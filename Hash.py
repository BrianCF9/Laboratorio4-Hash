
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

def HashBrianNasheeeeeeeeee(cadena):
    time=datetime.now()
    uf=int(ValorUF())
    largo=len(cadena)
    ascii_values=list()
    for character in cadena:
        ascii_values.append(ord(character))
    cadena=''
    cadena=cadena+str(uf)
    cadena=cadena+str(time.year)
    cadena=cadena+str(time.day)
    cadena=cadena+str(time.month)
    cadena=cadena+str(ascii_values[largo-1])
    cadena=cadena+str(largo)

    print(cadena)

    
    

    
    


HashBrianNasheeeeeeeeee('hola')


def Entropia(cadena):
    largo=len(cadena)
    #base ascii 128 caracteres
    base=128
    entropia=largo*math.log(base,2)
    return entropia



