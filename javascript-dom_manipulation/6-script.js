const div = document.getElementById('character');
fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
  .then(response => response.json())
  .then(data => div.textContent = data.name)
  .catch(error => console.error(error));
