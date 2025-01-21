from django.urls import path
from .views import shorten_url, redirect_to_original, url_analytics

urlpatterns = [
    path('', shorten_url, name='shorten_url'),
    path('<str:shortened_url>/', redirect_to_original, name='redirect_to_original'),
    path('<str:shortened_url>/analytics/', url_analytics, name='analytics'),
]