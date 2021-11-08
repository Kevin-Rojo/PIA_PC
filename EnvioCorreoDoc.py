#Importamos librerias

#Utilizada para enviar correo
import smtplib

#Utilizada para la conexion segura
import ssl

#Utilizada para pasar argumentos
import argparse

#Pasamos dos argumentos de caracter obligatorio
parser = argparse.ArgumentParser()
#Argumento --e correo del destinatario
parser.add_argument("--e", type=str,required=True,help="Destinatario")
#Argumento --m Mensaje
parser.add_argument("--m", type=str,required=True,help="Mensaje de correo")
args=parser.parse_args()


def EnvioCorreo(args):
    #Pasamos los argumentos a variables
    e = args.e
    m = args.m
    #Informacion del correo  utilizada para enviar los correos
    sender_email="alandgt15@gmail.com"
    password="prueba123_"
    smtp_server="smtp.gmail.com"
    #Puerto utilizado para el servidor smpt
    port = 587  # For starttls
    #Creamos la conexion
    context = ssl.create_default_context()
    #Intentamos enviar el correo
    try:
        server = smtplib.SMTP(smtp_server, port)
        server.ehlo() # Can be omitted
        server.starttls(context=context) # Secure the connection
        server.ehlo() # Can be omitted
        server.login(sender_email, password)
        server.sendmail(sender_email, e, m)
    except Exception as e:
        print(e)
    finally:
        server.quit()

EnvioCorreo(args)