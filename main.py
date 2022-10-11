from selenium_stealth import stealth
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
import random
import pickle


def document_initialised(driver):
    return driver.execute_script("return initialised")


def newdriver():
    options = webdriver.ChromeOptions()

    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)

    s = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(options=options, service=s)

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
    driver.set_window_position(0, 0)
    return driver


def upload(driver1, video_path, caption):
    driver1.get("https://www.tiktok.com/upload?lang=en")

    cookies = pickle.load(open("./cookies/d-11-10-2022/cookie-4.pkl", "rb"))
    for cookie in cookies:
        driver1.add_cookie(cookie)
    driver1.refresh()
    WebDriverWait(driver1, timeout=10).until(document_initialised)
    iframe = driver1.find_element(By.CSS_SELECTOR, 'iframe')
    driver1.switch_to.frame(iframe)
    WebDriverWait(driver1, timeout=10).until(document_initialised)
    upload = driver1.find_element(By.CSS_SELECTOR, 'input[type="file"]')
    upload.send_keys(video_path)
    captionfield = driver1.find_element(By.CSS_SELECTOR, 'div[spellcheck="false"]')
    captionfield.send_keys(caption)
    time.sleep(5)
    send = driver1.find_element(By.CSS_SELECTOR, '.css-y1m958')
    send.click()
    time.sleep(5)
    driver1.close()
    return 0


def main():
    cookiepath = input("Enter Cookie Folder Path : ")
    videospath = input("Enter Videos Folder Path : ")


