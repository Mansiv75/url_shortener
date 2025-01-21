import random 
import string
from .models import URL
import redis
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
# Create your views here.
from django.conf import settings
from django.utils.timezone import now

redis_client = redis.StrictRedis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, decode_responses=True)

def generate_shortened_url(request):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=10))

def shorten_url(request):
    if request.method == 'POST':
        original_url = request.POST.get('url')

        #check if url already exists
        existing_url = URL.objects.filter(original_url=original_url).first()
        if existing_url:
            shortened_url=existing_url.shortened_url
#             #if existing_url := URL.objects.filter(
# +            original_url=original_url
# +        ).first():
        else:
            shortened_url=generate_shortened_url()
            URL.objects.create(original_url=original_url, shortened_url=shortened_url)

            # save to redis for fast lookup
            redis_client.set(shortened_url, original_url)
            redis_client.set(f"{shortened_url}:hits",0) #initialize it to 0
            redis_client.set(f"{shortened_url}:last_accessed", "Never") #initialize it to never

        return JsonResponse({'shortened_url': shortened_url})
    return JsonResponse(request, 'shortener/shorten_url.html')

def redirect_to_original(request, shortened_url):
    original_url = redis_client.get(shortened_url)
    if original_url:
        redis_client.incr(f"{shortened_url}:hits") #increment hit counter
        redis_client.set(f"{shortened_url}:last_accessed", now().isoformat()) #update last accessed IP
        return redirect(original_url)
    else:
        return HttpResponse("URL not found", status=404)