from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CheckoutOverviewPage(BasePage):
    """Checkout Step Two: ringkasan pesanan."""

    URL = "https://www.saucedemo.com/checkout-step-two.html"

    # ======================= LOKATOR (Relative XPath) =======================
    ITEM_NAMES = (By.XPATH, "//div[@data-test='inventory-item-name']")
    SUBTOTAL_LABEL = (By.XPATH, "//div[@data-test='subtotal-label']")
    TAX_LABEL = (By.XPATH, "//div[@data-test='tax-label']")
    TOTAL_LABEL = (By.XPATH, "//div[@data-test='total-label']")
    FINISH_BUTTON = (By.XPATH, "//button[@data-test='finish']")
    CANCEL_BUTTON = (By.XPATH, "//button[@data-test='cancel']")

    def get_item_names(self):
        return self.get_texts(self.ITEM_NAMES)

    def get_subtotal_text(self) -> str:
        return self.get_text(self.SUBTOTAL_LABEL)

    def get_total_text(self) -> str:
        return self.get_text(self.TOTAL_LABEL)

    def click_finish(self):
        self.click(self.FINISH_BUTTON)

    def click_cancel(self):
        self.click(self.CANCEL_BUTTON)
