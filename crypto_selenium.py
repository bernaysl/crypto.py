from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

options = webdriver.ChromeOptions()
options.add_argument('--incognito')  # Gizli sekmede açması için
options.add_argument('--headless')  # Sekme görünürde açılmasın

driver = webdriver.Chrome(options=options)
driver.maximize_window()  # Tam ekranda açılsın
driver.delete_all_cookies()  # Çerezler gelmesin

driver.get("https://tr.tradingview.com/chart/?symbol=FX_IDC%3AXAUTRYG")  # Bu linki aç
driver.implicitly_wait(10)  # Site açılınca 10 saniye bekleme süresi ver

# Sürekli değiştiği için XPath'i kullanarak fiyat bilgisini al
xpath = '/html/body/div[2]/div[6]/div/div[2]/div[1]/div[1]/div[2]/div[2]/div/div[2]/div[2]/span[1]/span[1]'
while True:
    fiyat_bilgisi = driver.find_element(By.XPATH, xpath).text  # .text ile öğenin metin içeriğini al
    print(fiyat_bilgisi)
    sleep(3)
