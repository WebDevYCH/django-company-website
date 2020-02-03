from django.contrib import admin
from .models import Post, Category, Tag

# class PostAdmin(admin.ModelAdmin):
#     list_display=['title', 'created_time', 'modified_time', 'category', 'author']
from .models import Portfolio

admin.site.register(Portfolio)
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Tag)