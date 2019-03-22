from selenium import webdriver


def before_feature(context, feature):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--incognito')
    chrome_options.add_argument('--no-sandbox')
    context.browser = webdriver.Chrome(options=chrome_options)


def after_feature(context, feature):
    context.browser.quit()
