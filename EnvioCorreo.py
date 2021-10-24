import smtplib
import ssl
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--e", type=str,required=True,help="Destinatario")
parser.add_argument("--m", type=str,required=True,help="Mensaje de correo")
args=parser.parse_args()


def EnvioCorreo(args):
    e = args.e
    m = args.m
    sender_email="alandgt15@gmail.com"
    password="prueba123_"
    smtp_server="smtp.gmail.com"
    port = 587  # For starttls
    context = ssl.create_default_context()
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