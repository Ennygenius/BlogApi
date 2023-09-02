from django.urls import path
from .views import GetCreateBlog
from rest_framework.routers import DefaultRouter

routers =DefaultRouter()

routers.register('', GetCreateBlog, basename='Post' )

urlpatterns = routers.urls