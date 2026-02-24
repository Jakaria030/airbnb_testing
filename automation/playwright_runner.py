from automation.core.browser_session import BrowserSession
from automation.utils.db_helper import save_test_result
from automation.tests.step_01 import step_01
from automation.tests.step_02 import step_02
from automation.tests.step_03 import step_03

def playwright_runner():
    with BrowserSession(headless=False, slow_mo=200) as session:
        page = session.page
        page.goto("https://www.airbnb.com/")
    
        tests = [
            ("Step_01 - close modal", step_01),
            ("Step_02 - type country in search", step_02),
            ("Step_03 - collect suggestion countries", step_03),
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