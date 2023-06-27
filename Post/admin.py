from django.contrib import admin
from .models import Post,Comment





class Commentinline(admin.TabularInline):
    model=Comment
    extra=0


class PostAdmin(admin.ModelAdmin):
    inlines=[
            Commentinline,
        ]



admin.site.register(Post,PostAdmin)
admin.site.register(Comment)
