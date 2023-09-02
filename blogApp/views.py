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

    # def list(self, request):
    #     serializer = self.serializer(instance=self.queryset, many=True )
    #     return response(data=serializer.data)


    # def retrieve(self, request, pk):
    #     blog = get_object_or_404(self.queryset, pk=pk)
    #     serializer = self.serializer(blog)
    #     return response(serializer.data)

