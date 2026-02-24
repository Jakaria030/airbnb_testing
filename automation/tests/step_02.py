import random

def step_02(page):
    try:
        countries = [
            "United States", "Canada", "United Kingdom", "Germany", "France",
            "Italy", "Spain", "Australia", "Japan", "China",
            "Brazil", "India", "Mexico", "Netherlands", "Switzerland",
            "Sweden", "Norway", "Denmark", "South Korea", "Singapore"
        ]

        selected_country = random.choice(countries)
        search_input = page.locator('[data-testid="structured-search-input-field-query"]')
        search_input.wait_for(timeout=5000)
        search_input.click()
        search_input.fill("")
        search_input.type(selected_country, delay=200)

        comment = f"Expected: Type random country name in search | Outcome: Typed '{selected_country}'"
        return True, comment, page.url

    except Exception as e:
        return False, f"Expected: Type random country name in search | Outcome: Exception - {str(e)}", page.url