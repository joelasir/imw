<!doctype html>
<html lang="es">
    <head>
        <meta charset="utf-8">
        <title>Ejercicio 3!</title>
    </head>
    <body>
        <?php
            $color1 = mt_rand(0, 255);
            $color2 = mt_rand(0, 255);
            $color3 = mt_rand(0, 255);
            echo ("<style> body {background-color: rgb($color1, $color2, $color3)}</style>");
        ?>
    </body>
</html>
