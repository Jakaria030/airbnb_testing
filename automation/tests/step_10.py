def step_10(page):
    try:
        search_button = page.locator('[data-testid="structured-search-input-search-button"]')
        search_button.wait_for(timeout=5000)
        search_button.click()

        comment = "Expected: Click Search button | Outcome: Search button clicked successfully."

        return True, comment, page.url

    except Exception as e:
        return False, f"Expected: Click Search button | Outcome: Exception - {str(e)}", page.url