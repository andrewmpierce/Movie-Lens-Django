# Movie Lens Online

This is a Django project designed to allow users to rater movies from the Movie Lens
database and has a very large number of fake users present to represent the existing
ratings from the database. Users can register, rate movies, look at other user's pages
and movie pages, see a most popular list.

To run: Install the requirements by running pip install -r 'requirements.txt' from
your terminal. You will then need to run python manage.py runserver to get a local
host to view the site on. This will provide a web address and you will be able to
view the system.


Currently there is no homepage.
/most_popular -- most rated movies page
/top_twenty -- top twenty highest average ratings
/movies/movie_id -- movie page
/rater/rater_id -- user public page
/users/login
/users/register
/users/logout
/users/profile -- private profile page
