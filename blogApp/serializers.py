from rest_framework import serializers
from .models import Blog

class BlogSerializers(serializers.ModelSerializer):
    user_username = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Blog
        fields = ['id', 'title', 'sub_title', 'body', 'sub_body', 'date_created', 'footer', 'reading_time', 'img', 'user_username']