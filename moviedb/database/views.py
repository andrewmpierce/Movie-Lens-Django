from django.shortcuts import render, redirect, render_to_response
from django.db.models import Avg, Count
from .models import Movie, Rater, Rating
from users.forms import RatingForm
from django import forms
from datetime import datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.



def movie_detail(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    if request.method == 'POST':
        if request.user.is_authenticated():
                form = RatingForm(request.POST)
                if form.is_valid():
                        try:
                            rating = Rating.objects.get(rater=request.user.rater, movie=movie)
                            if request.POST['rating'] == '6':
                                del rating
                            else:
                                rating.stars=request.POST['rating']
                                rating.text=request.POST['text']
                                rating.timestamp=datetime.now()
                                rating.save()
                        except:
                             Rating.create_rating(movie=movie, rater=request.user.rater, stars=request.POST['rating'], text=request.POST['text'], timestamp=datetime.now().strftime('%Y-%m-%d %H:%M'))
        else:
            return redirect("http://127.0.0.1:8000/users/login")
    return render(request,
                  'database/movie_detail.html',
                  {'movie':movie})


def rater_detail(request, rater_id):
    rater = Rater.objects.get(pk=rater_id)
    ratings = []
    for rating in rater.rating_set.all():
        ratings.append({'movie':rating.movie,
                        'stars': rating.stars})
    return render(request,
                  'database/rater_detail.html',
                  {'rater': rater,
                  'ratings': ratings})


def top_movies(request):
    popular_movies = Movie.objects.all().annotate(num_ratings=Count('rating')) \
                                  .filter(num_ratings__gte=50)

    movies = popular_movies.annotate(Avg('rating__stars')) \
                           .order_by('-rating__stars__avg')[:20]

    return render(request,
                  'database/top_twenty.html',
                  {'movies': movies})

def most_viewed(request):
    popular_movies = Movie.objects.all().annotate(num_ratings=Count('rating')) \
                                      .order_by('-num_ratings')[:20]
    return render(request,
                  'database/most_pop.html',
                  {'popular_movies': popular_movies,
                  })


def list_movies(request):
    top_movies = popular_movies = Movie.objects.all().annotate(num_ratings=Count('rating')) \
                                  .filter(num_ratings__gte=50)

    top_movies = popular_movies.annotate(Avg('rating__stars')) \
                           .order_by('-rating__stars__avg')
    paginator = Paginator(top_movies, 20)
    page = request.GET.get('page')
    try:
        movies = paginator.page('page')
    except PageNotAnInteger:
        movies = paginator.page(1)
    except EmptyPage:
        movies = paginator.page(paginator.num_pages)
    return render_to_response('database/list_movies.html', {"movies":movies})
