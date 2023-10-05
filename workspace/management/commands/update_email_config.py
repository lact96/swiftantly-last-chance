from django.core.management.base import BaseCommand
from workspace.models import CustomUser, VirtualDomain
import subprocess

class Command(BaseCommand):
    help = 'Updates Postfix and Dovecot configurations for email users'

    def handle(self, *args, **kwargs):
        email_users = CustomUser.objects.filter(is_email_user=True)
        
        for user in email_users:
            domain = user.virtual_domain.domain_name
            email_address = f"{user.email_username}@{domain}"
            # Logic to update Postfix and Dovecot configurations
            # For demonstration, let's assume we're updating a text file that Postfix and Dovecot read from
            with open("/path/to/postfix_dovecot_user_file.txt", "a") as f:
                f.write(f"{email_address} {user.email_password}\n")
            
            # If you have specific shell commands to run, you can use subprocess like this:
            # subprocess.run(["your_shell_command_here"])
