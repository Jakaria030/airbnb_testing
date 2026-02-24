import threading
from django.utils import timezone
from automation.models import TestResult

def save_test_result(testcase: str, url: str, passed: bool, comment: str):
    def _save():
        TestResult.objects.create(
            testcase=testcase,
            url=url,
            passed=passed,
            comment=comment,
            created_at=timezone.now()
        )
        
    thread = threading.Thread(target=_save)
    thread.start()