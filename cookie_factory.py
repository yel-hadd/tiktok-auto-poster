import os
import time
import random
import pickle
from selenium import webdriver
from selenium_stealth import stealth
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


def load_credentials():
    logins = {}
    with open("./accounts/accounts.txt", "r") as file:
        data = ''.join([line.replace('\n', ',') for line in file.readlines()])
        temp = data.split(',')
    for account in temp:
        logins[account.split(':')[0]] = account.split(':')[1]
    return len(logins), logins


def login(email, password):
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

    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)

    s = Service(ChromeDriverManager().install())
    driver1 = webdriver.Chrome(options=options, service=s)

    stealth(driver1,
            languages=[f"{random.choice(languages)}", f"{random.choice(languages)}"],
            vendor=f"{random.choice(vendors)}",
            platform=f"{random.choice(platforms)}",
            webgl_vendor=f"{random.choice(webgl)}",
            renderer=f"{renderers}",
            fix_hairline=True,
            )
    driver1.get("https://www.tiktok.com/")
    driver1.get("https://www.tiktok.com/login/phone-or-email/email")

    time.sleep(5)

    email_field = driver1.find_elements(By.CSS_SELECTOR, 'input')[0]
    for chr in email:
        email_field.send_keys(chr)
        time.sleep(1.5 / random.randint(2, 10))
    password_field = driver1.find_elements(By.CSS_SELECTOR, 'input')[1]
    for chr in password:
        password_field.send_keys(chr)
        time.sleep(1.5 / random.randint(2, 10))
    time.sleep(1)
    submit = WebDriverWait(driver1, 100).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                                                                            'button[type="submit"]')))

    time.sleep(10)
    submit.click()

    return 0


def cookie_factory():
    output_path = './cookie-factory-output'
    creds = load_credentials()
    for e in creds:
        email = str(e)
        password = str(creds[e])
        login(email, password)
    return 0


cookie_factory()
