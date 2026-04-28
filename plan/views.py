from django.shortcuts import render

def main(request):
    return render(request, "main.html")

def fukuoka(request):
    return render(request, "fukuoka.html")