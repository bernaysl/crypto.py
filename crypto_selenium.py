from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

#chromeOptions = webdriver.ChromeOptions()
options = webdriver.ChromeOptions()
options.add_argument('--incognito')#gizli sekmede açması için
options.add_argument('--headless') #sekme görünürde açılmasın biz bunu görmeyelim

driver = webdriver.Chrome(options=options)
driver.maximize_window() #tam ekranda açılsın
driver.delete_all_cookies() #çerezler gelmesin

driver.get("https://tr.tradingview.com/chart/?symbol=FX_IDC%3AXAUTRYG") #bu linki aç
driver.implicitly_wait(10) #site açılınca 10 saniye bekleme süresi ver, 10 saniyeden önce açılırsa direkt işleme 
#site yüklenebilir ama fiyat bilgisi henüz yüklenmemiş olabilir o yüzden bekleme süresi koyuyorum

#sürekli değiştiği için linkin xpath'ini kopyaladım
while True:
    fiyat_bilgisi=driver.find_element("xpath","/html/body/div[2]/div[6]/div/div[1]/div[1]/div[1]/div[2]/div[2]/div/div[2]/div[2]/span[1]/span[1]")
    print(fiyat_bilgisi)
    sleep(3)
