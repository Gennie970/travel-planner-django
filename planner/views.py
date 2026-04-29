import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import TripDay, TripItem


# 📥 데이터 가져오기 (GET)
def get_trip(request):
    result = {}

    for day in TripDay.objects.all():
        result[day.date] = []

        for item in day.items.all():
            result[day.date].append({
                "time": item.time,
                "text": item.text,
                "cost": item.cost or ""
            })

    return JsonResponse(result)


# 💾 데이터 저장 (POST)
@csrf_exempt
def update_trip(request):
    if request.method == "POST":
        data = json.loads(request.body)

        TripDay.objects.all().delete()

        for date, items in data.items():
            day = TripDay.objects.create(date=date)

            for i in items:
                TripItem.objects.create(
                    day=day,
                    time=i.get("time", ""),
                    text=i.get("text", ""),
                    cost=i.get("cost") or None
                )

    return JsonResponse({"status": "ok"})






from django.shortcuts import render

def main(request):
    return render(request, "main.html")

def fukuoka(request):
    return render(request, "fukuoka.html")

def italy(request):
    return render(request, "italy.html")
