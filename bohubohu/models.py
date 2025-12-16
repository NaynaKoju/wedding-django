from django.db import models
from django.utils.text import slugify
from django.utils import timezone

# ===== HERO SECTION =====
class HeroSection(models.Model):
    title_main = models.CharField(max_length=200, default="FOREVER")
    title_sub = models.CharField(max_length=200, default="AFTER")
    lead_text = models.TextField(default="Hi, Welcome to our Big Day...")
    event_date = models.DateField(null=True, blank=True)
    circle_text = models.CharField(max_length=100, default="you are invited")
    hero_image = models.ImageField(upload_to="hero_images/")
    background_image = models.ImageField(upload_to="hero_images/", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Hero Section: {self.title_main} {self.title_sub}"


# ===== COUPLE SECTION =====
class Couple(models.Model):
    name = models.CharField(max_length=200)
    role = models.CharField(max_length=100, blank=True)  # Bride/Groom
    image = models.ImageField(upload_to='couples/')
    bio = models.TextField(blank=True)
    animation_class = models.CharField(max_length=100, default='fadeInUp')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


# ===== STORY SECTION =====
class StorySection(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='story/', blank=True, null=True)
    animation_class = models.CharField(max_length=100, default='fadeInUp')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


# ===== EVENTS =====
class Event(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    description = models.TextField()
    image = models.ImageField(upload_to='events/', blank=True, null=True)
    animation_class = models.CharField(max_length=100, default='fadeInUp')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


# ===== GALLERY =====
class GalleryImage(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='gallery/')
    published = models.BooleanField(default=True)
    animation_class = models.CharField(max_length=100, default='fadeInUp')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


# ===== SERVICES =====
class Service(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    icon_class = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='services/', blank=True, null=True)
    animation_class = models.CharField(max_length=100, default='fadeInUp')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


# ===== PORTFOLIO =====
class PortfolioItem(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='portfolio/')
    category = models.CharField(max_length=100, blank=True)
    animation_class = models.CharField(max_length=100, default='fadeInUp')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


# ===== BLOG =====
class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    content = models.TextField()
    featured_image = models.ImageField(upload_to='blogs/')
    published_at = models.DateTimeField(auto_now_add=True)
    animation_class = models.CharField(max_length=100, default='fadeInUp')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


# ===== RSVP =====
class RSVP(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    attending = models.BooleanField()
    guests = models.IntegerField(default=1)
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({'Attending' if self.attending else 'Not attending'})"


# ===== NAVIGATION =====
class NavigationItem(models.Model):
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=200, blank=True)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='children')
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order']


# ===== SITE SETTINGS =====
class SiteSettings(models.Model):
    site_name = models.CharField(max_length=100, default='Bohu.')
    contact_email = models.EmailField(default='bohu@gmail.com')
    contact_phone = models.CharField(max_length=20, default='+3I6555–01I6')
    address = models.TextField(default='+517 Washington Ave.\nManchester, Kentucky 39495')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.site_name
