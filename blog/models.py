from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from django.conf import settings
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from core.utils import slugify_instance_title


# Start Blog
class Blog(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, unique=True)
    img = models.ImageField(upload_to='blog/%Y/%m/%d', verbose_name='image')
    description = models.TextField(max_length=15000)
    slug = models.SlugField(max_length=80, unique=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created']
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Blog, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.slug])

    def __str__(self):
        return self.author.username + self.title


@receiver(pre_save, sender=Blog)
def check_slug(sender, instance, *args, **kwargs):
    if instance.slug is None:
        slugify_instance_title(instance, save=False)
        

@receiver(post_save, sender=Blog)
def course_post_save(sender, instance, created, *args, **kwargs):
    if created:
        slugify_instance_title(instance, save=True)



class Comments(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Blog, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created_at',)
        verbose_name = 'Coments'
        verbose_name_plural = 'Comentss'

    def __str__(self):
        return f'{self.user.username} - {self.user.email}'

