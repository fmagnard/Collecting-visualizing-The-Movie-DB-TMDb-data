FLORE MAGNARD

Q1/ I have tested my code on Windows 10.
My script is written in python. To execute it, double click on the script file.
Once the execution is over a "done" is printed on the terminal. 
(I code using sublime text 3)

I used the discover/movie query to fill in the movie_id_name file, I also add some 
specification as the genre ='878' which is Sciences Fiction, and the release_date.gte 
option which allow me to have only movies that were released after January, 1, 2000.
I also include all_movies.
http://api.themoviedb.org/3/discover/movie?api_key=d48608b6b79437317a0d1430af4a3378&include_all_movies=true&with_genres=878&release_date.gte=2000-01-01&page=%s" % page


To fill the second file, I used the movie/movie_id/similar to find similar movies
according to an id.
"http://api.themoviedb.org/3/movie/%s/similar?api_key=d48608b6b79437317a0d1430af4a3378" % movie_id