from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'login$', views.user_login, name='login'),
    url(r'^logout$', views.user_logout, name='logout'),
    url(r'^register$', views.user_register, name='register'),
    url(r'^profile/(?P<user_id>\d+)$', views.edit_profile, name='profile_edit'),
    url(r'^profile/edit/(?P<movie_id>\d+)$', views.edit_rating, name='edit_rating')

]
