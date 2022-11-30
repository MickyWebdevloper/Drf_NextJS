from django.contrib import admin
from .models import Posts


@admin.register(Posts)
class PostsAdmin(admin.ModelAdmin):
    list_display = ['id', 'slug', 'title','author',
                    'content', 'date_created', 'date_updated']

    prepopulated_fields = {"slug": ("title",)}
