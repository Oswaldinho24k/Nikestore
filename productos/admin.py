from django.contrib import admin
from .models import Product, Category, Subcat

# Register your models here.

class ProdAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("name",)}

admin.site.register(Product, ProdAdmin)
admin.site.register(Category)
admin.site.register(Subcat)
