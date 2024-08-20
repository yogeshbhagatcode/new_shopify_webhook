"""
Production Django settings for shopify_webhook project.
"""


# pylint: disable=unnecessary-pass,unused-argument
def plugin_settings(settings):
    """
    Set of plugin settings used by the Open Edx platform.
    """
    settings.WEBHOOK_RECEIVER_SEND_ENROLLMENT_EMAIL = True
    settings.WEBHOOK_RECEIVER_AUTO_ENROLL = True
    settings.WEBHOOK_RECEIVER_LMS_BASE_URL = 'http://local.overhang.io:8000'
    settings.WEBHOOK_RECEIVER_EDX_OAUTH2_KEY = 'webhook_receiver'
    settings.WEBHOOK_RECEIVER_EDX_OAUTH2_SECRET = 'mdKEVw7gJfUS684vG9L2mm7KzUxZsY6P'

    settings.WEBHOOK_RECEIVER_SETTINGS = {
        'shopify': {
            'shop_domain': '6dc7d5-5.myshopify.com',
            'api_key': 'K3etf+v53afl8AMu6HBIRHd8lZC6OhgrWOyAi9QIUpI=',
        }
    }