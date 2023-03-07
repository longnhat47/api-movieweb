from .models import *
from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField, SerializerMethodField
from accounts.serializers import UserCommentSerializer
import requests

class CategorySerializer(ModelSerializer):
    link = HyperlinkedIdentityField(
        view_name='category-detail',
        lookup_field = 'id'
    )
    class Meta:
        model = Category
        fields = ['id', 'name', 'link']


class CountrySerializer(ModelSerializer):
    class Meta:
        model = Country
        fields = ['id', 'name']


class MovieSerializer(ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'category', 'country', 'name',
                  'thumbnail', 'created_at', 'status']


class MovieDetailSerializer(ModelSerializer):
    link = HyperlinkedIdentityField(
        view_name='movie-detail',
        lookup_field = 'id'
    )
    comment = SerializerMethodField()
    class Meta:
        model = Movie
        fields = ['id', 'link', 'category', 'country', 'name', 'thumbnail',
                  'description', 'video', 'comment', 'created_at', 'status']
        extra_kwargs = {
            'status': {'read_only': True}
        }

    def get_comment(self, obj):
        comment = Comment.objects.filter(movie= obj.id)
        return CommentSerializer(instance=comment, many=True).data


class CommentSerializer(ModelSerializer):
    user = SerializerMethodField()
    class Meta:
        model = Comment
        fields = ['id', 'movie', 'user', 'content', 'created_at']

    def get_user(self, obj):
        u = User.objects.filter(id = obj.user.id)
        return (UserCommentSerializer(instance=u, many=True).data)[0]