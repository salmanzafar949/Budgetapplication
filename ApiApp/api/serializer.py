from rest_framework import serializers
from ApiApp.models import Blog


class Blogserializer(serializers.ModelSerializer):

    class Meta:
        model = Blog
        fields = ('id', 'title', 'body', 'created_at')
