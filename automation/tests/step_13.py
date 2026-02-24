def step_13(page):
    listings = []

    cards = page.locator('[itemprop="itemListElement"]')
    count = cards.count()

    for i in range(count):
        card = cards.nth(i)

        # Title (e.g. "Home in Horn")
        title_el = card.locator('[data-testid="listing-card-title"]')
        title = title_el.inner_text() if title_el.count() > 0 else None

        # Price
        price_el = card.locator('span[aria-label*="night"]')
        price = price_el.get_attribute('aria-label') if price_el.count() > 0 else None

        # Image URL
        img_el = card.locator('img[fetchpriority="high"]')
        if img_el.count() == 0:
            img_el = card.locator('picture img').first
        image_url = img_el.get_attribute('src') if img_el.count() > 0 else None

        listings.append({
            'title': title,
            'price': price,
            'image_url': image_url,
        })

    formatted_listings = ""

    for item in listings:
        formatted_listings += f"- title: {item['title']}\n"
        formatted_listings += f"- price: {item['price']}\n"
        formatted_listings += f"- img_url: {item['image_url']}\n\n"

    comment = f"Expected: All items data like title, price, image url | Outcome: \n\n{formatted_listings}"

    return True, comment, page.url