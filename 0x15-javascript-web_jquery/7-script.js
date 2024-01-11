const url = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';
const characterElement = $('#character');

$.get(url, function (data) {
  characterElement.text(data.name);
});
