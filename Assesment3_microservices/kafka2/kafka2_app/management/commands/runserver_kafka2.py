from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.conf import settings

class Command(BaseCommand):
    help = 'Runs the Kafka2 server on port 8001'

    def handle(self, *args, **options):
        port = getattr(settings, 'PORT', 8001)
        call_command('runserver', f'127.0.0.1:{port}')