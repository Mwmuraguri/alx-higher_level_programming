$(document).ready(function() {
  $("#btn_translate").click(function() {
    const languageCode = $("#language_code").val();
    const url = `https://www.fourtonfish.com/hellosalut/hello/?lang=${languageCode}`;

    // Make an AJAX GET request to the API
    $.get(url, function(data) {
      // Display the translation in the DIV#hello
      $("#hello").text(data.hello);
    });
  });
});
