from os import close
import smtplib
import ssl
import argparse
from email.mime.text import MIMEText
import base64

def decriptPassword(passw):
    password = passw
    print(type(password))
    password = base64.b64decode(password)
    password=password.decode("utf-8")
    return password

def EnvioCorreo(dest):

    e = dest
    
    with open("EmailConfig.txt") as f:
        lineas = f.readlines()

    m=open(lineas[2].split(":")[1],"rb")

    sender_email=lineas[0].split(":")[1]
    password=decriptPassword(lineas[1].split(":")[1])

    print(sender_email)

    smtp_server="smtp.gmail.com"
    port = 587  # For starttls
    context = ssl.create_default_context()
    mail_postfix = "gmail.com"

    me = "hola" + "<" + sender_email + "@" + mail_postfix + ">" 
    msg = MIMEText(m.read(), _subtype = 'html', _charset = 'UTF-8') # Cree una instancia, aquí configurada en formato de correo html
    msg ['Subject'] = "Spotify" # establecer asunto
    msg['From'] = me
    msg['To'] = ";".join(e)

    try:
        server = smtplib.SMTP(smtp_server, port)
        server.ehlo() # Can be omitted
        server.starttls(context=context) # Secure the connection
        server.ehlo() # Can be omitted
        print("haciendo Loggin")
        server.login(sender_email, password)
        for mail in e:
            server.sendmail(me, mail, msg.as_string())
    except Exception as e:
        print(e)
    finally:
        server.quit()

list=["uririsa@gmail.com","kevin.rojoor@gmail.com","krojo_10@hotmail.com"]
EnvioCorreo(list)