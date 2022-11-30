from django.urls import path
from .views import createView, filme

urlpatterns = [
    path('create',createView),
    path('filme',filme,name='filme'),
]