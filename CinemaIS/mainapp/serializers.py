from rest_framework import serializers
from .models import Movie, Room, Session, OccPlace, TopMovie, ActMovie, SadMovie, FunMovie


class MovieSerializer(serializers.Serializer):
    class Meta:
        model = Movie
        fields = ["id", "name", "info", "desc", "img", "desc_img"]

    def to_representation(self, instance: Movie):
        return {
            "id": instance.id,
            "name": instance.name,
            "info": instance.info,
            "desc": instance.desc,
            "img": instance.img,
            "desc_img": instance.desc_img
        }


class RoomSerializer(serializers.Serializer):
    class Meta:
        model = Room
        fields = ["id", "name", "is_vip"]

    def to_representation(self, instance: Movie):
        return {
            "id": instance.id,
            "name": instance.name,
            "is_vip": instance.is_vip,
        }


class SessionSerializer(serializers.Serializer):
    class Meta:
        model = Session
        fields = ["id", "room_id", "movie_id", "price", "datetime", "format"]

    def to_representation(self, instance: Session):
        return {
            "id": instance.id,
            "room_id": instance.room_id,
            "movie_id": instance.movie_id,
            "price": instance.price,
            "datetime": instance.datetime,
            "format": instance.format
        }


class OccPlaceSerializer(serializers.Serializer):
    class Meta:
        model = OccPlace
        fields = ["id", "user_id", "session_id", "row", "seat"]

    def to_representation(self, instance: OccPlace):
        return {
            "id": instance.id,
            "user_id": instance.user_id,
            "session_id": instance.session_id,
            "row": instance.row,
            "seat": instance.seat,
        }


class TopMovieSerializer(serializers.Serializer):
    class Meta:
        model = TopMovie
        fields = ["id", "movie_id"]

    def to_representation(self, instance: TopMovie):
        return {
            "id": instance.id,
            "movie_id": instance.movie_id,
        }


class ActMovieSerializer(serializers.Serializer):
    class Meta:
        model = ActMovie
        fields = ["id", "movie_id"]

    def to_representation(self, instance: ActMovie):
        return {
            "id": instance.id,
            "movie_id": instance.movie_id,
        }


class SadMovieSerializer(serializers.Serializer):
    class Meta:
        model = SadMovie
        fields = ["id", "movie_id"]

    def to_representation(self, instance: SadMovie):
        return {
            "id": instance.id,
            "movie_id": instance.movie_id,
        }


class FunMovieSerializer(serializers.Serializer):
    class Meta:
        model = FunMovie
        fields = ["id", "movie_id"]

    def to_representation(self, instance: FunMovie):
        return {
            "id": instance.id,
            "movie_id": instance.movie_id,
        }
