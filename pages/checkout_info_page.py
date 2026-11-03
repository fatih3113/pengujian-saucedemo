from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CheckoutInfoPage(BasePage):
    """Checkout Step One: formulir data pembeli."""

    URL = "https://www.saucedemo.com/checkout-step-one.html"

    # ======================= LOKATOR (Relative XPath) =======================
    FIRST_NAME_INPUT = (By.XPATH, "//input[@data-test='firstName']")
    LAST_NAME_INPUT = (By.XPATH, "//input[@data-test='lastName']")
    POSTAL_CODE_INPUT = (By.XPATH, "//input[@data-test='postalCode']")
    CONTINUE_BUTTON = (By.XPATH, "//input[@data-test='continue']")
    CANCEL_BUTTON = (By.XPATH, "//button[@data-test='cancel']")
    ERROR_CONTAINER = (By.XPATH, "//h3[@data-test='error']")

    def fill_information(self, first_name: str, last_name: str, postal_code: str):
        self.type_text(self.FIRST_NAME_INPUT, first_name)
        self.type_text(self.LAST_NAME_INPUT, last_name)
        self.type_text(self.POSTAL_CODE_INPUT, postal_code)

    def click_continue(self):
        self.click(self.CONTINUE_BUTTON)

    def click_cancel(self):
        self.click(self.CANCEL_BUTTON)

    def get_error_message(self) -> str:
        return self.get_text(self.ERROR_CONTAINER)
