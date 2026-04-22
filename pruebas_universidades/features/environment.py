from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def before_scenario(context, scenario):
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")
    context.driver = webdriver.Chrome(options=options)


def after_scenario(context, scenario):
    if hasattr(context, 'driver'):
        context.driver.quit()
