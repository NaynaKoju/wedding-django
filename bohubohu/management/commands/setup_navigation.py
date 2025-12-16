from django.core.management.base import BaseCommand
from bohubohu.models import NavigationItem

class Command(BaseCommand):
    help = 'Creates the navigation structure for Bohu wedding website'
    
    def handle(self, *args, **kwargs):
        # Delete existing items
        NavigationItem.objects.all().delete()
        
        items = [
            {'name': 'HOME', 'url': '/'},
            {'name': 'PAGES', 'url': '', 'children': [
                {'name': 'About Us', 'url': '/about-us/'},
                {'name': 'Our Story', 'url': '/our-story/'},
                {'name': 'Accomodation', 'url': '/accomodation/'},
                {'name': 'RSVP', 'url': '/rsvp/'},
                {'name': 'Gallery', 'url': '/gallery/'},
            ]},
            {'name': 'PORTFOLIO', 'url': '/portfolio/'},
            {'name': 'SHOP', 'url': '/shop/'},
            {'name': 'BLOG', 'url': '/blog/'},
            {'name': 'CONTACT', 'url': '/contact/'},
        ]
        
        for i, item_data in enumerate(items):
            item = NavigationItem.objects.create(
                name=item_data['name'],
                url=item_data.get('url', ''),
                order=i,
                is_active=True
            )
            
            if 'children' in item_data:
                for j, child_data in enumerate(item_data['children']):
                    NavigationItem.objects.create(
                        name=child_data['name'],
                        url=child_data['url'],
                        order=j,
                        parent=item,
                        is_active=True
                    )
        
        self.stdout.write(self.style.SUCCESS('Navigation items created successfully!'))
        self.stdout.write(f'Total items created: {NavigationItem.objects.count()}')