const imagenRandom = Math.floor(Math.random() * 11) + 1;
document.querySelector('#gallery img').setAttribute('src', `../../assets/images/ilustraciones/ilustracion_${imagenRandom}.png`);