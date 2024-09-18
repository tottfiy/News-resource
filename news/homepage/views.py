from django.shortcuts import render


# Create your views here.
def landing_handle(request):
    return render(request, 'homepage/landing.html')
