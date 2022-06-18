from re import X
from seleniumwire import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import os, random
from multiprocessing import Pool
from selenium.webdriver.chrome.options import Options
 
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
 
cwd = os.getcwd()
mobile_emulation = {
    "deviceMetrics": { "width": 360, "height": 650, "pixelRatio": 3.4 },
    }
opts = Options()
opts.headless = True
opts.add_argument('log-level=3') 
dc = DesiredCapabilities.CHROME
dc['loggingPrefs'] = {'driver': 'OFF', 'server': 'OFF', 'browser': 'OFF'}
# /user-bot:robot@gate.smartproxy.com:7000
opts.add_experimental_option('excludeSwitches', ['enable-logging'])
opts.add_argument('--ignore-certifcate-errors-spki-list')
 
path_browser = f"{cwd}\chromedriver.exe"
opts.add_argument('--disable-setuid-sandbox')
opts.add_argument('disable-infobars')
opts.add_argument('--ignore-certifcate-errors')
opts.add_argument('--ignore-certifcate-errors-spki-list')
opts.add_argument("--mute-audio")
opts.add_argument('--no-first-run')
opts.add_argument('--disable-dev-shm-usage')
opts.add_argument("--disable-infobars")
opts.add_argument('--log-level=3') 
opts.add_argument('--disable-blink-features=AutomationControlled')
opts.add_experimental_option("useAutomationExtension", False)
opts.add_experimental_option("excludeSwitches",["enable-automation"])
opts.add_experimental_option('excludeSwitches', ['enable-logging'])
opts.add_argument('--disable-notifications')
opts.add_argument('--disable-gpu')
opts.add_experimental_option("mobileEmulation", mobile_emulation)
opts.add_argument(f"user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.1.12 Safari/537.3")


def claim(data):
    port = f"1{random.randint(1111,9999)}"
    proxy_options = {
        'proxy': {
            'http': f'http://Uzilil666:Poker123@gate.smartproxy.com:{port}',
            'https': f'https://Uzilil666:Poker123@gate.smartproxy.com:{port}'
        
           },
        'no_proxy': 'localhost,127.0.0.1',
        "backend": "default",
        'mitm_http2': False 
    }
    browser = webdriver.Chrome(options=opts,seleniumwire_options=proxy_options)
    browser.get(data)
    if browser.current_url == data:
    #//div[@class="mt-3 alert alert-info"]/strong
        element_all = wait(browser,30).until(EC.presence_of_element_located((By.XPATH, '//a[@id="signin_btn"]')))
        #browser.execute_script("arguments[0].scrollIntoView();", element_all)
        browser.execute_script("arguments[0].click();", element_all)
        sleep(5)
        browser.execute_script("arguments[0].click();", element_all)
        
        get_claim = wait(browser,2).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@class="btnClaim"]')))
        
        for i in range(1, len(get_claim)+1):
            element_all = wait(browser,30).until(EC.presence_of_element_located((By.XPATH, f'(//*[@class="btnClaim"])[{i}]')))
            browser.execute_script("arguments[0].click();", element_all)
        print(f"[*] {data}")
        sleep(5)
        with open('success.txt','a') as f: f.write(f'{data}\n')
        browser.quit()
        
    else:
        with open('gagal.txt','a') as f: f.write(f'{data}\n')
        browser.quit()
        
if __name__ == '__main__':
    global list_accountsplit
    print('[*] Automation Claim')
    print('[*] Author: RJD')
    jumlah = int(input("[*] Multi Proccessing: "))
    file_list_akun = "data.txt"
    myfile_akun = open(f"{cwd}/{file_list_akun}","r")
    akun = myfile_akun.read()
    list_accountsplit = akun.split("\n")
 
    with Pool(jumlah) as p:  
        p.map(claim, list_accountsplit)

    print('[*] Automation is Done')

 