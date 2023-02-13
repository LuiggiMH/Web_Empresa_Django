from django.contrib import admin
from .models import Category, Blog

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


class BlogAdmin(admin.ModelAdmin):  # Configuracion Extendida
    readonly_fields = ('created', 'updated')
    list_display = ('title', 'author', 'published')
    ordering = ('author', 'published')
    search_fields = ('title', 'author__username', 'categories__name')
    date_hierarchy='published'
    list_filter = ('author__username', 'categories__name')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Blog, BlogAdmin)
