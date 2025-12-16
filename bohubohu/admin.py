from django.contrib import admin
from .models import (
    HeroSection, Couple, StorySection, Event, GalleryImage,
    Service, PortfolioItem, BlogPost, RSVP
)

# --------------------------
# Hero Section
# --------------------------
@admin.register(HeroSection)
class HeroSectionAdmin(admin.ModelAdmin):
    list_display = ('title_main', 'title_sub', 'event_date', 'updated_at')
    search_fields = ('title_main', 'title_sub')
    readonly_fields = ('created_at', 'updated_at')


# --------------------------
# Couple Section
# --------------------------
@admin.register(Couple)
class CoupleAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'created_at')
    search_fields = ('name', 'role')
    readonly_fields = ('created_at', 'updated_at')


# --------------------------
# Story Section
# --------------------------
@admin.register(StorySection)
class StorySectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'updated_at')
    search_fields = ('title',)
    readonly_fields = ('created_at', 'updated_at')


# --------------------------
# Event Section
# --------------------------
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'updated_at')
    search_fields = ('title',)
    list_filter = ('date',)
    readonly_fields = ('created_at', 'updated_at')


# --------------------------
# Gallery Section
# --------------------------
@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'published', 'updated_at')
    search_fields = ('title',)
    list_filter = ('published',)
    readonly_fields = ('created_at', 'updated_at')
    
    # Optional: show thumbnail in admin
    def image_tag(self, obj):
        if obj.image:
            return f'<img src="{obj.image.url}" width="100" />'
        return '-'
    image_tag.allow_tags = True
    image_tag.short_description = 'Image'


# --------------------------
# Services Section
# --------------------------
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'updated_at')
    search_fields = ('title',)
    readonly_fields = ('created_at', 'updated_at')


# --------------------------
# Portfolio Section
# --------------------------
@admin.register(PortfolioItem)
class PortfolioItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'updated_at')
    search_fields = ('title', 'category')
    list_filter = ('category',)
    readonly_fields = ('created_at', 'updated_at')


# --------------------------
# Blog Section
# --------------------------
@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_at', 'updated_at')
    search_fields = ('title',)
    list_filter = ('published_at',)
    readonly_fields = ('created_at', 'updated_at')


# --------------------------
# RSVP Section
# --------------------------
@admin.register(RSVP)
class RSVPAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'attending', 'created_at')
    search_fields = ('name', 'email')
    list_filter = ('attending',)
    readonly_fields = ('created_at',)
