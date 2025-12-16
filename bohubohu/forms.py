from django import forms
from .models import RSVP

class RSVPForm(forms.ModelForm):
    class Meta:
        model = RSVP
        fields = ['name', 'email', 'attending', 'guests', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'}),
            'attending': forms.Select(choices=[(True, 'Yes'), (False, 'No')], attrs={'class': 'form-select'}),
            'guests': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Message'}),
        }

# Optional template filter to add class dynamically
from django import template
register = template.Library()

@register.filter(name='add_class')
def add_class(field, css):
    return field.as_widget(attrs={"class": css})
