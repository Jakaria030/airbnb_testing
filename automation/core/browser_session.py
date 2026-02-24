import os
import datetime
from playwright.sync_api import sync_playwright

class BrowserSession:
    def __init__(self, headless=True, slow_mo=0):
        self.playwright = None
        self.browser = None
        self.context = None
        self.page = None
        self.headless = headless
        self.slow_mo = slow_mo

    def __enter__(self):   
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(headless=self.headless, slow_mo=self.slow_mo)
        context = self.browser.new_context()
        context.clear_cookies()
        self.page = context.new_page()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.browser:
            self.browser.close()
        if self.playwright:
            self.playwright.stop()