const toggleButtons = document.getElementsByClassName('toggle')[0]
const navLink = document.getElementsByClassName('nav-links')[0]

toggleButtons.addEventListener('click', () => {
    navLink.classList.toggle('active')
});