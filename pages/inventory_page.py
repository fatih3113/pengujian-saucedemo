from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class InventoryPage(BasePage):
    URL = "https://www.saucedemo.com/inventory.html"

    # ======================= LOKATOR (Relative XPath) =======================
    INVENTORY_ITEMS = (By.XPATH, "//div[@data-test='inventory-item']")
    ITEM_NAMES = (By.XPATH, "//div[@data-test='inventory-item-name']")
    ITEM_PRICES = (By.XPATH, "//div[@data-test='inventory-item-price']")
    SORT_DROPDOWN = (By.XPATH, "//select[@data-test='product-sort-container']")
    CART_LINK = (By.XPATH, "//a[@data-test='shopping-cart-link']")
    CART_BADGE = (By.XPATH, "//span[@data-test='shopping-cart-badge']")
    MENU_BUTTON = (By.XPATH, "//button[@id='react-burger-menu-btn']")
    LOGOUT_LINK = (By.XPATH, "//a[@id='logout_sidebar_link']")

    # ---------- Lokator dinamis (tergantung nama produk) ----------
    @staticmethod
    def _slug(product_name: str) -> str:
        """'Sauce Labs Backpack' -> 'sauce-labs-backpack'."""
        return product_name.lower().replace(" ", "-")

    def _add_button(self, product_name: str):
        return (By.XPATH, f"//button[@data-test='add-to-cart-{self._slug(product_name)}']")

    def _remove_button(self, product_name: str):
        return (By.XPATH, f"//button[@data-test='remove-{self._slug(product_name)}']")

    # ---------- Aksi ----------
    def add_to_cart(self, product_name: str):
        self.click(self._add_button(product_name))

    def remove_from_cart(self, product_name: str):
        self.click(self._remove_button(product_name))
        self.wait_until_gone(self._remove_button(product_name))

    def is_remove_button_displayed(self, product_name: str) -> bool:
        return self.is_displayed(self._remove_button(product_name))

    def open_cart(self):
        self.click(self.CART_LINK)

    def sort_by(self, value: str):
        """value: az, za, lohi, hilo."""
        self.select_by_value(self.SORT_DROPDOWN, value)

    def logout(self):
        self.click(self.MENU_BUTTON)
        self.click(self.LOGOUT_LINK)

    # ---------- Pengambilan data ----------
    def get_product_count(self) -> int:
        self.find_element(self.INVENTORY_ITEMS)
        return len(self.find_elements(self.INVENTORY_ITEMS))

    def get_product_names(self):
        return self.get_texts(self.ITEM_NAMES)

    def get_product_prices(self):
        """Mengembalikan daftar harga dalam bentuk float."""
        return [float(p.replace("$", "")) for p in self.get_texts(self.ITEM_PRICES)]

    def get_cart_count(self) -> int:
        """Jumlah di badge keranjang; 0 jika badge tidak ada."""
        if self.is_present(self.CART_BADGE):
            return int(self.get_text(self.CART_BADGE))
        return 0
