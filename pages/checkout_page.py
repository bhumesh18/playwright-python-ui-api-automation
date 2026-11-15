from playwright.sync_api import Page

class CheckoutPage:
    def __init__(self, page: Page):
        self.page=page

        #Customer information locators
        self.first_name=page.get_by_placeholder("First Name")
        self.last_name=page.get_by_placeholder("Last name")
        self.zipcode=page.get_by_placeholder("Zip/Postal Code")
        self.continue_button=page.get_by_role("button", name="Continue", exact=True)
        self.finish_button=page.get_by_role("button", name="Finish", exact=True)
        self.cancel_button=page.get_by_role("button", name="Cancel", exact=True)

        #Validation and confirmation locators
        self.error_message=page.locator("[data-test='error']")
        self.page_heading=page.locator(".title")
        self.overview_items=page.locator(".cart_item")
        self.success_message=page.locator(".complete-header")

    #Enter Customer information
    def fill_customer_info(self, first,last, postal):
        self.first_name.fill(first)
        self.last_name.fill(last)
        self.zipcode.fill(postal)

    #Continue to checkout overview
    def continue_to_overview(self):
        self.continue_button.click()

    #Finish Order 
    def finish_order(self):
        self.finish_button.click()
        

        