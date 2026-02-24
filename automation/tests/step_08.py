def step_08(page):
    try:
        selected_date_container = page.locator('[data-xray-jira-component="Guest: Search Bar"]')
        selected_date_container.locator('> div').nth(1).locator('> div').nth(4).click()

        adults_row = page.locator('[data-testid="search-block-filter-stepper-row-adults"]')
        adults_row.wait_for(timeout=5000)

        all_rows = page.locator('[data-testid^="search-block-filter-stepper-row-"]')
        row_count = all_rows.count()

        comment = f"Expected: Open guest selection modal | Outcome: Modal opened successfully with {row_count} guest row options."

        return True, comment, page.url

    except Exception as e:
        return False, f"Expected: Open guest selection modal | Outcome: Exception - {str(e)}", page.url