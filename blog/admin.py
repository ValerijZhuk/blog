from django.contrib import admin
from blog.models import *


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'topic', 'likes_count', 'times_of_edit', 'name')
    list_filter = ('topic', 'likes_count')
    search_fields = ('topic__name', 'name')

    fieldsets = (
        ('Post Info', {'fields': ('likes_count', 'name', 'text')}),
        ('Additional Info', {'fields': ('times_of_edit', 'topic')})
    )

    readonly_fields = ('likes_count',)

    actions = ['drop_times_of_edit']

    def drop_times_of_edit(self, request, queryset):
        queryset.update(times_of_edit=0)


class PostTopic(admin.ModelAdmin):
    list_display = ('name', 'title')
    list_filter = ('name',)
    search_fields = ('title',)
    readonly_fields = ('date_created',)

    fieldsets = (
        ('Topic Info', {'fields': ('date_created', 'name')}),
        ('Title', {'fields': ('title',)})
    )


class PostComment(admin.ModelAdmin):
    list_display = ('post', 'date_created', 'text')

    actions = ['max_rating']

    def max_rating(self, request, queryset):
        queryset.update(rating=4)


admin.site.register(Topic, PostTopic)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, PostComment)
