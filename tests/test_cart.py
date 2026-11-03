import pytest

from pages.cart_page import CartPage
from pages.checkout_info_page import CheckoutInfoPage
from pages.inventory_page import InventoryPage

BACKPACK = "Sauce Labs Backpack"
BIKE_LIGHT = "Sauce Labs Bike Light"


@pytest.fixture
def cart_page(driver, inventory_page):
    """Tambahkan Backpack lalu buka halaman keranjang."""
    inventory_page.add_to_cart(BACKPACK)
    inventory_page.open_cart()
    return CartPage(driver)


class TestCart:
    """Kasus uji halaman keranjang belanja."""

    def test_cart_displays_added_item(self, cart_page):
        """TC-13: Produk yang ditambahkan muncul di keranjang."""
        assert cart_page.get_page_title() == "Your Cart"
        assert cart_page.get_item_names() == [BACKPACK]
        assert "cart.html" in cart_page.get_current_url()

    def test_cart_displays_multiple_items(self, driver, inventory_page):
        """TC-14: Dua produk yang ditambahkan muncul semuanya di keranjang."""
        inventory_page.add_to_cart(BACKPACK)
        inventory_page.add_to_cart(BIKE_LIGHT)
        inventory_page.open_cart()

        cart_page = CartPage(driver)
        assert sorted(cart_page.get_item_names()) == sorted([BACKPACK, BIKE_LIGHT])

    def test_remove_item_from_cart(self, cart_page):
        """TC-15: Menghapus produk membuat keranjang kosong."""
        cart_page.remove_item(BACKPACK)

        assert cart_page.get_item_names() == []

    def test_continue_shopping_returns_to_inventory(self, driver, cart_page):
        """TC-16: Tombol Continue Shopping kembali ke halaman Products."""
        cart_page.click_continue_shopping()

        inventory_page = InventoryPage(driver)
        assert inventory_page.get_page_title() == "Products"
        assert inventory_page.get_current_url() == InventoryPage.URL

    def test_checkout_button_opens_step_one(self, driver, cart_page):
        """TC-17: Tombol Checkout membuka form data pembeli."""
        cart_page.click_checkout()

        info_page = CheckoutInfoPage(driver)
        assert info_page.get_page_title() == "Checkout: Your Information"
        assert info_page.get_current_url() == CheckoutInfoPage.URL
