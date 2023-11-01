$(document).ready(function() {
	// Make an AJAX GET request to the provided URL
	$.get("https://swapi-api.alx-tools.com/api/films/?format=json", function(data) {
		$.each(data.results, function(index, movie) {
			$("#list_movies").append("<li>"+ movie.title + "</li>");
		});
	});
});
