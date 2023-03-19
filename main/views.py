from django.shortcuts import render, redirect
from .forms import MessageForm
from .models import About_img,About_text,Our_Team
from django.contrib import messages
from products.models import Product
from blog.models import Blog



def index(request):
    product = Product.objects.all()
    blog = Blog.objects.filter()[:3]
    return render(request, 'index.html', {
        'product': product,
        'blog': blog,
        
    })


def content(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid:
            form.save()
            messages.success(request, 'Your message has been sent!')
            redirect('/contact')
        else:
            messages.success(request, 'Your message not been sent!')
    else:
        form = MessageForm()

    return render(request, 'contact.html', {
        'form': form,
        })


def about(request):
    team = Our_Team.objects.all()
    img = About_img.objects.last()
    text = About_text.objects.all()
    return render(request, 'about.html', {
        'team':team,
        'img': img,
        'text': text,

    })







