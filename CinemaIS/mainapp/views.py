from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import TopMovie, ActMovie, SadMovie, FunMovie, Movie, Session, Room, OccPlace
import json, math


def home(request):
    top_movies = list(TopMovie.objects.all())
    act_movies = list(ActMovie.objects.all())
    sad_movies = list(SadMovie.objects.all())
    fun_movies = list(FunMovie.objects.all())
    return render(request, 'home.html', {'user': request.user,
                                         'top_movies': top_movies,
                                         'act_movies': act_movies,
                                         'sad_movies': sad_movies,
                                         'fun_movies': fun_movies})


def movie_page(request):
    movie = Movie.objects.filter(id=request.GET.get('id')).first()
    top_movies = list(TopMovie.objects.all())
    act_movies = list(ActMovie.objects.all())
    sad_movies = list(SadMovie.objects.all())
    fun_movies = list(FunMovie.objects.all())
    sessions = list(Session.objects.filter(movie=movie).all())
    rooms = list(Room.objects.all())
    return render(request, 'movie.html', {'user': request.user,
                                          'movie': movie,
                                          'top_movies': top_movies,
                                          'act_movies': act_movies,
                                          'sad_movies': sad_movies,
                                          'fun_movies': fun_movies,
                                          'sessions': sessions,
                                          'rooms': rooms})


def session_page(request):
    if request.method == "POST":
        if request.user.is_anonymous:
            return redirect('login')


        data = json.loads(request.body.decode("utf-8"))
        user = request.user
        session = Session.objects.filter(id=data.get('sessionId')).first()
        occ_places = data.get('occ_places')
        for occ_place in occ_places:
            occ_place += 1
            new_occ_place = OccPlace()
            new_occ_place.user = user
            new_occ_place.session = session
            new_occ_place.row = math.ceil(occ_place / 22)
            new_occ_place.seat = occ_place
            new_occ_place.seat -= (new_occ_place.row - 1) * 22
            new_occ_place.save()
        return redirect(f'/movie?id={session.movie_id}')

    session = Session.objects.filter(id=request.GET.get('id')).first()
    occ_places = [[occ_place.row, occ_place.seat] for occ_place in OccPlace.objects.filter(session=session).all()]
    return render(request, 'session.html', {'user': request.user,
                                            'session': session,
                                            'occ_places': occ_places,
                                            'range11': range(11),
                                            'range24': range(24)})
