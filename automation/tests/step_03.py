def step_03(page):
    try:
        container = page.locator('#bigsearch-query-location-listbox')
        container.wait_for(timeout=5000)

        options = container.locator('[role="option"]')
        count = options.count()

        suggestions = []
        for i in range(count):
            option = options.nth(i)
            text = option.inner_text().strip()
            if text:
                clean_text = " ".join(text.split())
                if clean_text not in suggestions:
                    suggestions.append(clean_text)

        formatted_list = "\n".join(f"- {text}" for text in suggestions)

        comment = f"Expected: Collect all suggestion texts | Outcome: Collected {len(suggestions)} items\n{formatted_list}"
        return True, comment, page.url

    except Exception as e:
        return False, f"Expected: Collect all suggestion texts | Outcome: Exception - {str(e)}", page.url