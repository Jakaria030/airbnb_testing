from django.contrib import admin
from .models import TestResult

@admin.register(TestResult)
class TestResultAdmin(admin.ModelAdmin):
    list_display = ('testcase', 'url', 'passed', 'created_at', 'comment_summary')
    list_filter = ('passed', 'created_at')
    search_fields = ('testcase', 'comment', 'url')
    list_display_links = ('testcase',)
    readonly_fields = ('created_at',)

    def comment_summary(self, obj):
        if obj.comment:
            return obj.comment[:50] + '...' if len(obj.comment) > 50 else obj.comment
        return '-'
    comment_summary.short_description = 'Comment'