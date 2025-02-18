from utils.base_page import BasePage

class TextBoxPage(BasePage):
    FULL_NAME = "input[placeholder='Full Name']"
    EMAIL = "input[placeholder='name@example.com']"
    CURRENT_ADDRESS = "#currentAddress"
    PERMANENT_ADDRESS = "#permanentAddress"
    SUBMIT_BUTTON = "text='Submit'"
    RESULT_NAME = "#name"
    RESULT_EMAIL = "#email"
    RESULT_CURRENT_ADDRESS = "//p[@id='currentAddress']"
    RESULT_PERMANENT_ADDRESS = "//p[@id='permanentAddress']"

    def fill_form(self, full_name, email, current_address, permanent_address):
        self.fill_text(self.FULL_NAME, full_name)
        self.fill_text(self.EMAIL, email)
        self.fill_text(self.CURRENT_ADDRESS ,current_address)
        self.fill_text(self.PERMANENT_ADDRESS, permanent_address)
        self.click_element(self.SUBMIT_BUTTON)

    def get_result(self):
        return {
            "name":self.get_text(self.RESULT_NAME).replace("Name:", "").strip(),
            "email":self.get_text(self.RESULT_EMAIL).replace("Email:","").strip(),
            "current_address":self.get_text(self.RESULT_CURRENT_ADDRESS).replace("Current Address :", "").strip(),
            "permanent_address":self.get_text(self.RESULT_PERMANENT_ADDRESS).replace("Permananet Address :", "").strip()
        }