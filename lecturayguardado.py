import serial
from serial import Serial

from datetime import datetime, timedelta
from datetime import date
from time import time
DateNow = date.today()
TimeNow = datetime.now().time()

data = serial.Serial('MI_COM',VELOCIDAD_DEL COM) #Por ejemplo serial.Serial('COM3',115200)


import os
import shutil

CurrentHour = TimeNow.hour

filename = str(DateNow) + ' ' + str(CurrentHour) + ".csv"

directorio = 'MI_DIRECTORIO' + str(DateNow) # LA CARPETA QUE SE CREA ES CON LA FECHA DEL DIA, ES OPCIONAL EL DIRECTORIO SE EJEMPLIFICA ASI "C:\DATA/" ESTA CARPETA DEBE EXISIR

if os.path.isdir(directorio):       #ESTA COMPROBACION NOS AYUDA A QUE SI EL PROGRAMA SE NOS TRUNCO Y VUELVE ARRANCAR NO SE BOTE POR QUE LA CARPETA YA EXISTE.
    print('La carpeta existe.');
else:
    os.mkdir(directorio)
    print('La carpeta no existia.'); # EN CASO DE NO EXISTIR LA CREARA. 

dirfilename = directorio + '/' + filename #AHORA VIENE LA CREACION DEL ARCHIVO. DENTRO DE LA CARPETA CREADA. 

print (filename)




while True: # MIENTRAS EL ROGRAMA ESTE CORRIENDO SEGUIRA LEYENDO EL COM A MANERA DE CICLO
    data_1 = data.readline().decode("ascii")
    data_1  = data_1 [:-2]   # EN MI CASO BORRO EL SALTO DE LINEA QUE MANDO DESDE EL ESP32 ESTO DEPENDERA DE TU DESARROLLO
   
   
    f = open(dirfilename,'a')
    data_WRITE = str(time())+ ',' + data_WRITE # CONCATENAMOS LA FECHA EN FORMATO UNIX + EL DATO
    f.write(data_WRITE) # LO ESCRIBE EN NUESTRO .CSV
    f.write('\n') # NOS DA UN SALTO DE LINEA QUE EN EL ARCHIVO ES UNA NUEVA FILA
