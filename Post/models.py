from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.urls import reverse


# Create your models here.
class Post(models.Model):
    image=models.ImageField(default='default.jpg',upload_to='Scam_images')
    title=models.CharField(max_length=300)
    description=models.TextField() 
    created_at=models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)       


    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self):       
      return reverse('post_detail', args=[str(self.id)])





class Comment(models.Model):
    scam=models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    comment=models.TextField(max_length=300)
    author=models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
   


    def __str__(self):
        return self.comment
          
          
    def get_absolute_url(self):        
        return reverse('scams_list')
    


