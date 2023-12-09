from django.contrib import admin
from.models import Category,Product
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepoluted_field={'slugs':('name',)}
admin.site.register(Category,CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','price','stock','available','created','updated']
    prepoluted_field={'slugs':('name',)}
    list_editable = ['price','stock','available']
    List_per_page=20
admin.site.register(Product,ProductAdmin)
