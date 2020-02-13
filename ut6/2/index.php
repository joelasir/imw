<!doctype html>
<html lang="es">
    <head>
        <meta charset="utf-8">
        <title>Ejercicio 2!</title>
    </head>
    <body>
        <form action="process.php" method="post">
            <label for="name">Nombre:</label>
            <input type="text" name="name"/><br>
            <label for="surname">Apellidos</label>
            <input type="text" name="surname"/><br>
            <label for="salario">Salario</label>
            <input type="number" name="salario"/><br>
            <label for="age">Edad</label>
            <input type="number" name="age"/>
            <input type="submit" name="enviar"/>      
        </form>
    </body>
</html>
