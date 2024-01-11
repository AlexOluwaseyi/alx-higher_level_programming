const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';
const titleElement = $('#list_movies');

$.get(url, function (data) {
  data.results.forEach(film => {
    titleElement.append('<li>' + film.title + '</li>');
  });
});
