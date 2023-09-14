from selenium import webdriver

import os, sys
import datetime
import getpass
import calendar

from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# restaurant = int(input("選擇您要訂購餐聽 [1]饗饗 [2]旭集 "))
# ac = input("Please Enter Your Account :")
# pw = getpass.getpass("Please Your Password :")
# bp = input("Please Enter your Booking peoples :")
# eat_time_num = int(input("選擇您的餐次 [1]午餐 [2]下午餐 [3]晚餐 "))
# if restaurant == 1:
#     store_num = int(input("選擇您的店別 [1]微風店 [2]新莊店 "))
#     url = "https://www.feastogether.com.tw/booking/Inparadise"
# else:
#     store_num = 1
#     url = "https://www.feastogether.com.tw/booking/Sunrise"

# order_date = input("輸入您要訂餐的日期 ex:2023-01-24 ")

# now = datetime.datetime.now()
# year = order_date[0:4]
# int_month = int(order_date[5:7])
# month = order_date[5:7]

# day = int(order_date[8:10])

# ch_month = ['一月', '二月', '三月', '四月', '五月', '六月', '七月', '八月', '九月', '十月', '十一月', '十二月']
# ch_month = ch_month[int_month - 1]

# if month == now.strftime("%m") or now.strftime("%Y-%m-%d") == datetime.datetime(now.year, now.month, calendar.monthrange(now.year, now.month)[1]).strftime("%Y-%m-%d"):
#     this_month = True
# else:
#     this_month = False

# eat_time_arr = ["wk-type-lunch", "wk-type-afternoon-tea", "wk-type-dinner"]
# eat_time = eat_time_arr[eat_time_num - 1]

# if restaurant == 1:
#     store_num_arr = ['li[rel="微風店"]', 'li[rel="新莊店"]']
# else:
#     store_num_arr = ['li[rel="旭集信義店"]']

# store = store_num_arr[store_num - 1]

# date = 'ul.days > li.notfull > span.notfull[data-col-date="' + order_date + '"]'
# order_date_field = '.dayContainer > span[aria-label="{ch_month} {day}, {year}"]'.format(ch_month=ch_month, day=day, year=year)

# os._exit(0)

url = "https://www.feastogether.com.tw/booking/Inparadise"

bp = int(input("Please Enter your Booking peoples :"))
# //*[@id="booking-area"]/form/div/div[3]/div[1]/div[2]/div[2]/div/div/div[3]/div[1] 微風店
# //*[@id="booking-area"]/form/div/div[3]/div[1]/div[2]/div[2]/div/div/div[3]/div[2] 新莊店
store_num = int(input("選擇您的店別 [1]微風店 [2]新莊店 "))
store = '//*[@id="booking-area"]/form/div/div[3]/div[1]/div[2]/div[2]/div/div/div[3]/div[{store}]' . format(store=store_num)

# //*[@id="popper-popper"]/div/li[2] 午餐
# //*[@id="popper-popper"]/div/li[3] 下午餐
# //*[@id="popper-popper"]/div/li[4] 晚餐
eat_time_num = int(input("選擇您的餐次 [1]午餐 [2]下午餐 [3]晚餐 "))
eat_time = '//*[@id="popper-popper"]/div/li[{time}]' . format(time=eat_time_num + 1)

order_date = input("輸入您要訂餐的日期 ex:2023-01-24 ")

def transferDate(date):
    year = int(date[0:4])
    month = int(date[5:7])
    day = int(date[8:10])
    week_list = ['星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期日']
    weekday = week_list[datetime.date(year, month, day).weekday()]

    temp = str(year) + '年' + str(month) + '月' + str(day) + '日 ' + weekday
    return temp

order_date = transferDate(order_date)

order_date_field = 'div[aria-label="Choose ' + order_date + '"]'
# aria-label="Choose 2023年9月15日 星期五"

# os._exit(0)


option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True) # 不自動關閉視窗
option.add_experimental_option("excludeSwitches", ["enable-logging"]) # 不顯示log

driver = webdriver.Chrome(options = option)
driver.maximize_window()

driver.get(url) # 去到指定頁面
current_window = driver.current_window_handle

# 點擊會員登入
WebDriverWait(driver, 3000).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/header/div/div/button[2]/div'))).click()
WebDriverWait(driver, 3000).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="login-popover"]/div[3]/div/div[1]/ul/li'))).click()

# 填入會員帳號
ac_input = WebDriverWait(driver, 2000).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mui-3"]')))
ac_input.send_keys(ac)

# 填入會員密碼
pw_input = WebDriverWait(driver, 2000).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mui-4"]')))
pw_input.send_keys(pw)

# 點擊登入
WebDriverWait(driver, 2000).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/header/div[2]/div/form/button'))).click()


i = 0
while 1:
    i += 1
    try:
        # 關閉注意事項
        try:
            WebDriverWait(driver, 2000).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/main/div[2]/div/div[1]/div[3]'))).click()
        except:
            print("close error")
        
        print("try store")
        # 點擊店別
        WebDriverWait(driver, 5000).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="booking-area"]/form/div/div[3]/div[1]/div[2]'))).click()
        # 選定店別
        WebDriverWait(driver, 2000).until(EC.visibility_of_element_located((By.XPATH, store))).click()
        # 確定
        # WebDriverWait(driver, 2000).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div[3]/div/div/div[4]/button'))).click()

        print("try people")
        # 點擊成員
        WebDriverWait(driver, 5000).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="booking-area"]/form/div/div[3]/div[2]/div[2]'))).click()
        # 選定成員
        for i in range(bp):
            WebDriverWait(driver, 2000).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="booking-area"]/form/div/div[3]/div[2]/div[2]/div[2]/div/div/div[1]/div/button[2]'))).click()
        # 確定
        # WebDriverWait(driver, 2000).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[3]/div[3]/div/div/button'))).click()
        
        print("try eat time")
        # 點擊餐別
        WebDriverWait(driver, 5000).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="booking-area"]/form/div/div[3]/div[3]/div[2]'))).click()
        # 選定餐別
        WebDriverWait(driver, 2000).until(EC.visibility_of_element_located((By.XPATH, eat_time))).click()
        # 確定
        # WebDriverWait(driver, 2000).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[3]/div[3]/div/div/button'))).click()
        
        print("try eat date")
        # 點擊餐別
        WebDriverWait(driver, 5000).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="booking-area"]/form/div/div[3]/div[4]/div[2]'))).click()
        # 選定餐別
        WebDriverWait(driver, 1, 1).until(EC.visibility_of_element_located((By.CSS_SELECTOR, order_date_field))).click()

        # 點擊搜尋
        WebDriverWait(driver, 5000).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/main/div/div[2]/div[1]/div[1]/div/form/div/div[2]/div[5]'))).click()
        
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
