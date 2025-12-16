from .models import NavigationItem, SiteSettings

def navigation_context(request):
    # Get main navigation items (no parent)
    main_navigation = NavigationItem.objects.filter(
        parent=None, 
        is_active=True
    ).order_by('order')
    
    # Get or create site settings
    site_settings, created = SiteSettings.objects.get_or_create(
        id=1,
        defaults={
            'site_name': 'Bohu.',
            'contact_email': 'bohu@gmail.com',
            'contact_phone': '+3I6555–01I6',
            'address': '+517 Washington Ave.\nManchester, Kentucky 39495'
        }
    )
    
    return {
        'main_navigation': main_navigation,
        'site_settings': site_settings
    }