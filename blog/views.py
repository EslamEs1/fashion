from django.shortcuts import get_object_or_404
from .models import Blog, Comments
from django.views.generic import ListView, DetailView
from django.http import HttpResponseRedirect
from django.contrib import messages



class PostListView(ListView):
    model = Blog
    context_object_name = 'posts'


class PostDetailView(DetailView):
    model = Blog
    context_object_name = 'post'
        
    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['comments'] = Comments.objects.filter(post_id=self.get_object().id)
        return context
    

def comment(request, slug):
    if request.method == 'POST':
        text = request.POST.get('comment')
        if text:
            post = get_object_or_404(Blog, slug=slug)
            if Comments.objects.filter(post=post, user=request.user).exists():
                messages.error(request, 'Your Already Added Comment')
            else:
                Comments.objects.create(post=post, comment=text, user=request.user)
                messages.success(request, 'Your Comment Added Successful!')
        else:
            messages.error(request, 'Invalid Comment')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
