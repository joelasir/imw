# Sirviendo aplicaciones Php y Python.

Configuraremos dos sitios web en los que usaremos php y python.

# Sitio web 1.

Crearemos el sitio web *php.alu5820.me* y lo enlazamos correctamente.

![1](img/1.png)

Y añadimos la configuración necesaria para que nginx procese los archivos PHP.
Le añadiremos un index al index.php para obligar que el fichero índice sea el index.php

![2.1](img/2_server.png)

Tenemos que mostrar la aplicación **demo_php.zip**
Para ello crearemos *demo* en webapps.

![2](img/2.png)

Y dentro descomprimiremos la aplicación php.

![3]/img/3_unzip.png)

Haremos un reload al servicio Nginx y comprobamos que funcione la aplicación correctamente.

![4](img/4_final.png)


## Sitio web 2.

Para este sitio web debemos crear *now.alu5820.me*. Lo enlazamos y configuramos el sitio web.

![5](img/5.png)

Añadiremos las líneas de configuración para que nginx procese las aplicaciones python.
También añadiremos un location *static* para que se almacenen los ficheros estáticos en el.

![6](img/13_now.png)

En webapps crearemos el directorio *now* en el que crearemos nuestra aplicación python.

![7](img/6_webapps.png)

Tendrá el siguiente código.

![8](img/7_codigopy.png)

Dentro del directorio *now* crearemos el entorno virtual utilizando el comando *pipenv*.
Instalaremos flask y pytz.

![9](img/8_flask.png)

![9](img/9_pytz.png)

Ahora crearemos un script para activar el entorno virtual con el siguiente código.

![10](img/diez.png)

Le daremos permisos.

![11](img/11_permisos_run.png)

Ahora procederemos a configurar *supervisor*.
Para que nuestro programa sea gestionado por supervisor tenemos que añadir un fichero de configuración.

![12](img/12_supervisorconf.png)

![12.1](img/12.1_conf.png)

Ya configurado el supervisor realizaremos un par de comandos para ver la respuesta del navegador al acceder a la web.

![14](img/14.png)

![15](img/15.png)

![16](img/16.png)

![17](img/17.png)
