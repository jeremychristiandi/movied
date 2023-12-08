from django.urls import path

from movies import views

urlpatterns = [
    path('movies/', views.AllMovies.as_view()),
    path('movies/<slug:movie_slug>/', views.MovieDetail.as_view()),
]