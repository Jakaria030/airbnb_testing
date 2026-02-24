from django.core.management.base import BaseCommand
from automation.playwright_runner import playwright_runner

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('--url', type=str, help="Landing URL")

    def handle(self, *args, **options):
        self.stdout.write(self.style.WARNING("\nStarting automation tests...\n"))

        try:
            playwright_runner()
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Error running tests: {e}"))

        self.stdout.write(self.style.WARNING("\nEnd automation tests...\n"))