import pickle
from selenium_stealth import stealth
from selenium import webdriver
import selenium
import time
import random
import os
import pyautogui


def startdriver():
    options = webdriver.ChromeOptions()
    options.add_argument('window-size=500x500')

    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    
    driver = webdriver.Chrome(options=options, executable_path=r"chromedriver.exe")
    #driver.set_window_size(500, 500)
    driver.set_window_position(0, 0)
    

    languages = ["af", "sq", "ar-SA", "ar-IQ", "ar-EG", "ar-LY", "ar-DZ", "ar-MA", "ar-TN", "ar-OM",
                 "ar-YE", "ar-SY", "ar-JO", "ar-LB", "ar-KW", "ar-AE", "ar-BH", "ar-QA", "eu", "bg",
                 "be", "ca", "zh-TW", "zh-CN", "zh-HK", "zh-SG", "hr", "cs", "da", "nl", "nl-BE", "en",
                 "en-US", "en-EG", "en-AU", "en-GB", "en-CA", "en-NZ", "en-IE", "en-ZA", "en-JM",
                 "en-BZ", "en-TT", "et", "fo", "fa", "fi", "fr", "fr-BE", "fr-CA", "fr-CH", "fr-LU",
                 "gd", "gd-IE", "de", "de-CH", "de-AT", "de-LU", "de-LI", "el", "he", "hi", "hu",
                 "is", "id", "it", "it-CH", "ja", "ko", "lv", "lt", "mk", "mt", "no", "pl",
                 "pt-BR", "pt", "rm", "ro", "ro-MO", "ru", "ru-MI", "sz", "sr", "sk", "sl", "sb",
                 "es", "es-AR", "es-GT", "es-CR", "es-PA", "es-DO", "es-MX", "es-VE", "es-CO",
                 "es-PE", "es-EC", "es-CL", "es-UY", "es-PY", "es-BO", "es-SV", "es-HN", "es-NI",
                 "es-PR", "sx", "sv", "sv-FI", "th", "ts", "tn", "tr", "uk", "ur", "ve", "vi", "xh",
                 "ji", "zu"]

    vendors = ["Google Inc.", "Firefox", "Google" "Chrome", "Microsoft", "Edge", "Apple", "Safari", "Opera", "Brave",
               "Vivaldi",
               "DuckDuckGo", "Chromium", "Epic"]

    platforms = ["ChromeOS", "Windows", "MAC", "Linux"]

    webgl = ["WebKit", "Intel Inc.", "AMD"]
    renderers = ["M1", "Intel", "Nvidia", "AMD"]

    stealth(driver,
            languages=[f"{random.choice(languages)}", f"{random.choice(languages)}"],
            vendor=f"{random.choice(vendors)}",
            platform=f"{random.choice(platforms)}",
            webgl_vendor=f"{random.choice(webgl)}",
            renderer=f"{renderers}",
            fix_hairline=True,
            )
    return driver


groupname = input("Enter cookie group name : ")
accounts = int(input("How many accounts you want to save? : "))
try:
    os.mkdir(f"./cookies/{groupname}-{time.strftime('%d-%m-%Y')}")
except:
    pass


email = 'amajidbac@gmail.com'
passw = 'AMAJID2001@'

for i in range(0, accounts):
    driver = startdriver()
    driver.get("https://www.tiktok.com/login/phone-or-email/email/?lang=en")
    time.sleep(3)
    pyautogui.click(343, 268)
    time.sleep(1)
    pyautogui.write(email, interval=0.25)
    pyautogui.press('tab')
    pyautogui.write(passw, interval=0.25)
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    y = input("tap Enter to save cookie")
    try:
        pickle.dump(driver.get_cookies(), open(f"./cookies/{groupname}-{time.strftime('%d-%m-%Y')}/cookie-{i}.pkl", "wb"))
    except selenium.common.exceptions.InvalidSessionIdException:
        pass
    try:
        driver.close()
    except selenium.common.exceptions.InvalidSessionIdException:
        pass
    
    
    

"""
driver.get("https://www.tiktok.com")
cookies = pickle.load(open("./cookies/11-10-2022/cookie-1.pkl", "rb"))
for cookie in cookies:
    driver.add_cookie(cookie)
"""