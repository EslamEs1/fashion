from django.contrib import admin
from .models import Product, Category, Branding, ImageProduct, ProductReview, Tags
from django_summernote.admin import SummernoteModelAdmin



class ImgInline(admin.TabularInline):
    model = ImageProduct
    max_num = 6
    extra = 1



@admin.register(Product)
class ProductAdmin(SummernoteModelAdmin, admin.ModelAdmin):
    list_display = ['title', 'check_rating',
                    'category', 'new_price', 'available', 'created']
    list_editable = ['new_price', 'available']
    list_filter = ['available', 'created', 'update']
    search_fields = ['title']
    inlines=[ImgInline]



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass



@admin.register(Branding)
class BrandingAdmin(admin.ModelAdmin):
    pass


admin.site.register(ProductReview)
admin.site.register(Tags)
