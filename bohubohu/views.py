# bohubohu/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import (
    HeroSection, Couple, StorySection, Event, GalleryImage,
    Service, PortfolioItem, BlogPost, RSVP
)
from .forms import RSVPForm

# -------------------------------
# Core Pages
# -------------------------------

def home(request):
    hero_sections = HeroSection.objects.all()
    couples = Couple.objects.all()
    story_sections = StorySection.objects.all()
    events = Event.objects.all()
    gallery_images = GalleryImage.objects.filter(published=True)
    services = Service.objects.all()
    portfolio_items = PortfolioItem.objects.all()
    blog_posts = BlogPost.objects.order_by('-published_at')[:3]

    if request.method == 'POST':
        rsvp_form = RSVPForm(request.POST)
        if rsvp_form.is_valid():
            rsvp_form.save()
            messages.success(request, "Thank you! Your RSVP has been submitted.")
            return redirect('home')
    else:
        rsvp_form = RSVPForm()

    context = {
        'hero_sections': hero_sections,
        'couples': couples,
        'story_sections': story_sections,
        'events': events,
        'gallery_images': gallery_images,
        'services': services,
        'portfolio_items': portfolio_items,
        'blog_posts': blog_posts,
        'rsvp_form': rsvp_form,
    }
    # Use landing.html as the home page (matches original WordPress demo)
    return render(request, 'bohu/landing.html', context)


def contact(request):
    return render(request, 'bohu/contact.html')


def search(request):
    query = request.GET.get('q', '')
    context = {'query': query}
    return render(request, 'bohu/search.html', context)


def about(request):
    return render(request, 'bohu/about.html')


def accommodation(request):
    return render(request, 'bohu/accommodation.html')


def coming_soon(request):
    return render(request, 'bohu/coming_soon.html')


def rsvp_style1(request):
    return render(request, 'bohu/rsvp_style1.html')


# -------------------------------
# Wedding Pages
# -------------------------------

def wedding_planner_style1(request):
    return render(request, 'bohu/wedding_planner_style1.html')


def wedding_shop_home(request):
    return render(request, 'bohu/wedding_shop_home.html')


def wedding_invitation(request):
    return render(request, 'bohu/wedding_invitation.html')


# -------------------------------
# Pages with dynamic content
# -------------------------------

def our_story_style1(request):
    story_sections = StorySection.objects.all()
    couples = Couple.objects.all()
    context = {
        'story_sections': story_sections,
        'couples': couples
    }
    return render(request, 'bohu/our_story_style1.html', context)


def gallery(request):
    images = GalleryImage.objects.filter(published=True)
    return render(request, 'bohu/gallery.html', {'gallery_images': images})


def planners(request):
    return render(request, 'bohu/planners.html')


def planner_single(request, id):
    return render(request, 'bohu/planner_single.html')


def brides_grooms(request):
    couples = Couple.objects.all()
    return render(request, 'bohu/brides_grooms.html', {'couples': couples})


def services(request):
    services_list = Service.objects.all()
    return render(request, 'bohu/services.html', {'services': services_list})


def service_single(request, id):
    service = get_object_or_404(Service, id=id)
    return render(request, 'bohu/service_single.html', {'service': service})


def pricing(request):
    return render(request, 'bohu/pricing.html')


def portfolio_grid(request):
    items = PortfolioItem.objects.all()
    return render(request, 'bohu/portfolio_grid.html', {'portfolio_items': items})


def portfolio_single(request, id):
    item = get_object_or_404(PortfolioItem, id=id)
    return render(request, 'bohu/portfolio_single.html', {'item': item})


# -------------------------------
# Shop Pages
# -------------------------------

def shop(request):
    return render(request, 'bohu/shop.html')


def product_single(request, id):
    return render(request, 'bohu/product_single.html')


def cart(request):
    return render(request, 'bohu/cart.html')


def checkout(request):
    return render(request, 'bohu/checkout.html')


# -------------------------------
# Blog Pages
# -------------------------------

def blog(request):
    posts = BlogPost.objects.order_by('-published_at')
    return render(request, 'bohu/blog.html', {'blog_posts': posts})


def blog_single(request, id):
    post = get_object_or_404(BlogPost, id=id)
    return render(request, 'bohu/blog_single.html', {'post': post})
