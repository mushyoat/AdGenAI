from django.urls import path
from . import views

app_name='gendata'
urlpatterns = [
    path('', views.index, name="index"),
    path('prompt', views.prompt, name='prompt'),
    path('rsa', views.rsa, name='rsa')
]