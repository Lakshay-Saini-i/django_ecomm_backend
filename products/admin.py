from django.contrib import admin
from . models import Product, Category, ProductImage, ColorVarient, SizeVarient, Coupon
# Register your models here.






class ProductImageAdmin(admin.StackedInline):
    model = ProductImage


class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'price']
    inlines = [ProductImageAdmin]

class ColorVarientAdmin(admin.ModelAdmin):
    list_display = ['color_name', 'price']  
    model = ColorVarient


class SizeVarientAdmin(admin.ModelAdmin):
    list_display = ['size_name', 'price']    
    model = SizeVarient



admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage)
admin.site.register(ColorVarient, ColorVarientAdmin)
admin.site.register(SizeVarient, SizeVarientAdmin)
admin.site.register(Coupon)
