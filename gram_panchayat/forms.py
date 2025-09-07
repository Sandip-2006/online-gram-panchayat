from django import forms
from .models import complain,Contact

class complain_form(forms.ModelForm):
    class Meta:
        model = complain
        fields = ['fname', 'phone_num', 'Email', 'complain', 'Complaint_Details', 'photo']

class contact_form(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name','email','subject','message']