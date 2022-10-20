#Bibliotecas
import mysql.connector
import RPi.GPIO as GPIO
from time import sleep
import sys
from mfrc522 import SimpleMFRC522
import argparse

#Parser
parser = argparse.ArgumentParser()
parser.add_argument("status")
args = parser.parse_args()

#Iniciar el sensor
reader = SimpleMFRC522()

#Realizar la conexión
cnx = mysql.connector.connect(user='alex', password='4892', host = '192.168.1.109', database = 'codigoIoT')
#Cursor
cursor = cnx.cursor()

#Cuerpo del programa
try:
    #Hacer lectura unica
    print("Acerca el Tag al sensor")
    id, text = reader.read()
    sttr = text.split(",")
    sleep(1)
    insertquery = ("INSERT INTO rfid (nombre,texto,rfid) VALUES ('" + sttr[0] +"','" + args.status + "'," + 
    str(id)+");")
    print(insertquery)

    #Ejecutar cursor
    cursor.execute(insertquery)
    #Asegurarse de eralizr la operancion en la base de datos
    cnx.commit()
    print("Query OK")
    sleep(1)

    #Cerrar
    cursor.close()
    cnx.close()
    GPIO.cleanup()
except KeyboardInterrupt:
    #Cerrar
        cursor.close()
        cnx.close()
        GPIO.cleanup()
        raise