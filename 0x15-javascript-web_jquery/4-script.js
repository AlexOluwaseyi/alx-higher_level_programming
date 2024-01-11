$(function () {
  const headerElement = $('header');
  const toggleHeader = $('#toggle_header');

  toggleHeader.click(function () {
    headerElement.toggleClass('red green');
  });
});
