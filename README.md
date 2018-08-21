# noeh
Un generador de puertas traseras en formato PHP para la interaccion de la terminal local del servidor por medio de python

# Uso
Al ejecutar noeh, lo primero que debemos hacer en tal caso de que no hayamos generado la carga util lo generaremos con el siguiente comando: generate out 'nombre de la carga util' passwd 'contraseña', para posteriormente al subir ese archivo en el servidor al que atacaremos solo buscamos la ruta donde se encuentre el archivo por ej: 'http://localhost/test.php', una vez hecho eso solo usamos el comando de noeh conn_addr 'La url del archivo' passwd 'La contraseña para confirmar la identidad' noconfirm 'true or false, true en el caso de que se desea no confirmar que es un archivo legible para la interaccion entre la maquina-victima y la maquina-atacante, false para la contrario', y para finalizar solo ejecutar los comandos que conocemos dependiendo del sistema operativo.

# Informacion de noeh

 info: It is a code written in python to generate backdoors in PHP format for soon in a
 post-splash to interact with the website remotely, Use the command [info] to show the information and help.

[Noeh] > Hi, my name is DtxdF!

# Capturas de pantalla
![](https://i.imgur.com/rHXQQRx.png)
![](https://i.imgur.com/CBFdzE1.png)
