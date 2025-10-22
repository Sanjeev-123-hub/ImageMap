from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'mapapp/home.html')
def map(request):
    return render(request, 'mapapp/map.html')