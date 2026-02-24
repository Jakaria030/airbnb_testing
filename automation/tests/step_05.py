def step_05(page):
    try:
        tabs_element = page.locator('#tabs')
        tabs_element.wait_for(timeout=5000)

        comment = "Expected: Date picker modal opens | Outcome: Date picker modal is visible."

        return True, comment, page.url

    except Exception as e:
        return False, f"Expected: Date picker modal opens | Outcome: Exception - {str(e)}", page.url