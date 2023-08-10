from django.core.mail.backends.base import BaseEmailBackend


class MailchimpEmailBackend(BaseEmailBackend):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.client = Client()
        self.client.set_config({
            'api_key': 'YOUR_MAILCHIMP_API_KEY',
            'server': 'YOUR_MAILCHIMP_API_SERVER_PREFIX',  # e.g., 'us5', 'us2', etc.
        })

    