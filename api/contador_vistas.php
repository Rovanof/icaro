<?php
// Archivo donde se almacenan las visitas
$contadorArchivo = 'contador.json';

// Leer el archivo donde se almacenan las visitas
if (file_exists($contadorArchivo)) {
    $data = json_decode(file_get_contents($contadorArchivo), true);
    $visitas = $data['visitas'];
} else {
    $visitas = 0;
}

// Incrementar el contador
$visitas++;

// Guardar el nuevo contador en el archivo
file_put_contents($contadorArchivo, json_encode(['visitas' => $visitas]));

// Devolver el número total de visitas como JSON
echo json_encode(['visitas' => $visitas]);
?>