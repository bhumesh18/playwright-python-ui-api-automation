from playwright.sync_api import expect

#Test case 1 : Verify products in cart 
def test_cart_products(cart_page):
    expect(cart_page.cart_items).to_have_count(2)

    products=cart_page.get_product_names()

    assert "Sauce Labs Backpack" in products
    assert "Sauce Labs Bike Light" in products

# Test case 2 : Remove products from cart 
def test_remove_products(cart_page):
    cart_page.remove_product("sauce-labs-backpack")
    expect(cart_page.cart_items).to_have_count(1)
    products=cart_page.get_product_names()

    assert "Sauce Labs Bike Light" in products
    assert "Sauce Labs Backpack" not in products

# Test case 3 : Continue shopping 
def test_continue_shopping(cart_page):
    cart_page.continue_shopping()
    expect(cart_page.page.locator(".title")).to_have_text("Products")


# Test case 4 : Proceed to checkout 
def test_checkout_navigation(cart_page):
    cart_page.proceed_to_checkout()
    expect(cart_page.page.locator(".title")).to_have_text("Checkout: Your Information")