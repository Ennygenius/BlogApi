from django.shortcuts import render
from rest_framework import viewsets
from .models import Blog
from .serializers import BlogSerializers
from rest_framework.response import Response as response
from django.shortcuts import get_object_or_404

# Create your views here.
class GetCreateBlog(viewsets.ModelViewSet):
    serializer_class = BlogSerializers
    queryset = Blog.objects.all()
    

    def perform_create(self, serializer):
        # Automatically set the user field to the currently logged-in user
        serializer.save(user=self.request.user)
  