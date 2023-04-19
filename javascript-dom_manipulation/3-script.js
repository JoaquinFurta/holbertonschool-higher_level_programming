const header = document.querySelector('header');
const x = document.getElementById('toggle_header');
x.onclick = () => {
  header.classList.toggle('green');
  header.classList.toggle('red');
};
