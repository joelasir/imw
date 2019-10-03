# Listado de directorios

Primero comenzamos creando la carpeta shared dentro del directorio /webapps .

![1](img/1.png)

Dentro del listado insertaremos los siguientes enalces, usando el comando *ln -s*
para así enlazar estos.

![2](img/2.png)

Ya enlazados entraremos al archivo alu5820.me, lo editaremos y añadimos lo siguiente:

![3](img/4.png)

Con esto podremos acceder al listado /shared con los enlaces creados anteriormente.

Por último haremos un *reload* al servicio Nginx para actualizar los cambios.

![4](img/6_reload.png)

 Y comprobamos en el navegador si funciona correctamente.

 ![5](img/5.png)
