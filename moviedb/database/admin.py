from django.contrib import admin
from .models import Movie, Rater, Rating


# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    list_display = ['movie_id', 'title', 'average_rating']

class RaterAdmin(admin.ModelAdmin):
    list_display = ['id', 'age', 'gender', 'occupation', 'zipcode']

class RatingAdmin(admin.ModelAdmin):
    list_display = ['rater', 'movie', 'stars', 'text', 'timestamp']

admin.site.register(Movie, MovieAdmin)
admin.site.register(Rater, RaterAdmin)
admin.site.register(Rating, RatingAdmin)
