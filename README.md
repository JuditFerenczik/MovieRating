# MovieRating
Flask application for rating movies

Simple Flask web application to store my favourite movies. List all of the already entered movies ordered by according to their ratings. It is possible to add movies by clicking
on the "Add movies" button. After entering the name of the movie we want to add it uses tmdb-api to look for the matching result movies. We got a list from them and 
by selecting the correct movie
it adds its data to the database. After that it redirects to the edit page where we can edit/add our review and rating of that movie.
Saving this we get back to the home page where the order of the movies are updated according to the newly added movie.
