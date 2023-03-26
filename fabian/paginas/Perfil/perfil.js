async function loadData() {
    //? ¿Qué es fetch?
    // Fetch es una función que nos permite hacer peticiones HTTP a un servidor y nos devuelve una promesa
    //? ¿Qué es una promesa?
    // Una promesa es un objeto que representa el resultado de una operación asíncrona. Una promesa puede estar en uno de tres estados:
    // - Pendiente: Estado inicial, ni cumplida ni rechazada.
    // - Cumplida: Significa que la operación se completó satisfactoriamente.
    // - Rechazada: Significa que la operación falló.
    //? ¿Qué es una función asíncrona?
    // Una función asíncrona es una función que devuelve una promesa. Cuando una función asíncrona retorna un valor, la promesa se resuelve con el valor retornado. Cuando la función asíncrona lanza una excepción o algún valor, la promesa es rechazada con el valor lanzado.
    //? ¿Qué es await?
    // Await es una palabra clave que nos permite esperar a que una promesa se cumpla o se rechace, y nos devuelve el valor de la promesa.
    const response = await fetch('https://raw.githubusercontent.com/Alwexis/Events-Scraper/main/data/final%20data.json');
    const data = await response.json();
    const eventWrapper = document.querySelector('#event-wrapper');
    //? ¿Qué hace Object.keys?
    // Object.keys() es una función de la clase Object que nos permite obtener las llaves de un objeto.
    Object.keys(data).forEach((key) => {
        //? ¿Qué es data[key]?
        // data[key] es un arreglo de objetos, cada objeto representa un evento. El nombre que tiene en este ejemplo es por el nombre del objeto que cree.
        //? ¿Qué hace forEach?
        // forEach() es una función de la clase Array que nos permite iterar sobre cada elemento de un arreglo.
        data[key].forEach((event) => {
            let eventComponent;
            //? ¿Qué es window.navigator.userAgentData.mobile?
            // window.navigator.userAgentData.mobile es una propiedad que nos permite saber si el usuario está usando un dispositivo móvil o no.
            if (window.navigator.userAgentData.mobile) {
                eventComponent = buildMobileEventComponent(event);
            } else {
                eventComponent = buildDesktopEventComponent(event);
            }
            eventWrapper.appendChild(eventComponent);
        });
    });
}

function buildDesktopEventComponent(event) {
    const eventElement = document.createElement('div');
    eventElement.classList.add('evento');
    // Imagen del evento
    const eventImageDiv = document.createElement('div');
    eventImageDiv.classList.add('imagen-evento');
    const eventImage = document.createElement('img');
    let eventImageText;
    if (event.img === 'No disponible') {
        eventImage.src = 'https://cliply.co/wp-content/uploads/2021/09/142109670_SAD_CAT_400.gif';
        eventImageText = document.createElement('span');
        eventImageText.classList.add('no-image-text');
        eventImageText.innerText = 'Imagen no disponible :(';
    } else {
        eventImage.src = event.img;
    }
    eventImage.alt = event.nombre;
    eventImageDiv.appendChild(eventImage);
    if (eventImageText) {
        eventImageDiv.appendChild(eventImageText);
    }

    eventElement.appendChild(eventImageDiv);
    // Nombre del evento
    const eventName = document.createElement('span');
    eventName.classList.add('nombre-evento');
    eventName.innerText = event.nombre;

    eventElement.appendChild(eventName);
    // Descripcion del evento
    const eventDescription = document.createElement('p');
    eventDescription.classList.add('descripcion-evento');
    // Arreglaremos la descripcion
    const description = event.descripcion != 'No disponible' ? event.descripcion.replace(/\n/g, '') : 'No hay descripcion disponible';
    eventDescription.innerText = description;

    eventElement.appendChild(eventDescription);
    // Informacion del evento
    const eventInfoContainer = document.createElement('div');
    eventInfoContainer.classList.add('informacion-evento-container');
    // Fecha del evento
    const eventDate = document.createElement('div');
    eventDate.classList.add('informacion-evento');
    // Ícono de fecha
    const eventDateIcon = document.createElement('span');
    eventDateIcon.classList.add('material-symbols-outlined');
    eventDateIcon.innerText = 'calendar_month';
    // Texto de fecha
    const eventDateText = document.createElement('p');
    eventDateText.innerText = event.fecha;

    eventDate.appendChild(eventDateIcon);
    eventDate.appendChild(eventDateText);
    eventInfoContainer.appendChild(eventDate);
    // Lugar del evento
    const eventPlace = document.createElement('div');
    eventPlace.classList.add('informacion-evento');
    // Ícono de lugar
    const eventPlaceIcon = document.createElement('span');
    eventPlaceIcon.classList.add('material-symbols-outlined');
    eventPlaceIcon.innerText = 'location_on';
    // Texto de lugar
    const eventPlaceText = document.createElement('p');
    eventPlaceText.innerText = event.lugar;

    eventPlace.appendChild(eventPlaceIcon);
    eventPlace.appendChild(eventPlaceText);
    eventInfoContainer.appendChild(eventPlace);
    // Precio del evento
    const eventPrice = document.createElement('div');
    eventPrice.classList.add('informacion-evento');
    // Ícono de precio
    const eventPriceIcon = document.createElement('span');
    eventPriceIcon.classList.add('material-symbols-outlined');
    eventPriceIcon.innerText = 'payments';
    // Texto de precio
    const eventPriceText = document.createElement('p');
    eventPriceText.innerText = event.precio;

    eventPrice.appendChild(eventPriceIcon);
    eventPrice.appendChild(eventPriceText);
    eventInfoContainer.appendChild(eventPrice);

    eventElement.appendChild(eventInfoContainer);
    // Boton de ver evento
    const eventButtonContainer = document.createElement('a');
    eventButtonContainer.classList.add('boton-evento-container');
    eventButtonContainer.href = event.url;
    eventButtonContainer.target = '_blank';
    const eventButton = document.createElement('div');
    eventButton.classList.add('boton-evento');
    const eventButtonText = document.createElement('span');
    eventButtonText.innerText = 'Ver Evento';

    eventButton.appendChild(eventButtonText);
    eventButtonContainer.appendChild(eventButton);
    eventElement.appendChild(eventButtonContainer);

    return eventElement;
}

