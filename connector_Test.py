import mysql.connector

cnx = mysql.connector.connect(user='Alex', password='4892', host = '192.168.1.109', database = 'codigoIoT')
cnx.close()