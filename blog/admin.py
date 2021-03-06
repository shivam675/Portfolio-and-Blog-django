from django.contrib import admin
from .models import Blog, PostImage, Tag, Comment, Video


class PostImageAdmin(admin.StackedInline):
    model = PostImage
    extra = 1

class PostVideoAdmin(admin.StackedInline):
    model = Video
    extra = 1

class PostCommentAdmin(admin.StackedInline):
    model = Comment

class PostTagAdmin(admin.StackedInline):
    model = Tag
    extra = 1
# admin.site.register(Blog)
@admin.register(Blog)
class PostAdmin(admin.ModelAdmin):
    inlines = [
    PostImageAdmin,
    PostTagAdmin,
    PostVideoAdmin,
    ]

    class Meta:
        model = Blog

@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    pass

@admin.register(Comment)
class PostCommentAdmin(admin.ModelAdmin):
    pass

@admin.register(Video)
class PostVideoAdmin(admin.ModelAdmin):
    pass


# @admin.register(Tag)
# class PostTagAdmin(admin.ModelAdmin):
#     pass
