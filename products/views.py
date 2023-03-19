from django.views.generic import ListView, DetailView
from .models import Product, ImageProduct, Category, Branding
from django.db.models import Q, Count
from taggit.models import Tag
from cart.forms import CartAddProductForm
from django.views.generic.edit import FormMixin


class ShopListView(ListView):
    model = Product
    paginate_by= 12
    context_object_name = 'products'

    def get_queryset(self):
        queryset = super(ShopListView, self).get_queryset()
        queryset = queryset.all()
        slug = self.kwargs.get('slug')
        min_price = self.kwargs.get('min_price')
        max_price = self.kwargs.get('max_price')
        tag = self.kwargs.get('tags')
        search_query = self.request.GET.get('q','')
        
        if slug:
            queryset = queryset.filter(Q(category__slug=slug) | Q(branding__slug=slug))

        if min_price and max_price:
            queryset = queryset.filter(new_price__range=(min_price, max_price))

        if tag:
            queryset = queryset.filter(product_tags__tags=tag)

        if search_query:
            queryset = queryset.filter(title__icontains=search_query)

        return queryset
    
    def get_context_data(self, **kwargs):
        context = super(ShopListView, self).get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        context['branding'] = Branding.objects.all()
        context['tags'] = Tag.objects.annotate(num_products=Count('tags')).filter(num_products=1)
        return context
    

class ShopDetailView(FormMixin,DetailView):
    model = Product
    context_object_name = 'product'
    form_class = CartAddProductForm

    def get_context_data(self, **kwargs):
        context = super(ShopDetailView, self).get_context_data(**kwargs)
        context['img'] = ImageProduct.objects.filter(product=self.get_object())
        context['tags'] = Tag.objects.filter(tags__product=self.get_object())
        context['related'] = Product.objects.filter(category=self.get_object().category)[:3]
        return context



