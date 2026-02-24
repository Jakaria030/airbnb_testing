# Airbnb Automation Test

This project contains an automated test suite for validating Airbnb search functionality using Playwright. It covers selecting locations, dates, guest counts, and verifying the resulting search URL and UI updates.

---

## 🧩 Project Overview

The test suite automates the following steps:

1. **Step 01-03:** Search for a location and collect suggestion texts.
2. **Step 04:** Randomly select a location from the suggestions.
3. **Step 05:** Open the date picker modal and navigate months randomly.
4. **Step 06-07:** Select check-in and check-out dates from the calendar.
5. **Step 08-09:** Open guest selection modal and randomly select adults, children, infants, or pets.
6. **Step 10:** Click the search button to execute the search.
7. **Step 11:** Verify that the selected dates and guest count appear in the page UI.
8. **Step 12:** Validate that the dynamically generated search URL contains correct check-in, check-out, and guest parameters.

---

## 🛠️ Prerequisites

- Python 3.9+  
- Playwright 


## Getting Started
Follow these steps to set up and run the project locally:

1. Clone the repository:
    ```bash
    git clone git@github.com:Jakaria030/airbnb_testing.git
    ```
2. Navigate to the project directory:
    ```bash
    cd airbnb_testing
    ```
3. Create Virtual Environment
    ```bash
    python3 -m venv .venv # for linux
        
    python -m venv .venv # for windows
    ```
4. Activate Virtual Environment
    ```bash
    source .vevn/bin/activate # for linux
    vevn\Scripts\activate # for windows
    ```
5. Install Dependencies
    ```bash
    pip install -r requirements.txt
    ```
6. Save Intsalled Packages (optional)
    ```bash
    pip freeze > requirements.txt
    ```
7. Apply migrations
    ```bash
    python manage.py migrate
    ```
8. Run the development server
    ```bash
    python manage.py runserver
    ```

📝 Notes

- The SQLite database (db.sqlite3) is not included in the repository. Create by running migrations.

1. Create a superuser
    ```bash
    python manage.py createsuperuser
    ```
    - You will be prompted to enter:
    - Username
    - Email (optional)
    - Password

## Additional Resources
- [Django Documentation](https://docs.djangoproject.com/en/6.0/topics/)
- [Playwright Documentation](https://playwright.dev/python/docs/intro)