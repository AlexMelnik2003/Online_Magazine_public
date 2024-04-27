from django.contrib import admin
from .models import Product, ProductImage, Comment, Rating, Editor, Profile

admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(Comment)
admin.site.register(Rating)
admin.site.register(Editor)
admin.site.register(Profile)
