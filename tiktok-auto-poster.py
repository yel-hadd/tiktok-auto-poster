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
from pythonping import ping


def switch_ip():
    return 0


def upload(cookie_path, video_path, caption):
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
    cookies = pickle.load(open(cookie_path, "rb"))
    for cookie in cookies:
        driver1.add_cookie(cookie)
    driver1.get("https://www.tiktok.com/upload?lang=en")
    time.sleep(5)
    iframe = driver1.find_element(By.CSS_SELECTOR, 'iframe')
    driver1.switch_to.frame(iframe)
    file_picker = WebDriverWait(driver1, 100).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,
                                                                                                     'input[type="file"]')))
    file_picker.send_keys(video_path)
    caption_field = driver1.find_element(By.CSS_SELECTOR, 'div[spellcheck="false"]')
    caption_field.send_keys(caption)
    send = WebDriverWait(driver1, 100).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                                                                          '.css-y1m958')))
    send.click()
    WebDriverWait(driver1, 100).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,
                                                                                       "#portal-container > div > div > div.jsx-461155393.jsx-3220008684.modal > div.jsx-461155393.jsx-3220008684.modal-btn.emphasis")))
    driver1.close()
    return 0


def load():
    cookiepath = input("Enter Cookie Folder Path (Absolute Path Recommended): ")
    videospath = input("Enter Videos Folder Path (Absolute Path Recommended): ")
    videos = []
    for root, dirs, files in os.walk(os.path.abspath(videospath)):
        for file in files:
            file = os.path.join(root, file)
            videos.append(file)
    cookies = []
    for root, dirs, files in os.walk(os.path.abspath(cookiepath)):
        for file in files:
            file = os.path.join(root, file)
            cookies.append(file)
    captions = []
    for root, dirs, files in os.walk(os.path.abspath("./captions")):
        for file in files:
            file = os.path.join(root, file)
            with open(file, "r") as cp:
                data = ' '.join([line.replace('\n', '') for line in cp.readlines()])
                captions.append(data)

    with open(os.path.abspath('./hashtags/hashtags.txt'), "r") as cp:
        hashtags = ' '.join([line.replace('\n', '') for line in cp.readlines()]).split(',')

    return cookies, videos, captions, hashtags


def tiktok_auto_sender():
    cookies, videos, captions, hashtags = load()
    num_of_uploads = 0
    for vid in videos:
        for cookie in cookies:
            htag1 = random.choice(hashtags)
            htag2 = random.choice(hashtags)
            htag3 = random.choice(hashtags)

            upload(cookie, vid, f"{random.choice(captions)} {htag1} {htag2} {htag3}")
            num_of_uploads += 1
            switch_ip()
            print(f"{num_of_uploads} videos has been uploaded !")


# tiktok_auto_sender()
ping('127.0.0.1')