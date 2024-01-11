$(function () {
  const headerElement = $('.my_list');
  const addItem = $('#add_item');

  addItem.click(function () {
    headerElement.prepend('<li>Item</li>');
  });
});
