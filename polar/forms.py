from django import forms
from .models import Query

class QueryForm(forms.ModelForm):
  class Meta:
    model = Query
    fields = ['query']
    widgets = {
        'query': forms.TextInput(
            attrs={'id': 'query-text', 'required': True, 'placeholder': 'Search', 'tab-index': '1'}
        ),
    }
