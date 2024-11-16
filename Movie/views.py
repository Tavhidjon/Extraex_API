from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateAPIView,DestroyAPIView






class MovieListCreateView(ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class=MovieSerializer



class MovieUpdateView(RetrieveUpdateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer



class MovieDeleteView(DestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer






class ActorListCreateView(ListCreateAPIView):
    queryset = Actor.objects.all()
    serializer_class=ActorSerializer



class ActorUpdateView(RetrieveUpdateAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer



class ActorDeleteView(DestroyAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer





class MovieCastListCreateView(ListCreateAPIView):
    queryset = MovieCast.objects.all()
    serializer_class=MovieCastSerializer



class MovieCastUpdateView(RetrieveUpdateAPIView):
    queryset = MovieCast.objects.all()
    serializer_class = MovieCastSerializer



class MovieCastDeleteView(DestroyAPIView):
    queryset = MovieCast.objects.all()
    serializer_class = MovieCastSerializer

    




class GenresCastListCreateView(ListCreateAPIView):
    queryset = Genres.objects.all()
    serializer_class=GenresSerializer



class GenresUpdateView(RetrieveUpdateAPIView):
    queryset = Genres.objects.all()
    serializer_class = GenresSerializer



class GenresDeleteView(DestroyAPIView):
    queryset = Genres.objects.all()
    serializer_class = GenresSerializer

    






class DirectorCastListCreateView(ListCreateAPIView):
    queryset = Director.objects.all()
    serializer_class=DirectorSerializer



class DirectorUpdateView(RetrieveUpdateAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer



class DirectorDeleteView(DestroyAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer


