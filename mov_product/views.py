from django.shortcuts import render
from .models import MovProduct


# Create your views here.
def mov_product(request):
    products = MovProduct.objects.all()
    return render(request, 'mov_product/mov_product.html', {'products': products})
