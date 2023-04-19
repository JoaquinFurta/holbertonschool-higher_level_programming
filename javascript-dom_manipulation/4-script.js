const myList = document.getElementsByClassName('my_list');
const x = document.getElementById('add_item');
x.onclick = () => {
  const newElem = document.createElement('li');
  const textNode = document.createTextNode('item');
  newElem.appendChild(textNode);
  myList[0].appendChild(newElem);
};
