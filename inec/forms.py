from django import forms
from .models import Lga, PollingUnit, Ward

class PollingUnitForm(forms.ModelForm):
    lga_choices = [(lga.lga_id, lga.lga_name)for lga in Lga.objects.all()]
    ward_choices = [(ward.ward_id, ward.ward_name) for ward in Ward.objects.all()]
    # ward_id = forms.ModelChoiceField(queryset=Ward.objects.all(), empty_label=None)
    # lga_id = forms.ModelChoiceField(queryset=lga_choices, empty_label=None)
    ward_id = forms.ChoiceField(choices=ward_choices)
    lga_id = forms.ChoiceField(choices=lga_choices)


    class Meta:
        model = PollingUnit
        fields = '__all__'
