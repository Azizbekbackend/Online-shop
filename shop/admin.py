from django.contrib import admin
from .models import Category,Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug':('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','slug','price','avialable','created','updated']
    list_filter = ['avialable','created','updated']
    list_editable = ['price','avialable']
    prepopulated_fields = {'slug':('name',)}

