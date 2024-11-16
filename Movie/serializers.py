from rest_framework.serializers import ModelSerializer
from .models import *


class MovieSerializer(ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class ActorSerializer(ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'



class MovieCastSerializer(ModelSerializer):
    class Meta:
        model= MovieCast
        fields = '__all__'




class GenresSerializer(ModelSerializer):
    class Meta:
        model= Genres
        fields = '__all__'




class DirectorSerializer(ModelSerializer):
    class Meta:
        model= Director
        fields = '__all__'



