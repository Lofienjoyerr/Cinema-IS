import os
from django.core.validators import FileExtensionValidator
from django.db import models
from userapp.models import User


def movie_directory_path(instance, filename):
    path = 'mainapp/movie_{0}/img.{1}'.format(instance.id, filename.split('.')[-1])
    if instance.id is None:
        if len(Movie.objects.all()) > 0:
            path = 'mainapp/movie_{0}/img.{1}'.format(Movie.objects.latest('id').id + 1, filename.split('.')[-1])
        else:
            path = 'mainapp/movie_{0}/img.{1}'.format(1, filename.split('.')[-1])

    if instance.id is not None:
        old_path = instance.img.path.replace('\\', '/').split('/')
        old_path = "/".join(old_path[:-1])
        if os.path.exists(old_path + '/' + path):
            os.remove(old_path + '/' + path)
    return path


def movie_desc_directory_path(instance, filename):
    path = 'mainapp/movie_{0}/desc_img.{1}'.format(instance.id, filename.split('.')[-1])
    if instance.id is None:
        if len(Movie.objects.all()) > 0:
            path = 'mainapp/movie_{0}/desc_img.{1}'.format(Movie.objects.latest('id').id + 1, filename.split('.')[-1])
        else:
            path = 'mainapp/movie_{0}/desc_img.{1}'.format(1, filename.split('.')[-1])

    if instance.id is not None:
        old_path = instance.desc_img.path.replace('\\', '/').split('/')
        old_path = "/".join(old_path[:-1])
        if os.path.exists(old_path + '/' + path):
            os.remove(old_path + '/' + path)
    return path


class Movie(models.Model):
    img = models.ImageField(upload_to=movie_directory_path,
                            default='userapp/default_avatar.webp',
                            validators=[FileExtensionValidator(['webp'])])
    desc_img = models.ImageField(upload_to=movie_desc_directory_path,
                                 default='userapp/default_avatar.webp',
                                 validators=[FileExtensionValidator(['webp'])])
    name = models.CharField(max_length=50)
    info = models.TextField()
    desc = models.TextField()
    genre = models.CharField(max_length=30, default='non-genre')

    def __str__(self):
        return self.name


class Room(models.Model):
    name = models.CharField(max_length=50)
    is_vip = models.BooleanField()

    def __str__(self):
        return self.name


class Session(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    datetime = models.DateTimeField()
    format = models.CharField(max_length=2, help_text='2D or 3D')

    def __str__(self):
        return self.movie.name + " " + self.room.name + " " + self.datetime.strftime("%B %d")

    def __lt__(self, other):
        return self.datetime < other.datetime


class OccPlace(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    row = models.PositiveIntegerField()
    seat = models.PositiveIntegerField()

    def __str__(self):
        return f"Ряд: {self.row}\n Место: {self.seat}"

    def __lt__(self, other):
        return (self.row, self.seat) <= (other.row, other.seat)


class TopMovie(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return self.movie.name


class ActMovie(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return self.movie.name


class SadMovie(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return self.movie.name


class FunMovie(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return self.movie.name
