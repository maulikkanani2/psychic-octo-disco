from django.db import models
from django_descope.models import DescopeUser

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(DescopeUser, on_delete=models.CASCADE)
    profile_photo = models.ImageField(upload_to='media/user_profile/', default='media/user_avtar.jpg')
    login_photo = models.ImageField(upload_to='media/user_login/', blank=True, null=True)
    is_face_recohnisation = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.user.first_name} profile"
