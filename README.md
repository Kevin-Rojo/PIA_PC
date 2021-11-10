# PIA_PC

## Table of Contents
1. [Informacion General](#general-info)
1. [Ejemplos de Uso](#ejemplos)
1. [Herramientas](#general-info)
2. [Technologies](#technologies)
3. [Installation](#installation)
4. [Collaboration](#collaboration)
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
```
python main.py -mode Manual
```

### Ejecucion Automatica con Parametros

#### Envio de Correos pishing
```
python main.py -script Email -dest [correo1,correo2,correo3]
```

#### Descarga de Documentos
```
python main.py -script Documents
```

#### Analisis de Puertos
```
python main.py -script Ports -ip [host:default="192.168.1.1"] -port [ports:default="8080"]
```

#### Web Scraping de Correos
```
python main.py -script WebMail
```

#### Analsis de Archivos con API Virus Total
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