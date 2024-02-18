from django import forms
from .models import ContactRecord

class ContactRecordForm(forms.ModelForm):
    class Meta:
        model = ContactRecord
        fields = ['acquisition_method', 'contact_info', 'communication_result', 'deal_closed']

