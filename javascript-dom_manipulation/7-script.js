const myList = document.getElementById('list_movies');
fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then(response => response.json())
  .then(data => data.results.forEach( elem => {
    const newElem = document.createElement('li');
    const textNode = document.createTextNode(elem.title);
    newElem.appendChild(textNode);
    myList.appendChild(newElem);
  }))
  .catch(error => console.error(error));
