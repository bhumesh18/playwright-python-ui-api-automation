from playwright.sync_api import Page

class InventoryPage: 
    def __init__(self, page: Page):
        self.page=page

        # page locators
        self.page_heading=page.locator(".title")
        self.inventory_items=page.locator(".inventory_item")
        self.product_names=page.locator(".inventory_item_name")
        self.cart_badge=page.locator(".shopping_cart_badge")

    #Get total no. of products
    def get_product_count(self):
        return self.inventory_items.count()

    #Get all product names 
    def get_product_names(self):
        return self.product_names.all_text_contents()

    # Add product to cart 
    def add_product_to_cart(self, product_slug):
        self.page.locator(
            f"[data-test='add-to-cart-{product_slug}']"
        ).click()

