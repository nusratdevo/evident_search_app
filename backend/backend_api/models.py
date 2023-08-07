from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.utils.translation import gettext_lazy as _

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        if not email:
            raise ValueError("Users must have an email")

        email = self.normalize_email(email).lower()

        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save()

        return user


    def create_superuser(self, email, password, **extra_fields):
        if not password:
            raise ValueError("Password is required")

        user = self.create_user(email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user

class CustomUser(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    image = models.ImageField(blank=True, upload_to='userprofile')

    #department = models.CharField(max_length=255)

    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)
    is_admin        = models.BooleanField(default=True)
    is_staff        = models.BooleanField(default=False)
    is_active        = models.BooleanField(default=True)
    is_superadmin        = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    def __str__(self):
        return self.email
    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, add_label):
        return True

class SortedInput(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    input_values = models.CharField(max_length=100)
    search_value = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-timestamp']