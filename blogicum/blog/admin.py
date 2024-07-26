from django.contrib import admin
from .models import Location, Category, Post, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'text',
        'pub_date',
        'author',
        'location',
        'category',
        'is_published',
        'created_at'
    )
    list_editable = (
        'category',
        'is_published'
    )
    search_fields = ('title',)
    list_filter = ('is_published',)
    list_display_links = ('title',)
    empty_value_display = 'Не задано'


admin.site.register(Category)
admin.site.register(Location)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
