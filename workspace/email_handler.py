import imaplib
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class EmailHandler:
    def __init__(self, user_email, user_password, domain):
        self.user_email = user_email
        self.user_password = user_password
        self.domain = domain
        self.imap_server = None
        self.smtp_server = None

    def login(self):
        self.imap_server = imaplib.IMAP4_SSL(f'{self.domain}', 993)
        self.imap_server.login(self.user_email, self.user_password)
        self.smtp_server = smtplib.SMTP_SSL(f'{self.domain}', 465)
        self.smtp_server.login(self.user_email, self.user_password)

    def logout(self):
        self.imap_server.logout()
        self.smtp_server.quit()

    def send_email(self, to_email, subject, body):
        msg = MIMEMultipart()
        msg['From'] = self.user_email
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))
        self.smtp_server.sendmail(self.user_email, to_email, msg.as_string())

    def fetch_emails(self):
        self.imap_server.select('inbox')
        status, messages = self.imap_server.search(None, 'ALL')
        email_ids = messages[0].split()
        return email_ids

    def mark_as_read(self, email_id):
        self.imap_server.store(email_id, '+FLAGS', '\\Seen')

    def mark_as_unread(self, email_id):
        self.imap_server.store(email_id, '-FLAGS', '\\Seen')

    def mark_as_spam(self, email_id):
        self.imap_server.store(email_id, '+FLAGS', '\\Flagged')

    # Add your rule methods here
    
    
