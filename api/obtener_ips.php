?php
$ipsFile = 'ips.json';  // Archivo donde se almacenan las IPs

// Verificar si el archivo existe y devolver las IPs
if (file_exists($ipsFile)) {
    $ips = json_decode(file_get_contents($ipsFile), true);
    echo json_encode(['ips' => $ips]);
} else {
    echo json_encode(['ips' => []]);
}
?>