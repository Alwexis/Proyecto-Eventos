//document.querySelector('#logo-svg');
(async () => {
    const response = await fetch('https://raw.githubusercontent.com/Alwexis/Proyecto-Eventos/main/icono.svg');
    const text = await response.text();
    document.querySelector('#logo').innerHTML = text;
})();