from django.contrib import admin
from .models import Main, Message, About_img, About_text,Our_Team
# Register your models here.



@admin.register(Main)
class MainAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False if Main.objects.count() >= 1 else True



@admin.register(Message)
class Message(admin.ModelAdmin):
    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    list_display = ['name', 'email', 'message', 'created_at']
    list_filter = ['name',  'created_at']




@admin.register(About_text)
class About_textAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False if About_text.objects.count() >= 3 else True



@admin.register(About_img)
class About_imgAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False if About_img.objects.count() >= 1 else True



@admin.register(Our_Team)
class Our_TeamAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False if Our_Team.objects.count() >= 4 else True
