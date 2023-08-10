from django.core.mail.backends.base import BaseEmailBackend
from mailchimp_marketing import Client
import json

class MailchimpEmailBackend(BaseEmailBackend):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.client = Client()
        self.client.set_config({
            'api_key': 'YOUR_MAILCHIMP_API_KEY',
            'server': 'YOUR_MAILCHIMP_API_SERVER_PREFIX',  # e.g., 'us5', 'us2', etc.
        })

    def send_messages(self, email_messages):
        for message in email_messages:
            msg = {
                "from_email": message.from_email,
                "subject": message.subject,
                "text": message.body,
                "to": [{"email": recipient} for recipient in message.to],
            }
            response = self.client.messages.send(create_message=False, message=msg)
            print(json.dumps(response, indent=2)) 