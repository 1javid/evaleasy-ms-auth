# user_auth/models.py
from django.db import models
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import BaseUserManager
from django.core.exceptions import ValidationError

class UserManager(BaseUserManager):
    def create_user(self, user_id, user_type, institution, first_name, last_name, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(
            user_id=user_id,
            user_type=user_type,
            institution=institution,
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password,
            **extra_fields
        )
        user.save(using=self._db)
        return user

class UserType(models.Model):
    name = models.CharField(max_length=50, unique=True)

class Institution(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class User(models.Model):
    user_id = models.PositiveIntegerField(unique=True)
    user_type = models.ForeignKey(UserType, on_delete=models.CASCADE)
    institution = models.ForeignKey(Institution, on_delete=models.SET_NULL, null=True, blank=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()  # Use the custom manager

    def save(self, *args, **kwargs):
        # Ensure password is hashed before saving
        if not self.password.startswith('pbkdf2_'):  # Skip hashing if already hashed
            self.password = make_password(self.password)
        super().save(*args, **kwargs)
    
    def check_password(self, raw_password):
        if not check_password(raw_password, self.password):
            raise ValidationError("Incorrect password.")
        return True