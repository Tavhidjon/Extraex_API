from django.urls import path
from .views import *

urlpatterns = [
    path('movies/', MovieListCreateView.as_view()),
    path('movies/delete/<int:pk>/', MovieDeleteView.as_view()), 
    path('movies/update/<int:pk>/', MovieUpdateView.as_view()), 

    path('actor/', ActorListCreateView.as_view()), 
    path('actor/delete/<int:pk>/', ActorUpdateView.as_view()), 
    path('actor/update/<int:pk>/', ActorDeleteView.as_view()), 


    path('MovieCast/', MovieCastListCreateView.as_view()), 
    path('MovieCast/delete/<int:pk>/', MovieCastUpdateView.as_view()), 
    path('MovieCast/update/<int:pk>/', MovieCastDeleteView.as_view()), 


    path('Genres/', GenresCastListCreateView.as_view()), 
    path('Genres/delete/<int:pk>/', GenresUpdateView.as_view()), 
    path('Genres/update/<int:pk>/', GenresDeleteView.as_view()), 

    path('Director', DirectorCastListCreateView.as_view()), 
    path('Director/delete/<int:pk>/', DirectorUpdateView.as_view()), 
    path('Director/update/<int:pk>/', DirectorDeleteView.as_view()), 







]