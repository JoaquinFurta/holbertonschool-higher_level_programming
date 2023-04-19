const header = document.querySelector('header');
const x = document.getElementById('update_header');
x.onclick = () => {
  header.textContent = 'New Header!!!';
};
