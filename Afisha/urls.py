from django.contrib import admin
from django.urls import path
from movie_app.views import directors_list_api_view, movies_list_api_view, review_list_api_view, director_detail_list_api_view, movie_detail_list_api_view, review_detail_list_api_view, get_movie_review_list_api_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/movies/reviews/', get_movie_review_list_api_view),
    path('api/v1/directors/', directors_list_api_view),
    path('api/v1/directors/<int:id>/', director_detail_list_api_view),
    path('api/v1/movies/', movies_list_api_view),
    path('api/v1/movies/<int:id>/', movie_detail_list_api_view),
    path('api/v1/reviews/', review_list_api_view),
    path('api/v1/reviews/<int:id>/', review_detail_list_api_view),

]
