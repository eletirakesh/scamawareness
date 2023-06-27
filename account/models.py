from django.db import models

from django.db import models
from Post.models import Post

from django.contrib.auth.models import User


class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    image=models.ImageField(default='default.jpg' ,upload_to='profile_pics')
    bio=models.CharField(max_length=300)
    badge=models.CharField(max_length=100,default='Beginner',null=True,blank=True)

    def __str__(self) -> str:
        return f'{self.user.username} Profile'
    
    def update_badge(self):
        post_count = Post.objects.filter(author=self.user).count()
        if post_count == 0:
            self.badge = "Novice"
        elif post_count >= 1 and post_count < 5:
            self.badge = "Apprentice"
        elif post_count >= 5:
            self.badge = "Expert"
        else:
            self.badge = "Unknown"

    def save(self, *args, **kwargs):
        self.update_badge()
        super().save(*args, **kwargs)