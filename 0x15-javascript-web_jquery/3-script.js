$(function () {
  const headerElement = $('header');
  const redDiv = $('#red_header');

  redDiv.click(function () {
    headerElement.addClass('red');
  });
});
