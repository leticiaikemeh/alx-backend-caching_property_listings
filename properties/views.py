from django.http import JsonResponse
from django.views.decorators.cache import cache_page
from .models import Property


@cache_page(60 * 15)  # 15 minutes
def property_list(request):
    # Return ALL properties (as the task requires)
    qs = Property.objects.all().only(
        "id", "title", "description", "price", "location", "created_at"
    )

    data = [
        {
            "id": p.id,
            "title": p.title,
            "description": p.description,
            # Decimal -> string for JSON
            "price": str(p.price),
            "location": p.location,
            "created_at": p.created_at.isoformat(),   # datetime -> ISO 8601
        }
        for p in qs
    ]
    return JsonResponse(data, safe=False)
