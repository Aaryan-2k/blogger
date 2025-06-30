from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class blogs(models.Model):
    blog_text=models.TextField()
    blog_title=models.CharField(max_length=500)
    blog_image=models.ImageField(upload_to='blogimg', null=True, blank=True)
    created_at=models.DateTimeField(auto_now=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE, null=True, blank=True)
