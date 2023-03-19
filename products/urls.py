from django.urls import path
from .views import ShopListView, ShopDetailView


app_name = 'products'


urlpatterns = [
    path('', ShopListView.as_view(), name='shop_list'),
    path('<slug:slug>/', ShopListView.as_view(), name='filter_list'),
    path('<int:min_price>/<int:max_price>/', ShopListView.as_view(), name='price_filter'),
    path('<str:tags>/', ShopListView.as_view(), name='tag_filter'),
    path('details/<slug:slug>/', ShopDetailView.as_view(), name='shop_detail'),
]
