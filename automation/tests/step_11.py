def step_11(page):
    try:
        container = page.locator('[data-testid="little-search"]')
        container.wait_for(state="visible", timeout=5000)

        date_button = container.locator('[data-testid="little-search-date"]')
        date_text_locator = date_button.locator('*').filter(has_text=True)
        date_text = date_text_locator.first.inner_text().strip() if date_text_locator.count() > 0 else ""

        if not date_text:
            return False, "Expected: Date present | Outcome: Date not found.", page.url

        guest_button = container.locator('[data-testid="little-search-guests"]')
        guest_text_locator = guest_button.locator('*').filter(has_text=True)
        guest_text = guest_text_locator.last.inner_text().strip() if guest_text_locator.count() > 0 else ""

        if not guest_text:
            return False, "Expected: Guest count present | Outcome: Guest count not found.", page.url

        return True, f"Expected: Date and guest present | Outcome: Date: {date_text}, Guests: {guest_text}", page.url

    except Exception as e:
        return False, f"Expected: Date and guest present | Outcome: Exception - {str(e)}", page.url