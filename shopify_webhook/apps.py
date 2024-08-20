"""
shopify_webhook Django application initialization.
"""

from django.apps import AppConfig


class ShopifyWebhookConfig(AppConfig):
    """
    Configuration for the shopify_webhook Django application.
    """

    name = 'shopify_webhook'

    plugin_app = {
        'url_config': {
            'lms.djangoapp': {
                'namespace': 'shopify_webhook',
                'regex': '^webhooks/',
                'relative_path': 'urls',
            }
        },
        'settings_config': {
            'lms.djangoapp': {
                'common': {'relative_path': 'settings'},
                'production': {'relative_path': 'settings'},
            }
        },
    } 
