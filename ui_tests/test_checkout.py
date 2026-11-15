from playwright.sync_api import expect

#Test case 1 : Successful Checkout 
def test_successful_checkout(checkout_page):
    checkout_page.fill_customer_info(
        "Test", "User", "201301"
    )
    checkout_page.continue_to_overview()
    #Validate overview page
    expect(checkout_page.page_heading).to_have_text("Checkout: Overview")

    #Verify two products are present 
    expect(checkout_page.overview_items).to_have_count(2)

    #Finish Order
    checkout_page.finish_order()

    #Validate order confirmation 
    expect(checkout_page.success_message).to_have_text("Thank you for your order!")

# Test Case 2 : Empty First name validation
def test_empty_first_name(checkout_page):
    checkout_page.continue_to_overview()
    expect(checkout_page.error_message).to_be_visible()
    expect(checkout_page.error_message).to_contain_text("First Name is required")

# Test Case 3: Empty postal code validation
def test_empty_postal_code(checkout_page):

    checkout_page.fill_customer_info(
        "Test",
        "User",
        ""
    )

    checkout_page.continue_to_overview()
    expect(checkout_page.error_message).to_be_visible()
    expect(checkout_page.error_message).to_contain_text(
        "Postal Code is required"
    )
