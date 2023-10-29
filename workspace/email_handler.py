import imaplib
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from django.contrib.auth import get_user_model
from workspace.models import EmailRule, EmailSetting, EmailUser

User = get_user_model()

class EmailHandler:
    def __init__(self, email_user):
        self.user = email_user.custom_user
        self.email = email_user.email_address
        self.password = email_user.hashed_password  # Postfix-compatible password
        self.domain = self.user.domain.name  # Assuming VirtualDomain has a 'name' field
        self.imap_server = imaplib.IMAP4_SSL(self.domain, 993)
        self.smtp_server = smtplib.SMTP_SSL(self.domain, 465)

    def login(self):
        try:
            self.imap_server.login(self.email, self.password)
            self.smtp_server.login(self.email, self.password)
        except Exception as e:
            print(f"An error occurred: {e}")

    def logout(self):
        self.imap_server.logout()
        self.smtp_server.quit()

    def send_email(self, to_email, subject, body):
        msg = MIMEMultipart()
        msg['From'] = self.email
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))
        self.smtp_server.sendmail(self.email, to_email, msg.as_string())

    def fetch_email(self):
        self.imap_server.select('inbox')
        status, messages = self.imap_server.search(None, 'ALL')
        email_ids = messages[0].split()
        return email_ids

    def mark_as_read(self, email_id):
        self.imap_server.store(email_id, '+FLAGS', '\\Seen')

    def mark_as_unread(self, email_id):
        self.imap_server.store(email_id, '-FLAGS', '\\Seen')

    def mark_as_spam(self, email_id):
        self.imap_server.copy(email_id, 'Spam')
        self.imap_server.store(email_id, '+FLAGS', '\\Deleted')
        self.imap_server.expunge()

    def move_to_folder(self, email_id, folder_name):
        self.imap_server.copy(email_id, folder_name)
        self.imap_server.store(email_id, '+FLAGS', '\\Deleted')
        self.imap_server.expunge()

    def forward_email(self, email_id, forward_to):
        status, msg_data = self.imap_server.fetch(email_id, '(RFC822)')
        raw_email = msg_data[0][1]
        self.smtp_server.sendmail(self.email, forward_to, raw_email)

    def reply_email(self, email_id, reply_body):
        status, msg_data = self.imap_server.fetch(email_id, '(BODY[HEADER.FIELDS (FROM SUBJECT)])')
        msg_header = msg_data[0][1].decode('utf-8')
        msg = MIMEMultipart()
        msg['From'] = self.email
        msg['To'] = self.email  # Extract the 'From' from msg_header
        msg['Subject'] = "Re: "  # Extract the 'Subject' from msg_header
        msg.attach(MIMEText(reply_body, 'plain'))
        self.smtp_server.sendmail(self.email, self.email, msg.as_string())  # Replace self.email with the extracted 'From'

    def set_auto_reply(self, message):
        setting = EmailSetting.objects.get(user=self.user)
        setting.auto_reply = message
        setting.save()

    def set_forwarding(self, forward_email):
        setting = EmailSetting.objects.get(user=self.user)
        setting.forwarding_email = forward_email
        setting.save()

    def set_spam_filter(self, level):
        setting = EmailSetting.objects.get(user=self.user)
        setting.spam_filter_level = level
        setting.save()

    def set_signature(self, signature):
        setting = EmailSetting.objects.get(user=self.user)
        setting.signature = signature
        setting.save()

    def set_vacation_mode(self, start_date, end_date, message):
        setting = EmailSetting.objects.get(user=self.user)
        setting.vacation_mode_start = start_date
        setting.vacation_mode_end = end_date
        setting.vacation_message = message
        setting.save()

    def set_read_receipt(self):
        setting = EmailSetting.objects.get(user=self.user)
        setting.read_receipt = True
        setting.save()

    def set_priority(self, level):
        setting = EmailSetting.objects.get(user=self.user)
        setting.email_priority = level
        setting.save()

    def set_folder_rule(self, folder_name, condition):
        rule = EmailRule(user=self.user, rule_type='Move to Folder', condition=condition, action=folder_name)
        rule.save()
