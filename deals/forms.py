from django import forms
from .models import Deal
from leads.models import Lead


class DealForm(forms.ModelForm):
    expected_close_date = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )

    lead = forms.ModelChoiceField(
        queryset=Lead.objects.all().order_by('id'),
        widget=forms.Select(attrs={'class': 'form-select'}),
        empty_label="Select Lead"
    )

    class Meta:
        model = Deal
        fields = ['title', 'lead', 'value', 'stage', 'expected_close_date', 'notes']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'value': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'stage': forms.Select(attrs={'class': 'form-select'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }