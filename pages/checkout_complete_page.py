from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CheckoutCompletePage(BasePage):
    """Halaman konfirmasi pesanan selesai."""

    URL = "https://www.saucedemo.com/checkout-complete.html"

    # ======================= LOKATOR (Relative XPath) =======================
    COMPLETE_HEADER = (By.XPATH, "//h2[@data-test='complete-header']")
    COMPLETE_TEXT = (By.XPATH, "//div[@data-test='complete-text']")
    BACK_HOME_BUTTON = (By.XPATH, "//button[@data-test='back-to-products']")

    def get_complete_header(self) -> str:
        return self.get_text(self.COMPLETE_HEADER)

    def click_back_home(self):
        self.click(self.BACK_HOME_BUTTON)
