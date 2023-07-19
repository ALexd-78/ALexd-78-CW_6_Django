from django.contrib import admin

from blog.models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'heading', 'create_date', 'count_views')
    search_fields = ('heading',)
    list_filter = ('create_date', 'count_views')
