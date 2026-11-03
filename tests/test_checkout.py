import pytest

from pages.cart_page import CartPage
from pages.checkout_complete_page import CheckoutCompletePage
from pages.checkout_info_page import CheckoutInfoPage
from pages.checkout_overview_page import CheckoutOverviewPage

BACKPACK = "Sauce Labs Backpack"


@pytest.fixture
def checkout_info_page(driver, inventory_page):
    """Tambahkan Backpack, buka keranjang, lalu masuk ke form checkout."""
    inventory_page.add_to_cart(BACKPACK)
    inventory_page.open_cart()
    CartPage(driver).click_checkout()
    return CheckoutInfoPage(driver)


class TestCheckout:
    """Kasus uji alur checkout end-to-end."""

    def test_checkout_complete_flow(self, driver, checkout_info_page):
        """TC-18: Alur checkout lengkap hingga muncul 'Thank you for your order!'."""
        checkout_info_page.fill_information("Budi", "Santoso", "51111")
        checkout_info_page.click_continue()

        overview_page = CheckoutOverviewPage(driver)
        assert overview_page.get_page_title() == "Checkout: Overview"
        assert overview_page.get_item_names() == [BACKPACK]
        overview_page.click_finish()

        complete_page = CheckoutCompletePage(driver)
        assert complete_page.get_page_title() == "Checkout: Complete!"
        assert complete_page.get_complete_header() == "Thank you for your order!"
        assert complete_page.get_current_url() == CheckoutCompletePage.URL

    def test_checkout_overview_shows_correct_subtotal(self, driver, checkout_info_page):
        """TC-19: Subtotal di ringkasan sesuai harga produk ($29.99)."""
        checkout_info_page.fill_information("Budi", "Santoso", "51111")
        checkout_info_page.click_continue()

        overview_page = CheckoutOverviewPage(driver)
        assert overview_page.get_subtotal_text() == "Item total: $29.99"

    def test_checkout_negative_empty_first_name(self, checkout_info_page):
        """TC-20: First Name kosong menampilkan pesan error."""
        checkout_info_page.fill_information("", "Santoso", "51111")
        checkout_info_page.click_continue()

        assert "Error: First Name is required" in checkout_info_page.get_error_message()

    def test_checkout_negative_empty_last_name(self, checkout_info_page):
        """TC-21: Last Name kosong menampilkan pesan error."""
        checkout_info_page.fill_information("Budi", "", "51111")
        checkout_info_page.click_continue()

        assert "Error: Last Name is required" in checkout_info_page.get_error_message()

    def test_checkout_negative_empty_postal_code(self, checkout_info_page):
        """TC-22: Postal Code kosong menampilkan pesan error."""
        checkout_info_page.fill_information("Budi", "Santoso", "")
        checkout_info_page.click_continue()

        assert "Error: Postal Code is required" in checkout_info_page.get_error_message()

    def test_checkout_cancel_returns_to_cart(self, driver, checkout_info_page):
        """TC-23: Tombol Cancel pada form checkout kembali ke keranjang."""
        checkout_info_page.click_cancel()

        cart_page = CartPage(driver)
        assert cart_page.get_page_title() == "Your Cart"
        assert cart_page.get_current_url() == CartPage.URL
