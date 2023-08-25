
from selenium import webdriver

# before all
def before_all(context):
    context.browser = webdriver.Chrome(r"PATH TO CHROMEDRIVER")
    context.browser.maximize_window()

def after_all(context):
    context.browser.quit()