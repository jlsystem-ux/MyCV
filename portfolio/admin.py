from django.contrib import admin
from .models import Technology, Project

@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon', 'color')
    search_fields = ('name',)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'featured', 'order', 'created_at')
    list_filter = ('status', 'featured', 'technologies')
    search_fields = ('title', 'description', 'short_description')
    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal = ('technologies',)
    date_hierarchy = 'created_at'
    ordering = ('order', '-created_at')

    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'slug', 'short_description', 'description')
        }),
        ('Technologies', {
            'fields': ('technologies',)
        }),
        ('Media & Links', {
            'fields': ('image', 'demo_url', 'github_url')
        }),
        ('Status & Display', {
            'fields': ('status', 'featured', 'order', 'completed_at')
        }),
    )
