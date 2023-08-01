from django.contrib import admin
from .models import Post,User

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass

# Register your models here.
