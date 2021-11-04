#Se establecen los parámetros
param([string]$ipaddress, [int]$port)
#Se crea la variable con la función 'tnc' para establecer una conexión con el puerto
$conection = tnc $ipaddress -Port $port #-ErrorAction Ignore
#Condicion de si el puerto esta abierto o cerrado
if ($conection.TcpTestSucceeded){
     Write-Host "Conectado"
} else { 
     Write-Host "Desconectado"
}