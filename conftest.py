import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from playwright.sync_api import Playwright
from api_tests.api_client import APIClient
from api_tests.config import (
    API_BASE_URL, API_TIMEOUT, AUTH_API_BASE_URL
)


#Fixture 1. Open SauceDemo
@pytest.fixture
def sauce_page(page):
    page.goto("https://www.saucedemo.com/")
    yield page

#Fixture 2. Create Loginpage object

@pytest.fixture
def login_page(sauce_page):
    return LoginPage(sauce_page)


#Fixture 3. Inventory page object 

@pytest.fixture
def inventory_page(login_page):

    #login using standard_user
    login_page.login("standard_user", "secret_sauce")

    #return inventory page object
    return InventoryPage(login_page.page)

# Fixture 4 : Cart Page object

@pytest.fixture
def cart_page(inventory_page):
    #add two products
    inventory_page.add_product_to_cart("sauce-labs-backpack")
    inventory_page.add_product_to_cart("sauce-labs-bike-light")

    #open shopping cart
    inventory_page.page.locator(".shopping_cart_link").click()

    return CartPage(inventory_page.page)

# Fixture 5 : Checkout 

@pytest.fixture
def checkout_page(cart_page):
    cart_page.proceed_to_checkout()
    return CheckoutPage(cart_page.page)


#Fixture :

# API context
@pytest.fixture(scope="session")
def api_context(playwright: Playwright):

    context = playwright.request.new_context(
        base_url=API_BASE_URL,
        timeout=API_TIMEOUT
    )

    yield context
    context.dispose()


# Authentication API context
@pytest.fixture(scope="session")
def auth_api_context(playwright: Playwright):

    context = playwright.request.new_context(
        base_url=AUTH_API_BASE_URL,
        timeout=API_TIMEOUT,
        extra_http_headers={
            "Accept": "application/json"
        }
    )

    yield context
    context.dispose()


# Reusable API client
@pytest.fixture
def api_client(api_context):

    return APIClient(api_context)