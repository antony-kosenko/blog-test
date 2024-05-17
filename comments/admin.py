from django.contrib import admin

from comments.models import Comment, Rate

admin.site.register(Comment)
admin.site.register(Rate)
