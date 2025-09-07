from django import forms
from .models import complain

class complain_form(forms.ModelForm):
    class Meta:
        model = complain
        fields = ['fname', 'phone_num', 'Email', 'complain', 'Complaint_Details', 'photo']

