from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.core.management import call_command
from django.db.models.signals import post_save
from django.dispatch import receiver

import crypt, random, string
class VirtualDomain(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        user = self.create_user(email, password, **extra_fields)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    date_joined = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    # Additional fields
    company_name = models.CharField(max_length=100)
    company_address = models.TextField()
    is_email_user = models.BooleanField(default=False)
    domain = models.ForeignKey(VirtualDomain, on_delete=models.CASCADE, blank=True, null=True)
    
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
    


# Workspace Model
class Workspace(models.Model):
    owner = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='workspace_owner')
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    members = models.ManyToManyField(CustomUser, related_name='workspace_members')

    def __str__(self):
        return self.name
    
class EmailUser(models.Model):
    custom_user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='email_user')
    email_address = models.EmailField(unique=True)
    hashed_password = models.CharField(max_length=128)

    def save(self, *args, **kwargs):
        salt = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(8))
        self.hashed_password = crypt.crypt(self.custom_user.password, f"$6${salt}$")
        super().save(*args, **kwargs)
        
@receiver(post_save, sender=CustomUser)
def create_or_update_email_user(sender, instance, created, **kwargs):
    if instance.is_email_user:
        EmailUser.objects.get_or_create(
            custom_user=instance,
            defaults={'email_address': instance.email}
        )