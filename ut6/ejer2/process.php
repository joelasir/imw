<!doctype html>
<html lang="es">
    <head>
        <meta charset="utf-8">
        <title>Ejercicio 2!</title>
    </head>
    <body>
        <?php
            $name = $_POST["name"];
            $surname = $_POST["surname"];
            $salario = $_POST["salario"];
            $age = $_POST["age"];
            if ($salario >= 2000) {
                echo "El nuevo salario es $salario euros";
            }
            elseif ($salario >= 1000 and $salario <= 2000) {
              if ($age > 45) {
                $salario *= 1.03;
                echo "El nuevo salario es $salario euros";
              }
              elseif ($age <= 45) {
                $salario *= 1.1;
                echo "El nuevo salario es $salario euros";
              }
            }
            elseif ($salario < 1000) {
              if ($age < 30) {
                $salario = 1100;
                echo "El nuevo salario es $salario euros";
              }
              elseif ($age >= 30 and $age < 45) {
                $salario *= 1.03;
                echo "El nuevo salario es $salario euros";
              }
              elseif ($age > 45) {
                $salario *= 1.45;
                echo "El nuevo salario es $salario euros";
              }
            }
        ?>
    </body>
</html>
