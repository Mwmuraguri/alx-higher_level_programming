$(document).ready(function() {
  // Add a click event listener to the div with id "update_header"
  $("#update_header").click(function() {
    // Use jQuery to update the text of the header element to "New Header!!!"
    $("header").text("New Header!!!");
  });
});

