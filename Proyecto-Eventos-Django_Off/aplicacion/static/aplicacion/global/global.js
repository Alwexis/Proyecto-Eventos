window.onload = async function () {
    const logoElements = document.querySelectorAll('.logo');
    if (logoElements.length > 0) {
        const response = await fetch('https://raw.githubusercontent.com/Alwexis/Proyecto-Eventos/main/icono.svg');
        const text = await response.text();
        logoElements.forEach(logoElement => logoElement.innerHTML = text);
    }
}