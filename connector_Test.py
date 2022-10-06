#Bibliotecas
import mysql.connector

#Programa
print("Conectandose a la base de datos")
cnx = mysql.connector.connect(user='alex', password='4892', host = '192.168.1.109', database = 'codigoIoT') 
print("Conexión realizada")
print(cnx)

print("Cerrar conexión")
cnx.close()
print("Conexión cerrada")