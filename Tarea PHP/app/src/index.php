<!DOCTYPE html>
<html>
<head>
    <title>Formulario Lab0</title>
</head>
<body>
    <h1> Información del usuario </h1>
    <form method="post" action="index.php">
        <label for="nombre">Nombre:</label>
        <input type="text" id="nombre" name="nombre" required><br><br>
        <label for="edad">Edad:</label>
        <input type="number" id="edad" name="edad" required><br><br>
        <label for="description">Descripción:</label>
        <input type="text" id="description" name="description" required><br><br>

        <input type="submit" value="Enviar">
    </form>
</body>
</html>
<?php
    if ($_SERVER["REQUEST_METHOD"]=="POST" && isset($_POST['nombre']) && isset($_POST['edad']) && isset($_POST['description'])){

        $nombre = isset($_POST['nombre']) ? $_POST['nombre'] : '';
        $edad = isset($_POST['edad']) ? $_POST['edad'] : '';
        $description = isset($_POST['description']) ? $_POST['description'] : '';

        function generar_array($nombre, $edad, $description){
            $array = [
                "nombre" => $nombre,
                "edad" => $edad,
                "description" => $description,
            ];
            return $array;
        }

        function guardar_fichero($array) {
    
        $file = fopen('nombre_y_descripción.txt','a');
        fwrite($file, "La descripción del usuario {$array['nombre']} es la siguiente:  {$array['description']}) \n)");
        fclose($file);
        $edad=$array['edad'];
        $file2 = fopen('edades.txt','a');
        fwrite($file2,$edad ."\n");
        fclose($file2);
        

    }
        if ($_POST['nombre'] !='' && $_POST['edad'] !='' && $_POST['description'] !=''){

            $array_asociativo = generar_array ($nombre, $edad, $description);
            guardar_fichero($array_asociativo);
            
            $fileEdades = fopen('edades.txt','r');
            $sumaEdades = 0;
            $numeroEdades = 0;

            while(!feof($fileEdades)){
                $edad2 = fgets($fileEdades);
                $sumaEdades += intval($edad2);
                $numeroEdades++;
            }
            fclose($fileEdades);
            $numeroEdades--;
            $mediaedades = $sumaEdades / $numeroEdades;
            echo "La media de las edades es: " . $mediaedades;            
        }
}
?>
