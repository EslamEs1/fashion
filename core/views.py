from django.shortcuts import render
from main.models import Main
from products.models import Product
from django.db.models import Q



def home(request):
    main = Main.objects.last()

    return {
        'main': main,
    }



def handler500(request):
    return render(request, '500.html', status=500)




def search(request):
    name = request.GET.get('q', '')
    products = Product.objects.filter(
        Q(description__icontains=name) |
        Q(title__icontains=name)
    )

    return render(request, 'products/product_list.html', {
        'products': products,

    })
