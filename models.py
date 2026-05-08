from django.db import models

class Entry(models.Model):
    title = models.CharField(max_length=100) # عنوان المقالة
    content = models.TextField()               # محتوى المقالة
    timestamp = models.DateTimeField(auto_now_add=True) # وقت الإنشاء

    def __str__(self):
        return f"{self.title}"

class Listing(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image_url = models.URLField(blank=True)

    def __str__(self):
        return f"{self.title}"