from playwright.sync_api import expect

 # Test 1 : Verify inventory page
def test_inventory_page(inventory_page):
       expect(inventory_page.page_heading).to_have_text("Products")

 # Test 2 : Verify product count and names 
def test_product_listing(inventory_page):
       expect(inventory_page.inventory_items).to_have_count(6)
       product_names=inventory_page.get_product_names()
       assert "Sauce Labs Backpack" in product_names
       print("Product listing validation passed")

 # Test 3 : Add product to cart
def test_add_product_to_cart(inventory_page):
       inventory_page.add_product_to_cart("sauce-labs-backpack")
       expect(inventory_page.cart_badge).to_have_text("1")
       print("Product added to cart successfully")