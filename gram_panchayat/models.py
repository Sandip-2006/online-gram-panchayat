from django.db import models


# Create your models here.

COMPLAINT_CATEGORIES = [
    ("Water", "Water Supply"),
    ("Electricity", "Electricity"),
    ("Road", "Road / Infrastructure"),
    ("Sanitation", "Sanitation"),
    ("Other", "Other"),
]

class complain(models.Model):
    fname = models.CharField(max_length=200,null=False)
    phone_num = models.CharField(max_length=10,null=False)
    Email = models.CharField(max_length=100,null=True)
    complain = models.CharField(choices=COMPLAINT_CATEGORIES, default='Water',max_length=50)
    Complaint_Details = models.TextField(null=False, max_length=500)
    photo = models.FileField(upload_to='complaints/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'complain is: {self.complain} | {self.Complaint_Details[:36]}' 