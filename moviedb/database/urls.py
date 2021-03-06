from django.conf.urls import url
from database.views import HomePageView

from . import views

urlpatterns = [
    url(r'top', views.top_movies, name='top_twenty'),
    url(r'most', views.most_viewed, name='most_popular'),
    url(r'^movies/(?P<movie_id>\d+)$', views.movie_detail, name='movie_detail'),
    url(r'^rater/(?P<rater_id>\d+)$', views.rater_detail, name='rater_detail'),
    url(r'^list/', views.list_movies, name='list_movies'),
    url(r'^$', HomePageView.as_view(), name='home')

]
