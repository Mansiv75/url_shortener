import random 
import string
import json
from .models import URL
import redis
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
# Create your views here.
from django.conf import settings
from django.utils.timezone import now
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect, HttpResponseNotFound


redis_client = redis.StrictRedis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, decode_responses=True)

import logging

logger = logging.getLogger(__name__)


def generate_shortened_url():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=10))

@csrf_exempt
def shorten_url(request):
    if request.method == 'POST':
    
            data = json.loads(request.body)
            original_url = data.get('url')
            
            existing_shortened_url = redis_client.hget('url_mapping', original_url)
            if existing_shortened_url:
                return JsonResponse({'shortened_url': existing_shortened_url.decode('utf-8')})
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

                base_url = request.build_absolute_uri('/')  # e.g., "http://127.0.0.1:8000/"
                full_shortened_url = f"{base_url}{shortened_url}"

                return JsonResponse({'shortened_url': full_shortened_url})
    
    return render(request, 'shortener/shorten_url.html')
def redirect_to_original(request, shortened_url):
    original_url = redis_client.get(shortened_url)
    if original_url:
        redis_client.incr(f"{shortened_url}:hits") #increment hit counter
        redis_client.set(f"{shortened_url}:last_accessed", now().isoformat()) #update last accessed IP
        return HttpResponseRedirect(original_url)
    else:
        return HttpResponse("URL not found", status=404)
    
def url_analytics(request, shortened_url):
    hit_count = redis_client.get(f"{shortened_url}:hits")
    last_accessed = redis_client.get(f"{shortened_url}:last_accessed")

    if hit_count is None or last_accessed is None :
        return HttpResponse("No analytics found for this URL:", status=404)
    
    return JsonResponse({
        'shortened_url': shortened_url,
        'hits': hit_count,
        'last_accessed': last_accessed
    })


