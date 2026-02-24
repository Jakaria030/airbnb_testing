import random
import time

def step_06(page):

    try:
        next_month_button = page.locator('[aria-label="Move forward to switch to the next month."]')
        next_month_button.wait_for(timeout=5000)

        clicks = random.randint(3, 8)

        for _ in range(clicks):
            next_month_button.click()
            time.sleep(0.5)

        comment = f"Expected: Randomly navigate calendar | Outcome: Clicked 'Next Month' button {clicks} times."

        return True, comment, page.url

    except Exception as e:
        return False, f"Expected: Randomly navigate calendar | Outcome: Exception - {str(e)}", page.url