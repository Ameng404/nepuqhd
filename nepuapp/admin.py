from django.contrib import admin
from .models import Post, Category,Column,Article,Paper

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title','column']
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'modified_time', 'category', 'author']

admin.site.register(Article,ArticleAdmin)
admin.site.register(Column)
admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Paper)