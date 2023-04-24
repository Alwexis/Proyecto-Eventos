function toggleDescription() {
    let description_icon = document.querySelector('.titulo-descripcion i');
    let description = document.querySelector('.contenido-descripcion');
    description_icon.classList.toggle('toggled');
    description.classList.toggle('toggled');
}