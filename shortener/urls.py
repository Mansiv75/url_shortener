from django.urls import path
from .views import test_redis

urlpatterns = [
    path('test_redis/', test_redis, name='test_redis'),
]