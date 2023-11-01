$(document).ready(function() {
  // Make an AJAX GET request to the provided URL
  $.get("https://hellosalut.stefanbohacek.dev/?lang=fr", function(data) {
    // Display the fetched translation in the DIV#hello
    $("#hello").text(data.hello);
  });
});
