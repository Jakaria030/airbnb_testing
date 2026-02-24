def step_01(page):
    title = page.title()
    return True, f"Expected: Homepage loaded and title get | Outcome: {title}", page.url