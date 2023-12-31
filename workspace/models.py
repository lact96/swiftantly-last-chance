from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.core.management import call_command
from django.db.models.signals import post_save
from django.dispatch import receiver
import logging
from passlib.hash import sha512_crypt
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
    def set_password(self, raw_password):
        # Call the parent set_password method
        super().set_password(raw_password)

        if self.is_email_user:
            # Generate a new salt and hash the password
            hashed_password = sha512_crypt.using(rounds=656000).hash(raw_password)
            # Update or create the EmailUser instance
            email_user, created = EmailUser.objects.update_or_create(
                custom_user=self,
                defaults={'hashed_password': hashed_password}
            )
            email_user.save()
# Workspace Model
class Workspace(models.Model):
    owner = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='workspace_owner')
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    members = models.ManyToManyField(CustomUser, related_name='workspace_members')

    def __str__(self):
        return self.name

logger = logging.getLogger(__name__)

class EmailUser(models.Model):
    custom_user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='email_user')
    email_address = models.EmailField(unique=True)
    hashed_password = models.CharField(max_length=128)

    def save(self, *args, **kwargs):
        # No need to handle password here, it's done in CustomUser.set_password
        super().save(*args, **kwargs)
        

from django.db import models

class EmailSettings(models.Model):
    RATE_LIMIT_CHOICES = [
        ('per_minute', 'Per Minute'),
        ('per_hour', 'Per Hour'),
    ]
    ENCRYPTION_CHOICES = [
        ('TLS', 'TLS'),
        ('SSL', 'SSL'),
        ('None', 'None'),
    ]
    LOG_LEVEL_CHOICES = [
        ('Error', 'Error'),
        ('Warning', 'Warning'),
        ('Info', 'Info'),
        ('Debug', 'Debug'),
    ]

    rate_limit = models.IntegerField(default=100)
    rate_limit_type = models.CharField(max_length=10, choices=RATE_LIMIT_CHOICES, default='per_minute')
    max_attachment_size = models.IntegerField(default=10240)  # in KB
    max_recipients = models.IntegerField(default=50)
    spam_filter_level = models.IntegerField(default=1)
    auto_delete_spam = models.BooleanField(default=False)
    auto_archive_duration = models.IntegerField(default=30)  # in days
    encryption_type = models.CharField(max_length=5, choices=ENCRYPTION_CHOICES, default='TLS')
    authentication_required = models.BooleanField(default=True)
    log_level = models.CharField(max_length=10, choices=LOG_LEVEL_CHOICES, default='Info')

    def __str__(self):
        return f"Settings-{self.id}"

class EmailRule(models.Model):
    AUTO_REPLY = 'Auto-Reply'
    FORWARD = 'Forward'
    SPAM_FILTER = 'Spam Filter'
    RULE_TYPE_CHOICES = [
        (AUTO_REPLY, 'Auto-Reply'),
        (FORWARD, 'Forward'),
        (SPAM_FILTER, 'Spam Filter'),
    ]
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    rule_type = models.CharField(max_length=50, choices=RULE_TYPE_CHOICES)
    condition = models.CharField(max_length=200)
    action = models.CharField(max_length=200)

class EmailSetting(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    auto_reply = models.TextField(null=True, blank=True)
    forwarding_email = models.EmailField(null=True, blank=True)
    spam_filter_level = models.IntegerField(default=1)
    signature = models.TextField(null=True, blank=True)
    vacation_mode_start = models.DateField(null=True, blank=True)
    vacation_mode_end = models.DateField(null=True, blank=True)
    vacation_message = models.TextField(null=True, blank=True)
    read_receipt = models.BooleanField(default=False)
    email_priority = models.IntegerField(default=1)
    

@receiver(post_save, sender=CustomUser)
def create_or_update_email_user(sender, instance, created, **kwargs):
    if instance.is_email_user:
        # Generate a new salt and hash the password
        hashed_password = sha512_crypt.using(rounds=656000).hash(instance.password)
        # Update or create the EmailUser instance
        email_user, created = EmailUser.objects.update_or_create(
            custom_user=instance,
            defaults={'hashed_password': hashed_password}
        )
        email_user.save()
        
        