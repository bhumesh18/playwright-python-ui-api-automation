
import pytest
from playwright.sync_api import expect


@pytest.mark.parametrize(
    "username, password, expected_heading, expected_error",
    [
        ("standard_user", "secret_sauce", "Products", None),
        ("locked_out_user", "secret_sauce", None, "locked out"),
        ("invalid_user", "wrong123", None, "do not match"),
        ("standard_user", "wrong123", None, "do not match"),
        ("", "secret_sauce", None, "Username is required"),
        ("standard_user", "", None, "Password is required")
    ]
)


def test_login_scenarios(
    sauce_page,
    username,
    password,
    expected_heading,
    expected_error
):

    # Enter credentials
    sauce_page.locator("#user-name").fill(username)
    sauce_page.locator("#password").fill(password)

    # Click login
    sauce_page.locator("#login-button").click()

    # Verify expected result
    if expected_heading:
        expect(sauce_page.locator(".title")).to_have_text(
            expected_heading
        )

    else:
        error = sauce_page.locator("[data-test='error']")

        expect(error).to_be_visible()
        expect(error).to_contain_text(expected_error)
