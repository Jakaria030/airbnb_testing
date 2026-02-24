import urllib.parse

def step_12(page):
    try:
        current_url = page.url
        parsed = urllib.parse.urlparse(current_url)
        params = urllib.parse.parse_qs(parsed.query)

        required_keys = ["checkin", "checkout", "adults"]
        optional_keys = ["children", "infants"]

        missing = []

        for key in required_keys:
            if key not in params or not params[key][0]:
                missing.append(key)

        for key in optional_keys:
            if key in params and not params[key][0]:
                missing.append(key)

        if missing:
            return False, f"Expected URL to contain {required_keys + optional_keys}, Missing: {missing}", current_url

        return True, f"Expected URL to contain date & guest parameters | Outcome: All present in URL.", current_url

    except Exception as e:
        return False, f"Expected URL to contain date & guest parameters | Outcome: Exception - {str(e)}", page.url