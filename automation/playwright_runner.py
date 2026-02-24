from dotenv import load_dotenv
import os
from automation.core.browser_session import BrowserSession
from automation.utils.db_helper import save_test_result
from automation.tests.step_01 import step_01
from automation.tests.step_02 import step_02
from automation.tests.step_03 import step_03
from automation.tests.step_04 import step_04
from automation.tests.step_05 import step_05
from automation.tests.step_06 import step_06
from automation.tests.step_07 import step_07
from automation.tests.step_08 import step_08
from automation.tests.step_09 import step_09
from automation.tests.step_10 import step_10
from automation.tests.step_11 import step_11
from automation.tests.step_12 import step_12
from automation.tests.step_13 import step_13

load_dotenv()
def playwright_runner():
    with BrowserSession(headless=os.getenv("HEADLESS", "True").lower() == "true", slow_mo=int(os.getenv("SLOW_MO", 0))) as session:
        page = session.page
        page.goto(os.getenv("BASE_URL", "https://www.airbnb.com/"))
    
        tests = [
            ("Step_01 - close modal", step_01),
            ("Step_02 - type country in search", step_02),
            ("Step_03 - collect suggestion countries", step_03),
            ("Step_04 - click one suggestion coumtry", step_04),
            ("Step_05 - verify date picker", step_05),
            ("Step_06 - randomly navigate calendar", step_06),
            ("Step_07 - check-in check-out date select", step_07),
            ("Step_08 - verify guest modal", step_08),
            ("Step_09 - select guest and other options", step_09),
            ("Step_10 - click the search button", step_10),
            ("Step_10.1 - close modal", step_01),
            ("Step_11 - verify date and guests", step_11),
            ("Step_12 - verify url", step_12),
            ("Step_13 - scrape data", step_13),
        ]

        try:
            for test_name, test_func in tests:
                passed, comment, url = test_func(page)

                save_test_result(
                    testcase=test_name,
                    url=url,
                    passed=passed,
                    comment=comment
                )
                print(f"Test Name: {test_name} | Status: {"PASS" if passed else "FAIL"} | {comment}")
        except Exception as e:
            save_test_result(
                testcase=test_name,
                url=url,
                passed=False,
                comment=comment
            )
            print(f"Test Name: {test_name} | Status: FAIL | Error: {e}")