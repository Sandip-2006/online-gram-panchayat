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
    

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email  = models.EmailField(null=True, blank=True)
    subject = models.CharField(max_length=200)
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Contact'

    def __str__(self):
        return f"{self.name} - {self.subject}"
    

class Event(models.Model):
    title = models.CharField(max_length=200,blank=True)
    image = models.ImageField(upload_to='events/')
    description = models.TextField(blank=True)
    date = models.DateField()
    location = models.CharField(max_length=200)

    class Meta:
        db_table = 'Event'

    def __str__(self):
        return self.title
    
class Celebrity(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='celebrity_images/')
    extra_points = models.TextField(blank=True,null=True)
    created_at  = models.DateTimeField(auto_now_add=True,blank=True)

    class Meta:
        db_table = 'Celebrity'

    def __str__(self):
        return self.name
    
class Gallery(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='gallery/')
    created_at  = models.DateTimeField(auto_now_add=True,blank=True)

    class Meta:
        db_table = 'Gallery'

    
    def __str__(self):
        return self.title