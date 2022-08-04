from django.contrib import admin

# Register your models here.
from .models import Post

class PostAdmin(admin.ModelAdmin):
  fields = ['Title', 'Text', 'Author', 'Created_date', 'Published_date']
admin.site.register(Post, PostAdmin)