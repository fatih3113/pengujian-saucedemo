from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):
    URL = "https://www.saucedemo.com/"

    # ======================= LOKATOR (Relative XPath) =======================
    USERNAME_INPUT = (By.XPATH, "//input[@id='user-name' or @data-test='username']")
    PASSWORD_INPUT = (By.XPATH, "//input[@id='password' or @data-test='password']")
    LOGIN_BUTTON = (By.XPATH, "//input[@type='submit' and @id='login-button']")
    ERROR_CONTAINER = (
        By.XPATH, "//h3[@data-test='error' or contains(@class, 'error-message')]"
    )
    APP_LOGO = (By.XPATH, "//div[@class='app_logo' and text()='Swag Labs']")

    def open(self):
        """Membuka halaman web login."""
        self.driver.get(self.URL)

    def enter_username(self, username: str):
        self.type_text(self.USERNAME_INPUT, username)

    def enter_password(self, password: str):
        self.type_text(self.PASSWORD_INPUT, password)

    def click_login(self):
        self.click(self.LOGIN_BUTTON)

    def login(self, username: str, password: str):
        """Metode komposit untuk menjalankan alur login lengkap."""
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def get_error_message(self) -> str:
        """Mengambil pesan kesalahan jika kredensial login gagal/salah."""
        return self.get_text(self.ERROR_CONTAINER)

    def is_dashboard_displayed(self) -> bool:
        """Validasi apakah logo dashboard inventori berhasil dirender."""
        return self.find_element(self.APP_LOGO).is_displayed()
