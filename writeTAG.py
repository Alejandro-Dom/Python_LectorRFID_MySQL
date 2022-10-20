
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

try:
        nombre = input('Nombre:')
        edad = input('Edad:')
        telefono = input('Telefono:')
        naci = input('Fecha de nacimiento:')
        matricula = input('Matrícula:')
        text = (nombre + "," + edad + "," + telefono + "," + naci + "," + matricula)
        print("Acerca el TAG al sensor")
        reader.write(text)
        print("Tag escrito")
finally:
        GPIO.cleanup()