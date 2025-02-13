?php
$ipsFile = 'ips.json';  // Archivo donde guardamos las IPs

// Obtener los datos recibidos (la IP del cliente)
$data = json_decode(file_get_contents('php://input'), true);
$ip = $data['ip'];

// Cargar las IPs existentes
if (file_exists($ipsFile)) {
    $ips = json_decode(file_get_contents($ipsFile), true);
} else {
    $ips = [];
}

// Agregar la nueva IP si no está ya en la lista
if (!in_array($ip, $ips)) {
    $ips[] = $ip;
}

// Guardar las IPs en el archivo JSON
file_put_contents($ipsFile, json_encode($ips));

echo json_encode(['status' => 'success']);
?>