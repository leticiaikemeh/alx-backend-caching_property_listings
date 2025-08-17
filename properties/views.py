# properties/views.py
from django.http import JsonResponse
from django.views.decorators.cache import cache_page
from .models import Property


@cache_page(60 * 15)  # 15 minutes
def property_list(request):
    qs = Property.objects.all().only(
        "id", "title", "description", "price", "location", "created_at"
    )

    properties = [
        {
            "id": p.id,
            "title": p.title,
            "description": p.description,
            "price": str(p.price),                  # Decimal -> string
            "location": p.location,
            "created_at": p.created_at.isoformat(),  # datetime -> ISO 8601
        }
        for p in qs
    ]

    data = {"properties": properties}

    return JsonResponse({
        "properties": properties
    })
