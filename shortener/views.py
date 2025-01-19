import redis
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.conf import settings

redis_client = redis.StrictRedis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, decode_responses=True)

def test_redis(request):
    redis_client.set('greeting', 'Hello, from Redis!')
    value = redis_client.get('greeting')
    return HttpResponse('Hello, from Redis!')