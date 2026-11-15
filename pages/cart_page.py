from playwright.sync_api import Page

class CartPage: 
    def __init__(self, page: Page):
        self.page=page

        # Cart page locators
        self.cart_items=page.locator(".cart_item")
        self.product_names=page.locator(".inventory_item_name")
        self.checkout_button=page.locator("#checkout")
        self.continue_shopping_button=page.locator("#continue-shopping")

    # Get product names
    def get_product_names(self):
        return self.product_names.all_text_contents()

    # Count cart items 
    def get_cart_count(self):
        return self.cart_items.count()

    # Remove product 
    def remove_product(self, product_slug):
        self.page.locator(
            f"[data-test='remove-{product_slug}']"
        ).click()

    # Proceed to checkout 
    def proceed_to_checkout(self):
        self.checkout_button.click()

    #Continue shopping
    def continue_shopping(self):
        self.continue_shopping_button.click() 
        