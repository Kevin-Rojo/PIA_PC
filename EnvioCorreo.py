import smtplib
import ssl
import argparse
from email.mime.text import MIMEText

# parser = argparse.ArgumentParser()
# parser.add_argument("--e", type=str,required=True,help="Destinatario")
# parser.add_argument("--m", type=str,required=True,help="Mensaje de correo")
# args=parser.parse_args()


def EnvioCorreo(dest,msg):
    e = dest
    m= open(msg,'r')
    

    sender_email="ksrojo31@gmail.com"
    password="BattleField4"
    smtp_server="smtp.gmail.com"
    port = 587  # For starttls
    context = ssl.create_default_context()

    mail_postfix = "gmail.com"

    me = "hola" + "<" + sender_email + "@" + mail_postfix + ">" 
    msg = MIMEText(m.read(), _subtype = 'html', _charset = 'gb2312') # Cree una instancia, aquí configurada en formato de correo html
    msg ['Asunto'] = "Sotify" # establecer asunto
    msg['From'] = me
    msg['To'] = ";".join(e)
    print(msg)
    try:
        server = smtplib.SMTP(smtp_server, port)
        server.ehlo() # Can be omitted
        server.starttls(context=context) # Secure the connection
        server.ehlo() # Can be omitted
        server.login(sender_email, password)
        server.sendmail(me, e, msg.as_string())
    except Exception as e:
        print(e)
    finally:
        server.quit()

list=["kevin.rojoor@gmail.com"]
EnvioCorreo(list, "mail.html")