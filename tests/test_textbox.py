from pages.text_box_page import TextBoxPage
from utils.loggers import log_info

log_info("Test started")

def test_fill_text_box(setup):
    page = setup
    text_box = TextBoxPage(page)
    text_box.open_url("https://demoqa.com/text-box")

    full_name = "Gopal Sakhiya"
    email = "gopal@yopmail.com"
    current_address = "44/1 Bharat Apartment, 4C 5th Main Road, Jayanagar, Bangalore 560041, KA, IND"
    permanent_address = "44/1 Bharat Apartment, 4C 5th Main Road, Jayanagar, Bangalore 560041, KA, IND"

    text_box.fill_form(full_name, email, current_address, permanent_address)
    page.wait_for_timeout(3000)

    results = text_box.get_result()

    assert results["name"] == full_name, f"Expected '{full_name}',but got '{results['name']}'"
    assert results["email"] == email, f"Expected '{email}',but got '{results['email']}'"
    assert results["current_address"] == current_address, f"Expected '{current_address}, but got '{results["current_address"]}'"
    assert results["permanent_address"] == permanent_address, f"Expected '{permanent_address}',but got '{results["permanent_address"]}'"

    print(f"Extracted Name: {results['name']}")
    print(f"Actual Email: {results['email']}")
    print(f"Actual Current Address: {results['current_address']}")
    print(f"Actual Permanent Address: {results['permanent_address']}")
