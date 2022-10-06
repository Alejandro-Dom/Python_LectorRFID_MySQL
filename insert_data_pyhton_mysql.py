#Bibliotecas
import mysql.connector

#Conexión
cnx = mysql.connector.connect(user = 'alex', password = '4892', host = '127.0.0.1', database = 'codigoIoT')

#Cursor
cursor = cnx.cursor() 
insertquery = ("INSERT INTO rfid (nombre,texto,rfid) VALUES ('Alex','Test Python 3',50986321);")

#Ejecutar cursor
cursor.execute(insertquery)

#Asegurar que la operación se logro hacer en la base de datos
cnx.commit()
print("La operación del Query fue exitosa")

#Cerrar
cursor.close()
cnx.close()