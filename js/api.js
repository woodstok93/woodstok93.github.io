fetchData();

async function fetchData( ) {

    try{
        const Carrito = document.getElementById("Carrito").value.toLowercase();

        const response = await fetch('https://www.mercadolibre.com.ar/');

        if (!response.ok){
            throw new error("Could not fetch resource");

        }  
        const data = await response.json();
        const imgElement = document.getElementById("Carrito");

       imgElement.style.display = "block";
        console.log(data);
    }
    catch(error){
        console.error(error);
    }
}