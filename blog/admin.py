from django.contrib import admin
from .models import Blog, Comments
from django_summernote.admin import SummernoteModelAdmin



@admin.register(Blog)
class BlogAdmin(SummernoteModelAdmin, admin.ModelAdmin):
    list_display = ['author', 'title', 'created']
    search_fields = ['title']


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    pass

