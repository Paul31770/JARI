from django.shortcuts import render
from app.models import *
# Create your views here.
def drag_drop(request):
    # Item.objects.create(name='CCS', column='column1')
    # Item.objects.create(name='TARZ', column='column2')
    all_items = Item.objects.all()
    all_name= Task.objects.all()
    print("all items ", all_items)
    print("all name ",all_name)
    return render(request, 'drag.html',  context={'all_items': all_items, 'all_name': all_name})

    
