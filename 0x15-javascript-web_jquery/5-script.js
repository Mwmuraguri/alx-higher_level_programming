$(document).ready(function () {
// Add a click event listener to the div with id "add_item"
  $('#add_item').click(function () {
    $('.my_list').append('<li>Item</li>');
  });
});
