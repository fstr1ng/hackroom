from django.forms import ModelForm

from .models import Policy

class PolicyForm(ModelForm):
    class Meta:
        model = Policy
        fields = ['name', 'type', 'issue']
