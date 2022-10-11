from selenium_stealth import stealth
from selenium import webdriver
import time;
import random



options = webdriver.ChromeOptions()
options.add_argument('window-size=1440x2960')

options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
driver1 = webdriver.Chrome(options=options, executable_path=r"./chromedriver")
driver2 = webdriver.Chrome(options=options, executable_path=r"./chromedriver")
driver3 = webdriver.Chrome(options=options, executable_path=r"./chromedriver")
driver4 = webdriver.Chrome(options=options, executable_path=r"./chromedriver")

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
             "ji", "zu"];

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

stealth(driver2,
        languages=[f"{random.choice(languages)}", f"{random.choice(languages)}"],
        vendor=f"{random.choice(vendors)}",
        platform=f"{random.choice(platforms)}",
        webgl_vendor=f"{random.choice(webgl)}",
        renderer=f"{renderers}",
        fix_hairline=True,
        )

stealth(driver3,
        languages=[f"{random.choice(languages)}", f"{random.choice(languages)}"],
        vendor=f"{random.choice(vendors)}",
        platform=f"{random.choice(platforms)}",
        webgl_vendor=f"{random.choice(webgl)}",
        renderer=f"{renderers}",
        fix_hairline=True,
        )

stealth(driver4,
        languages=[f"{random.choice(languages)}", f"{random.choice(languages)}"],
        vendor=f"{random.choice(vendors)}",
        platform=f"{random.choice(platforms)}",
        webgl_vendor=f"{random.choice(webgl)}",
        renderer=f"{renderers}",
        fix_hairline=True,
        )
# https://www.tiktok.com/login/phone-or-email/email
driver1.get(upload_url)
#driver1.add_cookie(cookie)
driver2.get(upload_url)
driver3.get(upload_url)
driver4.get(upload_url)
#

# ("https://www.tiktok.com/upload?lang=en")


# helium.drag_file(file_path="/Users/yel-hadd/PycharmProjects/pythonProject/vid.mp4", to='Select file')
# helium.get_easily_readable_snippet()
#
# cells = find_all(S("table > tr > td", below="Post a video to your account"))
# fields = [cell.web_element.text for cell in cells]
#
#
# /html/body/div[1]/div/div[2]/div/iframe
#
# driver1.find_elements_by_xpath("9414f327-ce02-43ee-82ed-c0109ffec59e")
# driver1.
# driver1.find_element_by_name("Select file")
