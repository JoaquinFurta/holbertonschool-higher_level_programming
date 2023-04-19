document.addEventListener('DOMContentLoaded', function() {
  const div = document.getElementById('hello');
  fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
    .then(response => response.json())
    .then(data => div.textContent = data.hello)
    .catch(error => console.error(error));
});
