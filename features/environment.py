from features.browser import Browser
from features.pages.login_page import LoginPage
from features.pages.products_page import ProductsPage
from features.pages.settings_page import SettingsPage


def before_all(context):

    # user credentials
    username = 'standard_user'
    password = 'secret_sauce'

    context.browser = Browser()
    context.login_page = LoginPage()
    context.products_page = ProductsPage()
    # context.settings_page = SettingsPage()

    context.login_page.navigate_to_sauce_lab()
    context.login_page.login(username, password)


def after_all(context):
    context.server.shutdown()
    context.thread.join()
    context.browser.quit()
