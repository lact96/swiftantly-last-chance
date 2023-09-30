from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone

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
    
    # SMTP and IMAP for OWN SMTP User
    smtp_server = models.CharField(max_length=100, blank=True, null=True)
    imap_server = models.CharField(max_length=100, blank=True, null=True)
    smtp_port = models.IntegerField(blank=True, null=True)
    imap_port = models.IntegerField(blank=True, null=True)
    smtp_username = models.CharField(max_length=100, blank=True, null=True)
    smtp_password = models.CharField(max_length=100, blank=True, null=True)
    imap_username = models.CharField(max_length=100, blank=True, null=True)
    imap_password = models.CharField(max_length=100, blank=True, null=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

# Workspace Model
class Workspace(models.Model):
    owner = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='workspace_owner')
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    members = models.ManyToManyField(CustomUser, related_name='workspace_members')

    def __str__(self):
        return self.name