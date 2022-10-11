from selenium_stealth import stealth
from selenium import webdriver
import time;
import random
import pickle

options = webdriver.ChromeOptions()
options.add_argument('window-size=1440x2960')

options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
driver1 = webdriver.Chrome(options=options, executable_path=r"./chromedriver")


upload_url = "https://www.tiktok.com/upload?lang=en"

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

stealth(driver1,
        languages=[f"{random.choice(languages)}", f"{random.choice(languages)}"],
        vendor=f"{random.choice(vendors)}",
        platform=f"{random.choice(platforms)}",
        webgl_vendor=f"{random.choice(webgl)}",
        renderer=f"{renderers}",
        fix_hairline=True,
        )
driver1.set_window_position(0,0)
driver1.get(upload_url)

cookies = pickle.load(open("./cookies/d-11-10-2022/cookie-4.pkl", "rb"))
for cookie in cookies:
    driver1.add_cookie(cookie)
driver1.refresh()
time.sleep(5)
iframe = driver1.find_element_by_css_selector('iframe')
driver1.switch_to.frame(iframe)
time.sleep(5)
upload = driver1.find_element_by_css_selector('input[type="file"]')
video_path = './videos/vid.mp4'
upload.send_keys(video_path)
caption = driver1.find_element_by_css_selector('div[spellcheck="false"]')
caption.send_keys(video_path)
time.sleep(5)
send = driver1.find_element_by_css_selector('.css-y1m958').click()
time.sleep(5)
