# UT4-A1 Implantación de Worpdress

Comenzaremos creando la base de datos de Worpdress junto un usuario con acceso a esta en MySQL.

![1](./img/1.png)

Descargaremos el código fuente de Wordpress desde su página web usando el comando *curl*.

![2](./img/2.png)


Posteriormente lo descomprimiremos.

![3](./img/3_unzip.png)

Y lo copiamos en la ruta */usr/share*

![4](./img/4.png)

Le daremos permisos al usuario web *www-data* para que tenga acceso a estos ficheros.

![5](./img/5.png)

Ahora modificaremos el archivo de configuración de Wordpress para establecer el nombre de la base de datos, el usuario y la contraseña.

![6](./img/6.png)

![7](./img/7.png)

Crearemos un sitio web en Nginx con la siguiente configuración.

![8](./img/8_sitio_nginx.png)

Enlazamos para habilitar el sitio web.

![9](./img/9_enlace.png)

Reiniciamos el servicio y comprobamos que esté todo en funcionamiento.

![10](./img/10_reload.png)

Entramos a la url del sitio que hemos creado y comprobamos que se nos abre el sitio para configurar Wordpress.

![11](./img/11_wordpress.png)

Y vamos configurando los distintos parámetros.

![12](./img/12_conf.png)

![13](./img/13.png)

Ya configurado nos pedirá el usuario y clave que creamos anteriormente para poder acceder.

![14](./img/14.png)

Lo primero que haremos será ir a la pestaña de - *Apariencia -> Temas* - y elegir un tema que nos guste.

![15](./img/15_temas.png)

Y lo instalamos.

![16](./img/16_instalar_tema.png)

![16-1](./img/16_activar_tema.png)

Ahora ajustaremos los permalinks. Seleccionamos - *Día y nombre* - y guardamos los cambios.

![17](./img/17_enlaces_permanentes.png)

Ahora le indicaremos a Nginx que procese estas URLs que hemos creado. Modificamos el archivo de configuración del sitio web y añadimos lo siguiente:

![18](./img/18.png)

También configuraremos el límite de subida de archivos a Wordpress, ya que por defecto solo viene como máximo 2MB. Iremos al archivo *php.ini* y modificamos las siguientes líneas:

![19](./img/19.png)

![20](./img/20.png)

![21](./img/21.png)

Reiniciamos el servicio.

![22](./img/22_restart.png)

Además debemos añadir una línea al fichero de configuración de Nginx.

![23](./img/23_client_max.png)

Ya configurado Worpdress procedemos a crear un sencillo Post con las estadísticas de Wordpress.

![24](./img/24_entrada.png)

Y así quedaría la página con el tema y el Post que hemos escrito.

![25](./img/25_pagina.png)

Por último le añadiremos un certificado a nuestro sitio web con Certbot.

![26](./img/26_certbot.png)

Así quedaría nuestra configuración del sitio web en Nginx:

![27](./img/27_cat.png)

Y así nuestra página web con su certificado.

![28](./img/28_pagina_final.png)

