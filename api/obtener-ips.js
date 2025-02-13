function obtenerIP() {
    fetch("https://api64.ipify.org?format=json")
        .then(response => response.json())
        .then(data => {
            let ip = data.ip;
            // Llamamos a la función para guardar la IP en el servidor
            guardarIPEnServidor(ip);
        })
        .catch(() => {
            console.error("No se pudo obtener la IP.");
        });
}

function guardarIPEnServidor(ip) {
    // Aquí se hace un fetch para enviar la IP al servidor.
    fetch("guardar_ips.php", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ ip: ip })
    })
    .then(response => response.json())
    .then(data => {
        // Aquí mostramos las IPs obtenidas desde el servidor
        obtenerIPsDesdeServidor();
    })
    .catch(() => {
        console.error("No se pudo guardar la IP en el servidor.");
    });
}

function obtenerIPsDesdeServidor() {
    fetch("obtener_ips.php")
        .then(response => response.json())
        .then(data => {
            mostrarIPs(data.ips);
        })
        .catch(() => {
            console.error("No se pudo obtener las IPs.");
        });
}

function mostrarIPs(ipList) {
    const ipsElement = document.getElementById("ips");
    ipsElement.innerHTML = '';

    ipList.forEach(ip => {
        let ipElement = document.createElement('div');
        ipElement.textContent = ip;
        ipElement.classList.add('ip');
        ipElement.onclick = function() {
            // Lógica para redirigir si la IP tiene permisos
            if (esIPPermitida(ip)) {
                window.location.href = `2.html?ip=${ip}`;
            }
        };
        ipsElement.appendChild(ipElement);
    });
}

function esIPPermitida(ip) {
    // Lógica para verificar si la IP tiene permisos (ajustar según lo necesites)
    let ipList = JSON.parse(localStorage.getItem("ips")) || [];
    return ipList.includes(ip);
}

// Llamar a obtenerIP al cargar la página
obtenerIP();