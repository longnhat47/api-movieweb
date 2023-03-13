from django.shortcuts import render
from rest_framework import status, mixins
from rest_framework.response import Response
from rest_framework.generics import (
    RetrieveAPIView, 
    ListAPIView,
    CreateAPIView,
    UpdateAPIView,
    DestroyAPIView,
    RetrieveUpdateDestroyAPIView)
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly

from .models import *
from .serializers import *
# Create your views here.

# CATEGORY VIEWS----------------------------------------------------------------
class CreateCategoryView(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated, IsAdminUser]


class ListCategoryView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]



class CategoryRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

    lookup_field = 'id'


# COUNTRY VIEWS----------------------------------------------------------------
class ListCountryView(ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class CreateCountryView(CreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = [IsAuthenticated, IsAdminUser]


class CountryRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

    lookup_field = 'id'


# MOVIE VIEWS----------------------------------------------------------------

# class ListCreateMovieView(GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
#     queryset = Movie.objects.all()
#     serializer_class = MovieSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)


class ListMovieView(ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class CreateMovieView(CreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieCreateSerializer
    permission_classes = [IsAdminUser]


class MovieRetrieveView(RetrieveAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieDetailSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticatedOrReadOnly]
    



class MovieUpdateDeleteView(UpdateAPIView, DestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieDetailSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticated, IsAdminUser]


class MovieUpdateView(UpdateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieUpdateViewSerializer
    lookup_field = 'id'

    def get_queryset(self):
       data = Movie.objects.all()
       return data
    
    def update(self, request, *args, **kwargs):
        movie = self.get_object()
        print(movie.id)
        movie.views +=1
        movie.save()
        return Response('Update successful', status= status.HTTP_200_OK)


#COMMENT VIEWS----------------------------------------------------------------
class CommentListView(ListAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentCreateView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user = user)
        return super().perform_create(serializer)

class CommentDetailUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    lookup_field = 'id'