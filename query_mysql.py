#Bibliotecas
import mysql.connector

#Conexión
cnx = mysql.connector.connect(user='alex', password='4892', host = '127.0.0.1', database = 'detector_sintomas')
cursor = cnx.cursor()

query = ("SELECT id, nombre, temp FROM registro WHERE nombre = 'Alejandro Dominguez';")
cursor.execute(query)

res = cursor.fetchall()

for x in res:
    print (x)

cnx.close