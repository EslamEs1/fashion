from datetime import date
from cart.cart import Cart


def current_year(request):
    year = date.today().year
    
    return {
        'current_year': year
    }


def cart(request):
    return {'cart': Cart(request)}
