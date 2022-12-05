##Librerias Iniciales
import serial
from serial import Serial  # libreria usada pyserial

import os #Creacion de directorios
## recursos especifivcos de Librerias.
from datetime import datetime, timedelta
from datetime import date
from time import time
##  Codigo
DateNow = date.today()
TimeNow = datetime.now().time()

CurrentHour = TimeNow.hour

filename = str(DateNow) + ' ' + str(CurrentHour) + ".csv" # importante considerar el tipo de archivo  a utilizar en este caso es un CSV

directorio = 'Mi_carpeta' + str(DateNow)  # ejemplo ==  \data\temp/

if os.path.isdir(directorio): # comprobamos que la carpeta donde comenzaremos a guardar la informacion exista. 
    print('La carpeta existe.');
else:
    os.mkdir(directorio)
    print('La carpeta no existia.');

print (filename)  # nos aseguramos que el nombre del archivo a crear es el correcto

ser = serial.Serial('COM3',115200) #declaracion de la variable que contendra, la informacion leida por el COM SERIAL y la velocidad con la que esperamos leer

f = open(filename,'a')
#el siguiente ciclo permanecera activo mientras la lectura del COM este habilitada, estara guardando archivos en la carpeta con el nombre del dia de Hoy, los archivos
# se guardaran en archivos .CSV por hora, esto se puede modificar si asi se desea, cuando se llegue a la hora 23 se creara la carpeta con nombre del dia de mañana correspóndiente, 
# y seguira sesivamente, hasta que la lectura del COM o el proceso del programa se interrumpa. 
while True:
    Received = ser.readline().decode("ascii") #lectura de PUERTO COM
    Received = Received[:-1] #Quitamos el salto de linea. 
    
    
    TimeNow = datetime.now().time()
    tm = (str(DateNow) + ' ' + str(TimeNow))
    if TimeNow.hour != CurrentHour :
      f.write(str(time())+','+Received)
        CurrentHour = TimeNow.hour
        DateNow = date.today()
        f.close()
        print(filename)
        t = "Mi_carpeta" # ejemplo ==  \data\temp/
        t+= str(DateNow) + "/" + str(CurrentHour) + '.csv'
        if CurrentHour == 23:
          # con base a la libreria de Data time, creamos variables de ayer, hoy y mañana. se utilizaran mas delante, ya que guardamos nuestos archivos en una carpeta
          #que se del dia actual y consultamos el dia anterior y el de mañana en el proceso.

            presentday = datetime.now()
            yesterday = presentday - timedelta(1)
            tomorrow = presentday + timedelta(1)

            directorio = 'Mi_carpeta' + tomorrow.strftime('%Y-%m-%d')
            if os.path.isdir(directorio):
                os.mkdir(directorio)
                print('La carpeta de nuevo dia existe. ');
            else:
                os.mkdir(directorio)
                print('La carpeta de nuevo dia no existia.');
                print (dir_yesterday)
        f = open(t,'a', newline='\n', encoding='utf-8')

f.close()
