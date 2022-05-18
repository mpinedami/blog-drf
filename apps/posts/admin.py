from django.contrib import admin

from apps.posts.models import Post

# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass
