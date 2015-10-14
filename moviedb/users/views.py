from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import UserForm
from .models import Profile
from django.views.generic import DetailView
from django.views.generic import CreateView, UpdateView
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from database.models import Rater, Movie, Rating
from database.views import *
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import UserForm, ProfileForm
from django.contrib import messages

# Create your views here.

def user_register(request):
    form = UserForm(request.POST)
    if form.is_valid():
        user = form.save()
        password = user.password
        user.set_password(password)
        user.save()
        profile = Profile(user=user, favorite_movie= 'Toy Story')
        profile.save()
        user = authenticate(username=user,
                             password=password)
        user_r = User.objects.get(username=user)
        Rater.objects.create(user=user_r,
                            gender=request.POST['gender'],
                            age=request.POST['age'],
                            zipcode=request.POST['zipcode'],
                            occupation=request.POST['occupation'])
        ratings = []
        try:
            for rating in user_r.rater.rating_set.all():
                ratings.append({'movie':rating.movie,
                                'stars': rating.stars})
        except:
            pass
        login(request, user)
        return render(request,
                    'users/profile_edit.html',
                    {'rater': user_r,
                    'ratings': ratings})
    else:
        form = UserForm()
    return render(request, 'users/register.html',
                  {'form':form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        user_r = User.objects.get(username=username)
        rater = Rater.objects.get(pk=user_r.pk)
        profile = user_r.profile
        ratings = []
        for rating in user_r.rater.rating_set.all():
            ratings.append({'movie':rating.movie,
                        'stars': rating.stars})
        #import pdb; pdb.set_trace()
        if request.user.is_active:
            login(request, user)
            # return redirect(reverse('profile_edit')+"?rater={}&profile={}&rating={}".format(rater, profile, ratings))
            # # , kwargs={'rater':rater,
            # # 'profile': profile,
            # # 'rating': ratings}))
            return render(request,
                        'users/profile_edit.html',
                        {'rater':rater,
                        'profile': profile,
                        'ratings': ratings})
        else:
            return render(request,
                      'users/login.html',
                      {'failed':True,
                      'username':username})
    return render(request, 'users/login.html')


def user_logout(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        logout(request, user)
    return redirect('database/top_twenty.html')


# def view_profile(request, rater_id):
#     rater = Rater.objects.get(pk=rater_id)
#     ratings = []
#     for rating in rater.rating_set.all():
#         ratings.append({'movie':rating.movie,
#                     'stars': rating.stars})
#     return render(request,
#                 'users/profile_detail.html',
#                 {'rater':rater,
#                 'ratings': ratings})

@login_required
def edit_profile(request):
    #import pdb; pdb.set_trace()
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = Profile(user=request.user)

    if request.method == 'GET':
        profile_form = ProfileForm(instance=profile)
    if request.method == 'POST':
        rating = Rating.objects.get(rater=request.profile.user.rater, movie= request.POST['movie'])
        if request.POST['rating'] == 'delete':
            del rating
        else:
            profile_form = ProfileForm(instance=profile, data=request.POST)
            rating.stars=request.POST['rating']
            rating.text=request.POST['text']
            rating.timestamp=datetime.now()
            rating.save()
            profile_form.save()
            messages.add_message(request, messages.SUCCESS, 'Your profile has been updated')

    return render(request, 'users/profile_edit.html')
