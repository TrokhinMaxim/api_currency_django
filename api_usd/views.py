from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.cache import cache_page
from .models import Currency
from .currency import get_currency


@cache_page(10)
@require_http_methods(["GET"])
def get_current_usd(request):
    currency_data = get_currency()
    if "error" in currency_data:
        return JsonResponse({"error": currency_data["error"]})
    currency_instance = Currency.objects.create(value=currency_data["exchange_rate"])
    last_10_requests = Currency.objects.order_by("-request_date")[:10].values(
        "value", "request_date"
    )
    formatted_output = []
    for request_info in last_10_requests:
        date_str = request_info["request_date"].strftime("%Y-%m-%d %H:%M:%S")
        formatted_output.append(
            {"Курс Доллара": request_info["value"], "Дата запроса": date_str}
        )

    return JsonResponse(
        {"last_10_requests": formatted_output},
        json_dumps_params={"ensure_ascii": False},
    )
