<!doctype html>
<html lang="es">
    <head>
        <meta charset="utf-8">
        <title>Ejercicio 4!</title>
    </head>
    <body>
        <form action="index.php" method="post">
            <label for="row">Filas:</label>
            <input type="number" name="row"/><br>
            <label for="column">Columnas</label>
            <input type="number" name="column"/><br>
            <input type="submit" name="enviar"/>
        </form><br>
        <table border="1">
        <?php
        if (isset($_POST["row"]) and isset($_POST["column"])) {
        $row = $_POST["row"];
        $column = $_POST["column"];
        echo("<style>td {padding:15px;}</style>");
          if ($row >= 1 and $column >= 1) {
            $f = 1;
            $c = 1;
            while ($f <= $row) {
              echo("<tr>");
              while ($c <= $column) {
                echo("<td></td>");
                $c++;
              }
              $f++;
              $c = 1;
              echo("</tr>");
          }
        }
          else {
            echo ("Error. Introduzca un número válido.");
          }
        }
        ?>
      </table>
    </body>
</html>
