import time
from django.views.decorators.cache import cache_page
from django.http import JsonResponse


@cache_page(60)  # cache for 60 seconds
def slow_property_count(request):
    # pretend to be slow
    time.sleep(2)
    # in real life you'd query Property.objects.count()
    return JsonResponse({"count": 42, "cached_for": "60s"})
