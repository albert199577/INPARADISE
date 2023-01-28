from selenium import webdriver

import os, sys
import datetime
import getpass

from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

ac = input("Please Enter Your Account :")
pw = getpass.getpass("Please Your Password :")
bp = input("Please Enter your Booking peoples :")
eat_time_num = int(input("選擇您的餐次 [1]午餐 [2]下午餐 [3]晚餐 "))
store_num = int(input("選擇您的店別 [1]微風店 [2]新莊店 "))
order_date = input("輸入您要訂餐的日期 ex:2023-01-24 ")

now = datetime.datetime.now()
year = order_date[0:4]
int_month = int(order_date[5:7])
month = order_date[5:7]

day = order_date[8:10]

ch_month = ['一月', '二月', '三月', '四月', '五月', '六月', '七月', '八月', '九月', '十月', '十一月', '十二月']
ch_month = ch_month[int_month - 1]

if month == now.strftime("%m"):
    this_month = True
else:
    this_month = False

eat_time_arr = ["wk-type-lunch", "wk-type-afternoon-tea", "wk-type-dinner"]
eat_time = eat_time_arr[eat_time_num - 1]

store_num_arr = ['li[rel="微風店"]', 'li[rel="新莊店"]']
store = store_num_arr[store_num - 1]

date = 'ul.days > li.notfull > span.notfull[data-col-date="' + order_date + '"]'
order_date_field = '.dayContainer > span[aria-label="{ch_month} {day}, {year}"]'.format(ch_month=ch_month, day=day, year=year)

# os._exit(0)

option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True) # 不自動關閉視窗
option.add_experimental_option("excludeSwitches", ["enable-logging"]) # 不顯示log

driver = webdriver.Chrome(options = option)
driver.maximize_window()

driver.get("https://www.feastogether.com.tw/booking/2") # 去到指定頁面
current_window = driver.current_window_handle
# 關閉注意事項
try:
    WebDriverWait(driver, 2000).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-news"]/div/div/div/button'))).click()
except:
    print("close error")

# 點擊會員登入
WebDriverWait(driver, 3000).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="header"]/div[2]/div/ul/li[1]'))).click()

# 填入會員帳號
ac_input = WebDriverWait(driver, 2000).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="form-login-header"]/ul/li[1]/input')))
ac_input.send_keys(ac)

# 填入會員密碼
pw_input = WebDriverWait(driver, 2000).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="form-login-header"]/ul/li[2]/input')))
pw_input.send_keys(pw)

# 點擊登入
WebDriverWait(driver, 2000).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="form-login-header"]/ul/li[4]/button'))).click()

# 關閉緊報
try:
    WebDriverWait(driver, 2000).until (EC.alert_is_present())
    alert = driver.switch_to.alert
    alert.accept()
    print("alert Exists in page")
    driver.switch_to.window(current_window)
except:
    print("alert does not Exist in page")

i = 0
while 1:
    i += 1
    try:
        # 訂位人數
        book_people = WebDriverWait(driver, 2000).until(EC.visibility_of_element_located((By.ID, "book_people")))
        # book_people = driver.find_element(By.ID, 'book_people')
        # 填上訂位人數
        book_people.send_keys(bp)

        # 點擊日期
        driver.find_element(By.CSS_SELECTOR, '.flatpickr.flatpickr-input').click()

        # 點擊下個月
        if this_month == False:
            driver.find_element(By.CLASS_NAME, 'flatpickr-next-month').click()

        # 點擊下個月最後一天
        WebDriverWait(driver, 2000).until(EC.visibility_of_element_located((By.CSS_SELECTOR, order_date_field))).click()

        # 點擊餐別
        # CSS_SELECTOR
        driver.find_element(By.CLASS_NAME, eat_time).click()

        js = "document.body.scrollTo(0, 1000);"

        driver.execute_script(js)

        driver.find_element(By.ID, 'select_store').click()

        # 點擊店別
        # CSS_SELECTOR
        WebDriverWait(driver, 2000).until(EC.visibility_of_element_located((By.CSS_SELECTOR, store))).click()

        # notfull CSS_SELECTOR calendar-li notfull active
        # <li class="calendar-li notfull active">
        #     <span class="calendar-col notfull" data-col-date="2023-01-17">
        #         <span class="tag"></span>
        #         <span class="col-date">17</span>
        #         <span class="col-seat-status">
        #             <i class="seat"></i>
        #         <span class="seat-num">即將滿席</span>
        #         </span>
        #     </span>
        # </li>

        WebDriverWait(driver, 1, 1).until(EC.visibility_of_element_located((By.CSS_SELECTOR, date))).click()
        print('Can order')
        break;
    except:
        print('Can\'t order')
        driver.refresh()
        # driver.close()
        # os._exit(0)




# 確認訂位頁
# https://www.feastogether.com.tw/booking-check


# 確認訂位按鈕 
# CSS_SELECTOR
# btn btn-large

# reCAPTCHA
# CSS_SELECTOR
# recaptcha-checkbox-border

# 時間
# 下午餐
# <li>
#     <div class="data-head">時間</div>
#     <select id="order_time">
#         <option value="">請選擇</option>
#     <option>14:30</option>
#     </select>
# </li>

# <div class="relative basic-col">
#     <div class="select">
#         <select class="wk-select form-control select-hidden" id="eat_vegetable">
#             <option>0 位</option>
#             <option>1 位</option>
#             <option>2 位</option>
#         </select>
#         <div class="select-styled">0 位</div>
#         <ul class="select-options" style="display: none;">
#             <li rel="0 位">0 位</li>
#             <li rel="1 位">1 位</li>
#             <li rel="2 位">2 位</li>
#         </ul>
#     </div>
# </div>
