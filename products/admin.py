from django.contrib import admin
from .models import Product, preciseCategory, Tag

# Register your models here.
admin.site.register(Product)
admin.site.register(preciseCategory)
admin.site.register(Tag)
