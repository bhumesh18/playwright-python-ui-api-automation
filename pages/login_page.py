from playwright.sync_api import Page

class LoginPage: 
    def __init__(self, page: Page):
        self.page=page

        #Locators 
        self.username_input = page.get_by_placeholder("Username")
        self.password_input = page.locator("#password")
        self.login_button = page.get_by_role("button", name="Login")
        self.error_message = page.locator("[data-test='error']")
        self.page_heading = page.get_by_text("Products", exact=True)

    #Reusable login action
    
    def login(self, username, password):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()