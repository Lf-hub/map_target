import django.forms as forms

from core.models import Target


class TargetForm(forms.ModelForm):
    
    class Meta:
        model = Target
        fields = ['name', 'latitude', 'longitude', 'expiration_date']