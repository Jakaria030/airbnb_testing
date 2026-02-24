import random

def step_04(page):
    try:
        container = page.locator('#bigsearch-query-location-listbox')
        container.wait_for(timeout=5000)

        options = container.locator('[role="option"]')
        count = options.count()

        if count == 0:
            return False, "No suggestions found to click.", page.url

        random_index = random.randint(0, count - 1)
        options.nth(random_index).click()

        search_input = page.locator('[data-testid="structured-search-input-field-query"]')
        selected_value = search_input.input_value()

        comment = f"Expected: Click one random suggestion | Outcome: Clicked suggestion and search box shows '{selected_value}'"
        
        return True, comment, page.url

    except Exception as e:
        return False, f"Expected: Click one random suggestion | Outcome: Exception - {str(e)}", page.url