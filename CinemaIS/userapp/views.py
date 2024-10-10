from django.contrib.auth import logout, authenticate, login
from django.http import HttpResponse
from django.shortcuts import redirect, render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer
from mainapp.models import TopMovie, SadMovie, FunMovie, ActMovie, OccPlace, Session, Room


@api_view(['GET'])
def get_users_api(request):
    if request.user.is_superuser:
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    return HttpResponse("У Вас отсутствуют права на такой запрос", status=403)


@api_view(['GET'])
def get_user_api(request):
    if request.user.is_superuser:
        username = request.GET.get('username')
        user = User.objects.filter(username=username).first()
        serializer = UserSerializer(user)
        return Response(serializer.data)
    return HttpResponse("У Вас отсутствуют права на такой запрос", status=403)


def logout_page(request):
    logout(request)
    return redirect('home')


def login_page(request):
    if request.method == 'GET':
        return render(request, 'login.html')

    data = request.POST
    user = authenticate(request, username=data.get('username'), password=data.get('password'))
    if user is None:
        return render(request, 'login.html', {'error': 'Неудачная попытка входа'})
    login(request, user)
    return redirect('profile')


def reg_page(request):
    if request.method == "GET":
        return render(request, "reg.html")

    data = request.POST
    password1, password2 = data.get("password1"), data.get("password2")
    if password1 != password2:
        return render(request, "reg.html", {'error': 'Пароли должны совпадать'}, status=401)

    try:
        new = User()
        new.create_user(**{
            'username': data.get('username'),
            'phone': data.get('phone'),
            'email': data.get('email'),
            'password': password1
        })
        user = authenticate(request, username=data['username'], password=password1)
        login(request, user)
        return redirect('profile')
    except Exception:
        return render(request, "reg.html", {'error': 'Такой пользователь уже существует'}, status=401)


def profile(request):
    if request.method == "GET":
        if request.user.is_anonymous:
            return redirect('login')
        top_movies = list(TopMovie.objects.all())
        act_movies = list(ActMovie.objects.all())
        sad_movies = list(SadMovie.objects.all())
        fun_movies = list(FunMovie.objects.all())

        occ_places = sorted(list(OccPlace.objects.filter(user_id=request.user.id).all()))
        sessions = set()
        for occ_place in occ_places:
            sessions.add(Session.objects.filter(id=occ_place.session_id).first())
        sessions = sorted(list(sessions))
        rooms = set()
        for session in sessions:
            rooms.add(Room.objects.filter(id=session.room_id).first())
        rooms = list(rooms)
        return render(request, 'profile.html', {'user': request.user,
                                                'top_movies': top_movies,
                                                'act_movies': act_movies,
                                                'sad_movies': sad_movies,
                                                'fun_movies': fun_movies,
                                                'rooms': rooms,
                                                'sessions': sessions,
                                                'occ_places': occ_places})

    request.user.avatar = request.FILES['new_avatar']
    request.user.save()
    request.user.update_avatar()
    return redirect('profile')
