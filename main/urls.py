from django.urls import path
from .views import index, content, about
from core.views import search
app_name = 'main'


urlpatterns = [
    path('', index, name='home'),
    path('contact-us/', content, name='contact'),
    path('about-us/', about, name='about'),
    path('search/', search, name='search'),
]
