"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from core.views import handler500
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from payment.webhooks import stripe_webhook

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('accounts/', include('allauth.urls')),
    path('cart/', include('cart.urls', namespace='cart')),
    path('orders/', include('orders.urls', namespace='orders')),
    path('products/', include('products.urls', namespace='products')),
    path('blog/', include('blog.urls', namespace='blog')),
    path('payment/', include('payment.urls', namespace='payment')),
    path('', include('main.urls', namespace='main')),
    path('coupons/', include('coupons.urls', namespace='coupons')),
    path('summernote/', include('django_summernote.urls')),
    path('payment/webhook/', stripe_webhook, name='stripe-webhook'),

]





handler500 = handler500


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
