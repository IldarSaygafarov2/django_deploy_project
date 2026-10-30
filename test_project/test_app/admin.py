from django.contrib import admin

from unfold import admin as unfold_admin

from .models import Category, Article


@admin.register(Category)
class CategoryAdmin(unfold_admin.ModelAdmin):
    list_display = ['id', 'title', 'slug', 'created_at']
    list_display_links = ['id', 'title']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ['created_at']


@admin.register(Article)
class ArticleAdmin(unfold_admin.ModelAdmin):
    list_display = ['id', 'title', 'is_active',
                    'category', 'user', 'created_at']
    list_display_links = ['id', 'title']
    list_editable = ['category', 'user']
    list_filter = ['category', 'user', 'created_at']
    search_fields = ['title', 'description']
    prepopulated_fields = {'slug': ('title',)}
