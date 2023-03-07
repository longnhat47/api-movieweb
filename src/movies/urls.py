from django.urls import path
from .views import *

urlpatterns = [
    path('categorie', ListCategoryView.as_view(), name='categories'),
    path('categorie/create', CreateCategoryView.as_view(), name='categorie-create'),
    path('categorie/<int:id>', CategoryRetrieveUpdateDeleteView.as_view(), name='category-detail'),

    path('country', ListCountryView.as_view(), name='country'),
    path('country/create', CreateCountryView.as_view(), name='country-create'),
    path('country/<int:id>', CountryRetrieveUpdateDeleteView.as_view(), name='country-detail'),

    path('movie', ListMovieView.as_view(), name='movies'),
    path('movie/create', CreateMovieView.as_view(), name='movie-create'),
    path('movie/detail/<int:id>', MovieRetrieveView.as_view(), name='movie-detail'),
    path('movie/<int:id>', MovieUpdateDeleteView.as_view(), name='movie-edit'),

    path('comment', CommentListView.as_view(), name='comments'),
    path('comment/create', CommentCreateView.as_view(), name='create-comment'),
    path('comment/<int:id>', CommentDetailUpdateDeleteView.as_view(), name='comment-detail'),

]