import random
import time

def step_07(page):
    try:
        calendar = page.locator('div[aria-label="Calendar"][role="application"]')
        calendar.wait_for(timeout=5000)

        months = calendar.locator('> div').last.locator('> div').first.locator('> div')
        month_count = months.count()

        if month_count < 1:
            return False, "No month containers found.", page.url

        all_days = []

        for i in range(month_count):
            month = months.nth(i)
            days = month.locator('button:not([disabled])')
            day_count = days.count()

            for j in range(day_count):
                all_days.append(days.nth(j))

        if len(all_days) < 2:
            return False, "Not enough selectable dates available.", page.url

        # Randomly select check-in index
        checkin_index = random.randint(0, len(all_days) - 2)
        checkin_button = all_days[checkin_index]
    
        checkin_button.click()
        time.sleep(0.3)

        # Randomly select check-out AFTER check-in
        checkout_index = random.randint(checkin_index + 1, len(all_days) - 1)
        checkout_button = all_days[checkout_index]
  
        checkout_button.click()

        selected_date_container = page.locator('[data-xray-jira-component="Guest: Search Bar"]')
        text_locator = (
            selected_date_container
                .locator('> div').nth(1)      
                .locator('> div').nth(2)     
                .locator('> div').nth(1)   
                .locator('> div').last       
                .locator('> div')
        )
        selected_text = text_locator.inner_text().strip()

        comment = f"Expected: Select valid check-in and check-out dates | Outcome: {selected_text}"

        return True, comment, page.url

    except Exception as e:
        return False, f"Expected: Select valid check-in and check-out dates | Outcome: Exception - {str(e)}", page.url