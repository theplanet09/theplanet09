from django.shortcuts import render
from banana.models import Item

# Create your views here.

# landing page shenanigans
def banana_landing(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'banana_landing.html', context)