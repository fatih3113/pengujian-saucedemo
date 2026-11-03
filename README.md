# Pengujian Otomasi SauceDemo (Selenium + Pytest + POM)

Otomasi pengujian aplikasi e-commerce https://www.saucedemo.com/ menggunakan
Python, Selenium WebDriver, dan Pytest dengan pola Page Object Model (POM).

## Struktur
```
pengujian_aplikasi/
├── pages/        # Page Object (lokator Relative XPath + aksi halaman)
├── tests/        # Kasus uji (hanya logika dan assertion)
├── conftest.py   # Fixture driver dan login
├── pytest.ini
└── requirements.txt
```

## Menjalankan
```bash
python -m venv venv
venv\Scripts\activate          # Windows  (Mac/Linux: source venv/bin/activate)
pip install -r requirements.txt
pytest                         # jalankan semua tes
HEADLESS=1 pytest              # tanpa jendela browser (Mac/Linux)
```
Butuh Google Chrome terpasang. Selenium 4 mengunduh chromedriver otomatis.

## Anggota Kelompok
| Nama | NIM |
|------|-----|
|      |     |
