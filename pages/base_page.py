from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.common.by import By


class BasePage:
    """Kelas dasar yang diwarisi oleh seluruh halaman Page Object."""

    # Judul halaman (dipakai di Products, Your Cart, Checkout, dll.)
    PAGE_TITLE = (By.XPATH, "//span[@data-test='title']")

    def __init__(self, driver):
        self.driver = driver
        # Explicit wait default 10 detik
        self.wait = WebDriverWait(self.driver, 10)

    def find_element(self, locator):
        """Mencari elemen tunggal dengan explicit wait visibility."""
        try:
            return self.wait.until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            raise TimeoutException(
                f"Elemen dengan lokator {locator} tidak ditemukan dalam waktu tunggu."
            )

    def find_elements(self, locator):
        """Mencari banyak elemen tanpa menunggu (list kosong jika tidak ada)."""
        return self.driver.find_elements(*locator)

    def click(self, locator):
        """Menunggu elemen dapat diklik lalu melakukan aksi klik."""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def type_text(self, locator, text):
        """Mengisi teks ke input field setelah membersihkan teks sebelumnya."""
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        """Mengambil teks visual dari suatu elemen web."""
        return self.find_element(locator).text

    def get_texts(self, locator):
        """Mengambil teks dari banyak elemen sekaligus."""
        self.wait.until(EC.presence_of_all_elements_located(locator))
        return [el.text for el in self.find_elements(locator)]

    def is_displayed(self, locator) -> bool:
        """True jika elemen tampil dalam waktu tunggu."""
        try:
            return self.find_element(locator).is_displayed()
        except TimeoutException:
            return False

    def is_present(self, locator) -> bool:
        """Cek keberadaan elemen di DOM tanpa menunggu."""
        return len(self.find_elements(locator)) > 0

    def select_by_value(self, locator, value):
        """Memilih opsi dropdown berdasarkan atribut value."""
        Select(self.find_element(locator)).select_by_value(value)

    def wait_until_gone(self, locator):
        """Menunggu elemen hilang dari halaman."""
        self.wait.until(EC.invisibility_of_element_located(locator))

    def get_page_title(self) -> str:
        """Mengambil judul halaman (mis. 'Products', 'Your Cart')."""
        return self.get_text(self.PAGE_TITLE)

    def get_current_url(self):
        """Mendapatkan alamat URL browser saat ini."""
        return self.driver.current_url
