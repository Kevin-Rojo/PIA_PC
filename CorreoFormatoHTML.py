
import smtplib
from email.mime.text import MIMEText
 
mailto_list = ["kevin.rojoor@gmail.com"] # Dirección de correo electrónico del destinatario
mail_host = "smtp.gmail.com" # Configurar el servidor
mail_user = "ksrojo31@gmail.com" # buzón del remitente
mail_pass = "BattleField4" # Código de autorización del remitente
mail_postfix = "gmail.com" # Postfix de la bandeja de salida


def send_mail (to_list, sub, content): # to_list: destinatarios; sub: asunto; contenido: contenido del mensaje
    me = "hola" + "<" + mail_user + "@" + mail_postfix + ">" # Hola aquí se puede configurar arbitrariamente, después de recibir la carta, se mostrará de acuerdo con la configuración
    print(me)
    msg = MIMEText (content, _subtype = 'html', _charset = 'gb2312') # Cree una instancia, aquí configurada en formato de correo html
    msg ['Asunto'] = sub # establecer asunto
    msg['From'] = me
    msg['To'] = ";".join(to_list)
    try:
        s = smtplib.SMTP()
        s.connect (mail_host) # conectar servidor smtp
        s.login (mail_user, mail_pass) # servidor de inicio de sesión
        s.sendmail (me, to_list, msg.as_string ()) # enviar correo
        s.close()
        return True
    except (Exception):
        print ("Falló ...")
        return False
 
if __name__ == '__main__':
    
    msg= open("mail.html",'r')
    
    print(msg.read())

    #if send_mail(mailto_list, "hello", "<a href='http://www.cnblogs.com/visec479/'>Dana、Li</a>"):
    #    print ("Enviar correctamente")
    #else:
    #    print ("Error al enviar")
