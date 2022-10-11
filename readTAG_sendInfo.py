#Bibliotecas
import mysql.connector
import RPi.GPIO as GPIO
from time import sleep
import sys
from mfrc522 import SimpleMFRC522

#Iniciar el sensor
reader = SimpleMFRC522()
#Conexión
cnx = mysql.connector.connect(user='alex', password='4892', host = '192.168.1.109', database = 'codigoIoT')
cursor = cnx.cursor()

#Cuerpo del programa
try:
    #Leer el tag
    while True:
        print("Hold a tag near the reader")
        id, text = reader.read()
        print("ID: %s\nText: %s" % (id,text))
        insertquery = ("INSERT INTO rfid (nombre,texto,rfid) VALUES (%s,'Test Python 3',%s);"(id, text))
        cursor.execute(insertquery)
        cnx.commit()
        print("La operación del Query fue exitosa")
        #Cerrar
        cursor.close()
        cnx.close()
        sleep(10)
except KeyboardInterrupt:
    GPIO.cleanup()
    raise