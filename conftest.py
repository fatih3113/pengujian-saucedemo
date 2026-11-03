import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


@pytest.fixture(scope="function")
def driver():
    """Inisialisasi browser Google Chrome untuk setiap fungsi pengujian."""
    options = Options()
    options.add_argument("--log-level=3")
    options.add_argument("--start-maximized")

    # Matikan popup password manager Chrome yang bisa mengganggu klik
    options.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False,
    })
    options.add_experimental_option("excludeSwitches", ["enable-automation"])

    # Jalankan tanpa GUI jika variabel lingkungan HEADLESS=1
    if os.getenv("HEADLESS") == "1":
        options.add_argument("--headless=new")
        options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=options)
    yield driver

    # Teardown: selalu tutup browser setelah tes selesai
    driver.quit()


@pytest.fixture(scope="function")
def inventory_page(driver):
    """Login sebagai standard_user lalu kembalikan InventoryPage."""
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")
    assert login_page.is_dashboard_displayed()
    return InventoryPage(driver)
