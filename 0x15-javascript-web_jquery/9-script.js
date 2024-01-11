const url = 'https://hellosalut.stefanbohacek.dev/?lang=de';
$.get(url, function (data) {
  $('#hello').text(data.hello);
});
