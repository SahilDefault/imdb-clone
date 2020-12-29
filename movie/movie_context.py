from .models import Movie

def slider_movies(requests):
    movies = Movie.objects.last()
    return {'slider_movie': movies}