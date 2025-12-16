# bohubohu/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Core navigation
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('search/', views.search, name='search'),
    
    # HOME dropdown URLs
    path('home/', views.home, name='home'),  # Duplicate for home URL
    # path('home/style2/', views.home_style2, name='home_style2'),
    # path('home/style3/', views.home_style3, name='home_style3'),
    path('wedding-planner/style1/', views.wedding_planner_style1, name='wedding_planner_style1'),
    # path('wedding-planner/style2/', views.wedding_planner_style2, name='wedding_planner_style2'),
    path('wedding-shop/', views.wedding_shop_home, name='wedding_shop_home'),
    path('wedding-invitation/', views.wedding_invitation, name='wedding_invitation'),
    
    # PAGES dropdown URLs
    path('about/', views.about, name='about'),
    path('our-story/style1/', views.our_story_style1, name='our_story_style1'),
    # path('our-story/style2/', views.our_story_style2, name='our_story_style2'),
    # path('our-story/style3/', views.our_story_style3, name='our_story_style3'),
    path('accommodation/', views.accommodation, name='accommodation'),
    path('rsvp/style1/', views.rsvp_style1, name='rsvp_style1'),
    # path('rsvp/style2/', views.rsvp_style2, name='rsvp_style2'),
    # path('rsvp/style3/', views.rsvp_style3, name='rsvp_style3'),
    path('gallery/', views.gallery, name='gallery'),
    path('planners/', views.planners, name='planners'),
    path('planner/<int:id>/', views.planner_single, name='planner_single'),
    path('brides-grooms/', views.brides_grooms, name='brides_grooms'),
    path('services/', views.services, name='services'),
    # path('service/<int:id>/', views.service_single, name='service_single'),
    path('pricing/', views.pricing, name='pricing'),
    path('coming-soon/', views.coming_soon, name='coming_soon'),
    
    # PORTFOLIO dropdown URLs
    path('portfolio/grid/', views.portfolio_grid, name='portfolio_grid'),
    # path('portfolio/grid-s2/', views.portfolio_grid_s2, name='portfolio_grid_s2'),
    # path('portfolio/masonry/', views.portfolio_masonry, name='portfolio_masonry'),
    # path('portfolio/slide/', views.portfolio_slide, name='portfolio_slide'),
    path('portfolio/<int:id>/', views.portfolio_single, name='portfolio_single'),
    
    # SHOP dropdown URLs
    path('shop/', views.shop, name='shop'),
    path('product/<int:id>/', views.product_single, name='product_single'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    
    # BLOG dropdown URLs
    path('blog/', views.blog, name='blog'),
    path('blog/<int:id>/', views.blog_single, name='blog_single'),
]