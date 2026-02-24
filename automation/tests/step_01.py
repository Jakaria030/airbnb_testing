from playwright.sync_api import TimeoutError

def step_01(page):
    try:
        # Try to close modal if it appears
        try:
            modal_button_selector = 'button:has-text("Got it")'
            page.locator(modal_button_selector).wait_for(timeout=5000)
            page.locator(modal_button_selector).click()
            modal_comment = "Modal found and closed"
        except TimeoutError:
            modal_comment = "No modal appeared"

        # Return success with expected/outcome format
        comment = f"Expected: If modal found, close it | Outcome: {modal_comment}"
        return True, comment, page.url

    except Exception as e:
        return False, f"Expected: If modal found, close it | Outcome: Exception - {str(e)}", page.url