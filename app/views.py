from django.shortcuts import render
from app.models import Item
# Create your views here.
def drag_drop(request):
    Item.objects.create(name='CCS', column='column1')
    Item.objects.create(name='TARZ', column='column2')

    
    all_items = Item.objects.all()
    
    print("all items ", all_items)
    return render(request, 'drag.html',  context={'all_items': all_items})
