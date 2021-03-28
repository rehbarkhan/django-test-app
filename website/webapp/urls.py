from django.urls import path
from . import views

urlpatterns = [
    path('', views.Root,name='root'),
    path('home/',views.Home,name='home'),
    path('contact/',views.Contact,name='contact'),
    path('news/',views.News,name='news'),
]
