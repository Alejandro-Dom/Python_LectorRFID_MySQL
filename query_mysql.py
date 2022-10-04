#Bibliotecas
import datetime
import mysql.connector

#Conexión
cnx = mysql.connector.connect(user='alex', password='4892', host = '127.0.0.1', database = 'detector_sintomas')
cursor = cnx.cursor()

query = ("SELECT id, nombre, protodiagnostico FROM registro WHERE id= 13")
res = cnx.cmd_query(query)

print("Respuesta")
print(res)

#cursor.close()
cnx.close()