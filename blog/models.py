from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="العنوان")
    description = models.TextField(verbose_name="الوصف")
    image = models.ImageField(upload_to='post_images/', blank=True, null=True, verbose_name="الصورة")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ النشر")

    def __str__(self):
        return self.title