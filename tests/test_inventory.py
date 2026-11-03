from pages.inventory_page import InventoryPage

BACKPACK = "Sauce Labs Backpack"
BIKE_LIGHT = "Sauce Labs Bike Light"


class TestInventory:
    """Kasus uji halaman daftar produk."""

    def test_inventory_page_displays_six_products(self, inventory_page):
        """TC-07: Halaman Products menampilkan 6 produk."""
        assert inventory_page.get_page_title() == "Products"
        assert inventory_page.get_product_count() == 6

    def test_add_single_item_updates_cart_badge(self, inventory_page):
        """TC-08: Menambah 1 produk membuat badge keranjang bernilai 1."""
        inventory_page.add_to_cart(BACKPACK)

        assert inventory_page.get_cart_count() == 1
        assert inventory_page.is_remove_button_displayed(BACKPACK)

    def test_add_two_items_updates_cart_badge(self, inventory_page):
        """TC-09: Menambah 2 produk membuat badge keranjang bernilai 2."""
        inventory_page.add_to_cart(BACKPACK)
        inventory_page.add_to_cart(BIKE_LIGHT)

        assert inventory_page.get_cart_count() == 2

    def test_remove_item_clears_cart_badge(self, inventory_page):
        """TC-10: Menghapus produk dari halaman inventori menghilangkan badge."""
        inventory_page.add_to_cart(BACKPACK)
        inventory_page.remove_from_cart(BACKPACK)

        assert inventory_page.get_cart_count() == 0

    def test_sort_name_z_to_a(self, inventory_page):
        """TC-11: Sort Name (Z to A) mengurutkan nama secara menurun."""
        inventory_page.sort_by("za")
        names = inventory_page.get_product_names()

        assert names == sorted(names, reverse=True)

    def test_sort_price_low_to_high(self, inventory_page):
        """TC-12: Sort Price (low to high) mengurutkan harga menaik."""
        inventory_page.sort_by("lohi")
        prices = inventory_page.get_product_prices()

        assert prices == sorted(prices)
