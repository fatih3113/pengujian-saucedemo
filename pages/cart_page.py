from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CartPage(BasePage):
    URL = "https://www.saucedemo.com/cart.html"

    # ======================= LOKATOR (Relative XPath) =======================
    CART_ITEMS = (By.XPATH, "//div[@data-test='inventory-item']")
    ITEM_NAMES = (By.XPATH, "//div[@data-test='inventory-item-name']")
    CHECKOUT_BUTTON = (By.XPATH, "//button[@data-test='checkout']")
    CONTINUE_SHOPPING_BUTTON = (By.XPATH, "//button[@data-test='continue-shopping']")

    def _remove_button(self, product_name: str):
        slug = product_name.lower().replace(" ", "-")
        return (By.XPATH, f"//button[@data-test='remove-{slug}']")

    def get_item_names(self):
        """Daftar nama produk di keranjang (kosong jika tidak ada)."""
        self.get_page_title()  # pastikan halaman sudah termuat
        return [el.text for el in self.find_elements(self.ITEM_NAMES)]

    def remove_item(self, product_name: str):
        self.click(self._remove_button(product_name))
        self.wait_until_gone(self._remove_button(product_name))

    def click_checkout(self):
        self.click(self.CHECKOUT_BUTTON)

    def click_continue_shopping(self):
        self.click(self.CONTINUE_SHOPPING_BUTTON)
