const menuButton = document.querySelector('.menu-button');
const menu = document.querySelector('.menu');

menuButton.addEventListener('click', () => {
    menu.classList.toggle('menu-open');
});

const backButton = document.querySelector('.back-button');

backButton.addEventListener('click', () => {
    menu.classList.remove('menu-open');
});

