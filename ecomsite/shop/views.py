from django.shortcuts import render
from .models import Product
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    product_objects=Product.objects.all()
    #search code
    item_name=request.GET.get('item_name')
    if item_name!='' and item_name is not None:
        product_objects=product_objects.filter(title_icontains=item_name)
# Paginator code
paginator=Paginator(product_objects,4)
page=request.GET.get ('page')
product_objects=paginator.get_page(page)

return render(request,'')