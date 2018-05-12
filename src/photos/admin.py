from django.contrib import admin
from photos import models


class TagInline(admin.TabularInline):
    model = models.Tag
    extra = 0


class CommentInline(admin.TabularInline):
    model = models.Comment
    extra = 0


class CategoryInline(admin.TabularInline):
    model = models.Category
    extra = 0


class PhotoAdmin(admin.ModelAdmin):
    inlines = (CategoryInline, TagInline, CommentInline)

    class Meta:
        model = models.Photo


admin.site.register(models.Photo, PhotoAdmin)
admin.site.register(models.Category)
