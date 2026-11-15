from playwright.sync_api import expect

# Test case 1 : Valid login
def test_valid_login(login_page):
    login_page.login("standard_user", "secret_sauce")
    expect(login_page.page_heading).to_have_text("Products")


# Test case 2  : Locked out user 
def test_locked_out(login_page): 
    login_page.login("locked_out_user","secret_sauce")
    expect(login_page.error_message).to_be_visible()
    expect(login_page.error_message).to_contain_text("locked out")

# Test case 3 : Invalid user 
def test_invalid_user(login_page):
    login_page.login("invalid_user", "wrong123")
    expect(login_page.error_message).to_be_visible()
    expect(login_page.error_message).to_contain_text("do not match")