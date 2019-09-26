# Mis series favoritas.


Añadimos el fichero de configuración de Nginx que se encargará de las peticiones que se hagan a nuestro dominio (alu5820.me). Esto lo haremos dentro la carpeta Nginx, en sites available.

![1](img/1.png)

 Después de realizar esto procederemos a enlazar el fichero que hemos creado en los sites-enable para que esté disponible.

 ![2](img/2.png)

 A continuación recargaremos la configuración de Nginx.

 ![3](img/3.png)

 Ahora ya podremos empezar a personalizar nuestra página web en nuestro *home*.
Crearemos un index.html dentro del directorio webapps/series.

 ![4](img/4.png)

 Una vez creada la "base" para nuestra página web empezaremos a descargar imágenes de nuestras series favoritas para añadirlas al index. ESto lo podemos hacer ejecutando un "wget *url de la imagen*"

![5](img/5_imagenes.png)

Ya descargadas las insertaremos en el index.html creado anteriormente.

![6](img/6_indeximg.png)

Y quedaría así.

![7](img/7_imagenes_alu.png)

Por último le insertaremos enlaces a las imágenes que nos lleven a su respectiva página en IMDB.

![8](img/8_insertar_enlace.png)

Y así queda finalmente: [Mis series](http://alu5820.me/series/)
