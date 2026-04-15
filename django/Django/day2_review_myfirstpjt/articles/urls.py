from django.urls import path
from . import views

urlpatterns = [
    path("samsung01/", views.index, name='index'),

]
