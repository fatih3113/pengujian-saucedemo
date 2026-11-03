from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


class TestLogin:
    """Kumpulan kasus uji fungsional fitur autentikasi pengguna."""

    def test_login_positive_valid_user(self, driver):
        """TC-01: Login berhasil dengan kredensial valid."""
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("standard_user", "secret_sauce")

        assert login_page.is_dashboard_displayed() is True, (
            "Logo Swag Labs tidak tampil setelah login valid!"
        )
        expected_url = "https://www.saucedemo.com/inventory.html"
        actual_url = login_page.get_current_url()
        assert actual_url == expected_url, (
            f"Diharapkan '{expected_url}', tetapi berada di '{actual_url}'"
        )

    def test_login_negative_locked_out_user(self, driver):
        """TC-02: User yang diblokir (locked out) tidak bisa login."""
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("locked_out_user", "secret_sauce")

        expected_error = "Epic sadface: Sorry, this user has been locked out."
        actual_error = login_page.get_error_message()
        assert expected_error in actual_error, (
            f"Diharapkan: '{expected_error}', Diterima: '{actual_error}'"
        )

    def test_login_negative_empty_password(self, driver):
        """TC-03: Password dikosongkan menampilkan pesan wajib diisi."""
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("standard_user", "")

        expected_error = "Epic sadface: Password is required"
        actual_error = login_page.get_error_message()
        assert expected_error in actual_error, (
            f"Diharapkan: '{expected_error}', Diterima: '{actual_error}'"
        )

    def test_login_negative_empty_username(self, driver):
        """TC-04: Username dikosongkan menampilkan pesan wajib diisi."""
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("", "secret_sauce")

        expected_error = "Epic sadface: Username is required"
        actual_error = login_page.get_error_message()
        assert expected_error in actual_error, (
            f"Diharapkan: '{expected_error}', Diterima: '{actual_error}'"
        )

    def test_login_negative_wrong_password(self, driver):
        """TC-05: Password salah ditolak."""
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("standard_user", "password_salah")

        expected_error = "Username and password do not match any user in this service"
        actual_error = login_page.get_error_message()
        assert expected_error in actual_error, (
            f"Diharapkan: '{expected_error}', Diterima: '{actual_error}'"
        )

    def test_logout(self, driver, inventory_page):
        """TC-06: Logout mengembalikan user ke halaman login."""
        inventory_page.logout()

        login_page = LoginPage(driver)
        assert login_page.is_displayed(login_page.LOGIN_BUTTON)
        assert login_page.get_current_url() == LoginPage.URL
