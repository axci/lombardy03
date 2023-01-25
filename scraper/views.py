from django.shortcuts import render


# Create your views here.
def price_to_area(request):
    
    context = {}

    return render(request, 'scraper/index.html', context)
