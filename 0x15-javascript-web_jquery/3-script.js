$(document).ready(function() {
  // Add a click event listener to the div with id "red_header"
  $("#red_header").click(function() {
    // Use jQuery to add the "red" class to the header element
    $("header").addClass("red");
  });
});
