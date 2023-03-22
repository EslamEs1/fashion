from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from taggit.managers import TaggableManager
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from core.utils import slugify_instance_title


class Product(models.Model):
    type = (
        ('white','white'),
        ('red','red'),
        ('blue','blue'),
        ('green', 'green'),
        ('black', 'black'),
        ('gray', 'gray'),
        ('silver', 'silver'),
        ('brown', 'brown'),
        ('azure', 'azure'),
    )
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='category')
    branding = models.ForeignKey('Branding', on_delete=models.CASCADE, related_name='branding')
    title = models.CharField(max_length=80, unique=True)
    new_price = models.DecimalField(max_digits=19, decimal_places=2)
    old_price = models.DecimalField(max_digits=19, decimal_places=2)
    description = models.TextField(max_length=15000)
    information = models.TextField(max_length=15000, null=True, blank=True)
    color = models.CharField(max_length=15 ,choices=type)
    heart = models.IntegerField(default=0, editable=False)
    available = models.BooleanField(default=True)
    slug = models.SlugField(max_length=80, blank=True, null=True, editable=False)
    update = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Product, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('products:shop_detail', args=[self.slug])


    def check_rating(self):
        ratings = self.Product_reviews.all()
        if ratings:
            return round(sum(r.rating for r in ratings) / len(ratings),2)
        else:
            return 0


@receiver(pre_save, sender=Product)
def check_slug(sender, instance, *args, **kwargs):
    if instance.slug is None:
        slugify_instance_title(instance, save=False)


@receiver(post_save, sender=Product)
def course_post_save(sender, instance, created, *args, **kwargs):
    if created:
        slugify_instance_title(instance, save=True)

# Created ImageProduct==============================
class ImageProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_img')
    image = models.ImageField(upload_to='products/%Y/%m/%d/')

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.product.title


# Created Category==============================
class Category(models.Model):
    category_name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=80, blank=True,null=True, editable=False)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Category'

    def __str__(self):
        return self.category_name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.category_name)
        super(Category, self).save(*args, **kwargs)

    def filter(self):
        return reverse('products:filter_list', args=[self.slug])

# Created branding==============================
class Branding(models.Model):
    branding_name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=80, blank=True,null=True, editable=False)

    class Meta:
        verbose_name = 'Branding'
        verbose_name_plural = 'Branding'

    def __str__(self):
        return self.branding_name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.branding_name)
        super(Branding, self).save(*args, **kwargs)
        
    def filter(self):
        return reverse('products:filter_list', args=[self.slug])


# Create Product Review
class ProductReview(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='user_reviews', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='Product_reviews', on_delete=models.CASCADE)
    rating = models.IntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(5)])
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.product.title



class Tags(models.Model):
    product = models.ForeignKey(Product, related_name='product_tags', on_delete=models.CASCADE)
    tags = TaggableManager()

    def __str__(self):
        return str(self.tags)