function buildMobileEventComponent(event) {
    const eventElement = document.createElement('div');
    eventElement.classList.add('evento');
    // Creamos la parte superior del evento, en donde irán la imagen y texto.
    const eventTopSide = document.createElement('div');
    eventTopSide.classList.add('evento-top-side');
    // Nombre del evento
    const eventName = document.createElement('span');
    eventName.classList.add('nombre-evento');
    eventName.innerText = event.nombre;

    eventElement.appendChild(eventName);
    // Imagen del evento
    const eventImageDiv = document.createElement('div');
    eventImageDiv.classList.add('imagen-evento');
    const eventImage = document.createElement('img');
    eventImage.src = event.img;
    eventImage.alt = event.nombre;
    eventImageDiv.appendChild(eventImage);

    eventTopSide.appendChild(eventImageDiv);
    // Informacion del evento
    const eventInfoContainer = document.createElement('div');
    eventInfoContainer.classList.add('informacion-evento-container');
    // Fecha del evento
    const eventDate = document.createElement('div');
    eventDate.classList.add('informacion-evento');
    // Ícono de fecha
    const eventDateIcon = document.createElement('span');
    eventDateIcon.classList.add('material-symbols-outlined');
    eventDateIcon.innerText = 'calendar_month';
    // Texto de fecha
    const eventDateText = document.createElement('p');
    eventDateText.innerText = event.fecha;

    eventDate.appendChild(eventDateIcon);
    eventDate.appendChild(eventDateText);
    eventInfoContainer.appendChild(eventDate);
    // Lugar del evento
    const eventPlace = document.createElement('div');
    eventPlace.classList.add('informacion-evento');
    // Ícono de lugar
    const eventPlaceIcon = document.createElement('span');
    eventPlaceIcon.classList.add('material-symbols-outlined');
    eventPlaceIcon.innerText = 'location_on';
    // Texto de lugar
    const eventPlaceText = document.createElement('p');
    eventPlaceText.innerText = event.lugar;

    eventPlace.appendChild(eventPlaceIcon);
    eventPlace.appendChild(eventPlaceText);
    eventInfoContainer.appendChild(eventPlace);
    // Precio del evento
    const eventPrice = document.createElement('div');
    eventPrice.classList.add('informacion-evento');
    // Ícono de precio
    const eventPriceIcon = document.createElement('span');
    eventPriceIcon.classList.add('material-symbols-outlined');
    eventPriceIcon.innerText = 'payments';
    // Texto de precio
    const eventPriceText = document.createElement('p');
    eventPriceText.innerText = event.precio;

    eventPrice.appendChild(eventPriceIcon);
    eventPrice.appendChild(eventPriceText);
    eventInfoContainer.appendChild(eventPrice);

    eventTopSide.appendChild(eventInfoContainer);
    eventElement.appendChild(eventTopSide);
    // Creamos la "Bottom Side" del evento, que sería únicamente el botón de ver evento
    const eventButtonContainer = document.createElement('a');
    eventButtonContainer.classList.add('boton-evento-container');
    eventButtonContainer.href = event.url;
    eventButtonContainer.target = '_blank';
    const eventButton = document.createElement('div');
    eventButton.classList.add('boton-evento');
    const eventButtonText = document.createElement('span');
    eventButtonText.innerText = 'Ver Evento';

    eventButton.appendChild(eventButtonText);
    eventButtonContainer.appendChild(eventButton);
    eventElement.appendChild(eventButtonContainer);

    return eventElement;
}

function setupScrollEvents() {
    const scrollTopButton = document.querySelector('#go-top');
    //? ¿Qué hace esto?
    // Agrega un evento click al elemento scrollTopButton, que al hacer click, hace que el elemento main se desplace hacia arriba
    scrollTopButton.addEventListener("click", function() {
        document.querySelector('main').scrollIntoView({ behavior: 'smooth' });
        scrollTopButton.classList.remove('shown');
        scrollTopButton.classList.add('hidden');
    });

    //? ¿Qué hace esto?
    // Agrega un evento scroll al elemento window, que al hacer scroll, hace que el elemento scrollTopButton se muestre o se oculte.
    window.addEventListener("scroll", function() {
        let scrollPosition = document.documentElement.scrollTop || document.body.scrollTop;
        if (scrollPosition >= 400 && scrollTopButton.classList.contains('hidden')) {
            scrollTopButton.classList.remove('hidden');
            scrollTopButton.classList.add('shown');
        } else if (scrollPosition <= 400 && scrollTopButton.classList.contains('shown')) {
            scrollTopButton.classList.remove('shown');
            scrollTopButton.classList.add('hidden');
        }
     }, false);
}

setupScrollEvents();
loadData();