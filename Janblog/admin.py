from django.contrib import admin

# Register your models here.
from .models import Article,Category,Tag

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_time', 'last_modified_time', 'category', 'author']

admin.site.register(Article,PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)