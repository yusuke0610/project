from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep

def instagram():
    USERNAME = 'username'
    PASSWORD = 'userpass'
    #ドライバーを設定する
    driver_path = "/opt/homebrew/bin/chromedriver"
    service = Service(executable_path=driver_path)
    driver = webdriver.Chrome(service=service)
    error_flg = False
    #インスタのトップページURL
    target_url = 'https://www.instagram.com'
    driver.get(target_url)  
    sleep(3)
    print("chrome OK")
    if error_flg is False:
        try:
            username_input = driver.find_element(By.XPATH, '//input [@aria-label="電話番号、ユーザーネーム、メールアドレス"]')
            username_input.send_keys(USERNAME)
            sleep(1)
            print("ユーザーネームOK")
            
            password_input = driver.find_element(By.XPATH, '//input [@aria-label="パスワード"]')
            password_input.send_keys(PASSWORD)
            sleep(1)
            print("パスワードOK")
            
            username_input.submit()
            sleep(1)
            print("ログインOK")
            print(driver.title, driver.current_url)
            
            notnow_button = driver.find_element(By.XPATH, '//button [text()="後で"]')
            print("ここ")
            notnow_button.click()
            sleep(1)
        except Exception:
            error_flg = True
            print('ログインボタン押下時にエラーが発生しました。')
            
instagram()