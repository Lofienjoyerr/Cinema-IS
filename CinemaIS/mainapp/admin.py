from django.contrib import admin
from .models import Movie, Room, Session, OccPlace, TopMovie, ActMovie, SadMovie, FunMovie

admin.site.register(Movie)
admin.site.register(Room)
admin.site.register(Session)
admin.site.register(OccPlace)
admin.site.register(TopMovie)
admin.site.register(ActMovie)
admin.site.register(SadMovie)
admin.site.register(FunMovie)
