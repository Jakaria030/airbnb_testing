from django.db import models
from django.utils import timezone


class TestResult(models.Model):
    testcase   = models.CharField(max_length=500)
    url        = models.URLField(max_length=2000)
    passed     = models.BooleanField(default=False)
    comment    = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        badge = 'PASS' if self.passed else 'FAIL'
        return f"{badge} | {self.testcase}"