$(function () {
  const headerElement = $('header');
  const updateHeader = $('#update_header');

  updateHeader.click(function () {
    headerElement.text('New Header!!!');
  });
});
