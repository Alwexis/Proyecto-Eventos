window.onload = () => {
    const imagenRandom = Math.floor(Math.random() * 11) + 1;
    // document.querySelector('#gallery img').setAttribute('src', `../../assets/images/ilustraciones/ilustracion_${imagenRandom}.png`);
    const path = document.querySelector('#gallery img').getAttribute('data-src');
    document.querySelector('#gallery img').setAttribute('src', `${path}/ilustracion_${imagenRandom}.png`);

    //? Password Handler
    const showPwdElement = document.querySelector('#show-pwd-icon');

    const showPassword = function () {
        const pwdElement = document.querySelector('#password');
        const pwdType = pwdElement.getAttribute('type');
        if (pwdType == 'password') {
            pwdElement.setAttribute('type', 'text');
            showPwdElement.style = 'color: var(--color-black-4); transform: scale(0.75);'
            showPwdElement.innerText = 'visibility';
        } else {
            pwdElement.setAttribute('type', 'password');
            showPwdElement.style = 'color: var(--color-black); transform: scale(1);'
            showPwdElement.innerText = 'visibility_off';
        }
    }
    // PC Handlers
    showPwdElement.addEventListener('mouseup', showPassword);
    showPwdElement.addEventListener('mousedown', showPassword);
    showPwdElement.addEventListener('mouseout', () => {
        const pwdElement = document.querySelector('#password');
        const pwdType = pwdElement.getAttribute('type');
        if (pwdType == 'text') showPassword();
    });
    // Mobile Handlers
    showPwdElement.addEventListener('touchstart', showPassword);
    showPwdElement.addEventListener('touchend', showPassword);
}