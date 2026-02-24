import random
import time

def step_09(page):
    try:
        total_guest_target = random.randint(2, 5)

        adults_count = random.randint(1, total_guest_target - 1)
        children_count = total_guest_target - adults_count

        infants_count = random.randint(0, 2)
        pets_count = random.randint(0, 2)

        adults_btn = page.locator('[data-testid="stepper-adults-increase-button"]')
        children_btn = page.locator('[data-testid="stepper-children-increase-button"]')
        infants_btn = page.locator('[data-testid="stepper-infants-increase-button"]')
        pets_btn = page.locator('[data-testid="stepper-pets-increase-button"]')

        for _ in range(adults_count - 1):
            adults_btn.click()
            time.sleep(0.2)

        for _ in range(children_count):
            children_btn.click()
            time.sleep(0.2)

        for _ in range(infants_count):
            infants_btn.click()
            time.sleep(0.2)

        for _ in range(pets_count):
            pets_btn.click()
            time.sleep(0.2)

        selected_date_container = page.locator('[data-xray-jira-component="Guest: Search Bar"]')
        text_locator = (
            selected_date_container
                .locator('> div').nth(1)      
                .locator('> div').nth(4)     
                .locator('> div').nth(1)   
                .locator('> div').last       
                .locator('> div')
        )
        selected_text = text_locator.inner_text().strip()

        comment = f"Expected: Guests and other options select | Outcome: {selected_text}"

        return True, comment, page.url

    except Exception as e:
        return False, f"Expected: Guests and other options select | Outcome: Exception - {str(e)}", page.url