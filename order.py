from selenium import webdriver

from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# from order import order

option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True) # 不自動關閉視窗
option.add_experimental_option("excludeSwitches", ["enable-logging"]) # 不顯示log

driver = webdriver.Chrome(options = option)
driver.maximize_window()

driver.get("https://www.feastogether.com.tw/booking/2") # 去到指定頁面

i = 0
while 1:
    i += 1
    print (i)
    try:
        # 關閉注意事項
        try:
            WebDriverWait(driver, 2000).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-news"]/div/div/div/button'))).click()
        except:
            print("close error")

        # 訂位人數
        book_people = WebDriverWait(driver, 2000).until(EC.visibility_of_element_located((By.ID, "book_people")))
        # book_people = driver.find_element(By.ID, 'book_people')
        # 填上訂位人數
        book_people.send_keys('2')

        # 點擊日期
        # driver.find_element(By.XPATH, '/html/body/div[4]/div/div/div/ul/li[3]/div/input').click()
        date = driver.find_element(By.CSS_SELECTOR, ".flatpickr.flatpickr-input").click() 
        # date.send_keys('2023-02-15')

        # 點擊下個月
        driver.find_element(By.CLASS_NAME, 'flatpickr-next-month').click()

        # 點擊下個月最後一天
        # driver.find_element(By.XPATH, '/html/body/div[14]/div[2]/div/div[2]/div/span[18]').click()
        driver.find_element(By.CSS_SELECTOR, '.dayContainer > span[aria-label="二月 15, 2023"]').click()

        # 點擊晚餐
        driver.find_element(By.CLASS_NAME, 'wk-type-dinner').click()

        js = "document.body.scrollTo(0, 1000);"

        driver.execute_script(js)

        driver.find_element(By.ID, 'select_store').click()

        # driver.execute_script("window.scrollTo(0, 500);")

        WebDriverWait(driver, 1000).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "li[rel='微風店']"))).click()
        # WebDriverWait(driver, 100).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[4]/div/div/div/ul/li[5]/div/div/ul/li[2]'))).click()

        WebDriverWait(driver, 1, 0.5).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'ul.days > li.active'))).click()
        # driver.close()
        print('Can order')
        break;
    except:
        print('Can\'t order')
        driver.refresh()


