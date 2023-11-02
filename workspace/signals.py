from django.db.models.signals import post_save
from django.dispatch import receiver
import requests

from .models import EmailUser

@receiver(post_save, sender=EmailUser)
def create_remote_mailbox(sender, instance, **kwargs):
    api_url = "http://85.239.232.186:5000/create_mailbox"
    payload = {
        'email_address': instance.email_address,
        'domain': instance.custom_user.domain.name,
    }
    try:
        response = requests.post(api_url, json=payload)
        if response.status_code != 200:
            print(f"Failed to create mailbox. Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {e}")
