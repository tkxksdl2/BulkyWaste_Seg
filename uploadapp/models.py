from django.db import models

class Upload(models.Model):
    name = models.CharField(max_length=15, null=True)
    phone_number = models.CharField(max_length=50, null=True)
    image = models.ImageField(upload_to='upload/', null=True)
    location = models.TextField(null=True)
    #type = models.CharField(max_length=30,null=True)
    submit = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True, null=True)
    label = models.TextField(null=True)
    price = models.IntegerField(null=True)
