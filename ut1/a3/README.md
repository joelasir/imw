# Trabajo con virtual hosts.

La práctica consiste en crear 4 virtual hosts en Nginx con distintas configuraciones.
## Sitio web 1.
Debemos de crear *imw.alu5820.me* en sites-availables.
![1](img/1.png)

Dentro de este escribiremos lo siguiente: (nombre server, root)

![1.1](img/1.1.png)

Ya hecho eso enlazaremos con el comando *ln -s* a *sites-enabled*
![1.2](img/1.3.png)

A continuación iremos a /webapps y crearemos *imw*. Dentro de este crearemos el index.

![1.3](img/1.4_imw.png)

Descargaremos la imagen del Diagrama de unidades y la pondremos dentro del index.

![2](img/2.1_descargar_img.png)

![2.1](img/2.3_img_index.png)

Y así saldrá la imagen.

![2.2](img/2.4.png)

Hecho el primer paso procederemos al segundo.
Crearemos dentro de /webapps un directorio /mec el cual deberá tener un index para poner un enlace al Real Decreto.

![3](img/3_mec.png)

Modificaremos *imw.alu5820.me* y le pondremos un location para añadir el /mec

![3.1](img/3.1_location.png)

Modificamos el index y le pondremos el enlace correspondiente.

![3.2](img/3.4_enlace.png)

![3.3](img/3.4_enlace_decreto.png)

## Sitio web 2.
Comenzaremos creando *varlib.alu5820.me* siguiendo los pasos que hicimos anteriormente.

Enlazaremos y haremos reload para recagar la configuración
![4](img/4.1_varlib_enlac.png)

En el archivo del configuración de *varlib.alu5820.me* escribiremos el nombre del server, el root, y pondremos que podamos acceder usando el puerto 9000.

![4.1](img/4_varlib.png)

Y así sería el resultado:

![4.2](img/4.2_varlib_pagina.png)

## Sitio web 3.
Crearemos *ssl.alu5820.me*

Para este sitio web tendremos que poner que nos pida usuario y contraseña para acceder. Haremos los siguientes comandos:

![5](img/5_clave_user.png)

Se generará un archivo que en nuestro caso se almacenará en un fichero que tendremos en webapps llamado /ssl

Dentro de /webapps también debemos crear un fichero llamado /students en el que pondremos un index con el nombre de nuestros compañeros dentro.

![5.1](img/6_mostrar_nombre.png)

En el fichero de configuración del sitio web escribiremos el location.

![5.2](img/6_sites-ava_conf.png)

Comprobamos que funcione.

Ahora prohibiremos el acceso al fichero donde se aloja la contraseña.

![5.3](img/7_denegar_carpeta_passwd.png)

Para finalizar descargaremos *Certbot* para el certificado de nuestro sitio web.

![5.4](img/7_cat_certbot.png)


Por último comprobamos.

![5.4](img/6_web_pideclave.png)

![5.5](img/6_web_nombres.png)


## Sitio web 4.
Crearemos dos sitios webs: target.alu5820.me , redirect.alu5820.me .

El fichero de configuración del sitio web redirect quedará así:

![6](img/8_redirect.png)

Comprobaremos que nos redirecciona correctamente al target.


Antes de modificar el del target crearemos un fichero en /webapps que le daremos un nombre (en nuestro caso /redirect)

Ya creado modificaremos el archivo de configuración:

![6.1](img/10.png)

En el fichero creado anteriormente en /webapps descargaremos con el comando *wget* un archivo el cual tendremos que descomprimir usando *unzip* dentro de esta carpeta.

Accedemos al target y comprobamos que carga el archivo extraído:

![6.2](img/8_web.png)

Por último insertaremos los logfiles (en el target):

![6.3](img/9.png)
