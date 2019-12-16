from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.conf import settings
from django.urls import reverse

CATEGORY_CHOICES = (
    ('WLB', 'work life balance'),
    ('ALP', 'activity lift people'),
)
# Create your models here.
class preciseCategory(models.Model):
    name = models.CharField(max_length=50)
    common_category = models.CharField(choices=CATEGORY_CHOICES, max_length=3, default='WLB')

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=23)

    def __str__(self):
        return self.name

    class Meta:
        pass

class Product(models.Model):
    name = models.CharField(max_length=125)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='product_pics', default='default.jpg')
    precise_category = models.ForeignKey(preciseCategory, on_delete=models.CASCADE, null=True)
    common_category = models.CharField(choices=CATEGORY_CHOICES, max_length=3, default='WLB')
    tags = models.ManyToManyField(Tag)
    date_posted = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering=['date_posted']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product-detail', kwargs={'pk': self.pk})

class PaymentMethods(models.Model):
    name = models.CharField(max_length=125)

    class Meta:
        pass

    def __str__(self):
        return self.name

