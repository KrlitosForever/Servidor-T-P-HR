async function actualizarPanel() {
    // 1. Hacemos la petición GET a la URL de tu API
    const respuesta = await fetch("http://127.0.0.1:8000/datos");
    
    // 2. Convertimos la respuesta cruda a un objeto JSON que JavaScript pueda manejar
    const datos = await respuesta.json();

    // 3. Buscamos los IDs en tu HTML y reemplazamos los guiones por los números reales
    document.getElementById("dato-temp").innerText = datos.temperatura;
    document.getElementById("dato-humedad").innerText = datos.humedad;
}

// Ejecutamos la función para que los datos aparezcan al cargar la página
actualizarPanel();