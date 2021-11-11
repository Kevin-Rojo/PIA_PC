# PIA_PC

## Table of Contents
1. [Informacion General](#general-info)
1. [Ejemplos de Uso](#ejemplos)s
5. [Contacto](#contacto)

## Informacion General
<a name="general-info"></a>
#### Producto Integrador de prendizaje
**Unidad de Aprendizaje:**  Programacion para Ciberseguridad

Conjunto de Herramientas basadas en Python y powershell para la ayuda de procesos enfocados a la seguridad informatica

## Ejemplos de Uso
<a name="ejemplos"></a>
### Ejecucion desatendida
```
python main.py
```

### Ejecucion Manual
manda un menu y en base a eso hace la accion que se pide 
```
python main.py -mode Manual
```

### Ejecucion Automatica con Parametros
hace una ejecucion automatica pero solo del script que especifique 


#### Envio de Correos pishing
se envia un correo a las direcciones que se encuentre en el archivo config.txt
```
python main.py -script Email -dest [correo1,correo2,correo3]
```

#### Descarga de Documentos
descarga los documentos de una url especifica y crea un reporte de los documentos descargados 
```
python main.py -script Documents
```

#### Analisis de Puertos
se comprueba que los puertos de la red esten abiertos y se puedan enviar o recibir datos 
```
python main.py -script Ports -ip [host:default="192.168.1.1"] -port [ports:default="8080"]
```

#### Web Scraping de Correos
extraer correos de una url e informacion de su dominio 
```
python main.py -script WebMail
```

#### Analsis de Archivos con API Virus Total
analiza una carpeta de archivos en una API y verifica que no sean malware reconocido
```
python main.py -script VirusTotal
```



<a name="contacto"></a>
## Contacto
##### Kevin Samuel Rojo Ortega
* **Correo:** kevin.rojoor@uanl.edu.mx
##### Ramon Gilberto Valdez Escareño
* **Correo:** ramon.valdezes@uanl.edu.mx
##### Alan Damian Garcia Torres
* **Correo:** damian.garciatrrs@uanl.edu.mx
##### Juan Angel Rodriguez Bulnes
* **Correo:** juan.rodriguezblns@uanl.edu.mx
##### Jairo Ivan Hernandez Hernandez
* **Correo:** jairo.hernandezhdz@uanl.edu.mx




<!-- | Headline 1 in the tablehead | Headline 2 in the tablehead | Headline 3 in the tablehead |
|:--------------|:-------------:|--------------:|
| text-align left | text-align center | text-align right | -->