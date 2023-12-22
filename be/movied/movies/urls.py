from django.urls import path

from movies import views

urlpatterns = [
    path('movies/', views.AllMovies.as_view()),
    path('movies/genres/', views.AllGenres.as_view()),
    path('actors/', views.AllActors.as_view()),
    path('movies/<slug:movie_slug>/', views.MovieDetail.as_view()),
]