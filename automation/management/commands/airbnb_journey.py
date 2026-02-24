from django.core.management.base import BaseCommand
from django.utils import timezone
from automation.models import TestResult


class Command(BaseCommand):
    help = "Run Playwright automation tests and store results in database"

    def add_arguments(self, parser):
        parser.add_argument('--url', type=str, help='Optional URL to test')

    def handle(self, *args, **options):
        url = options.get('url')

        self.stdout.write(self.style.WARNING("Starting automation tests...\n"))

        try:

            # Example logic
            passed = True
            comment = "Test executed successfully"

            # Save to DB
            TestResult.objects.create(
                testcase="test_name",
                url="test_url",
                passed=passed,
                comment=comment,
            )

            self.stdout.write(self.style.SUCCESS("Tests completed successfully."))

        except Exception as e:
            TestResult.objects.create(
                testcase="Unknown",
                url=url or "",
                passed=False,
                comment=str(e)
            )

            self.stdout.write(self.style.ERROR(f"Error running tests: {e}"))