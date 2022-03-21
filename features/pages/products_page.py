from nose.tools import assert_true
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from features.browser import Browser


class ProductsPageElements(object):
    # inbox url
    SHOPPING_PAGE = 'https://www.saucedemo.com/inventory.html'

    # navbar elements
    BURGER_BUTTON = '//button[@id="react-burger-menu-btn"]'
    LOGOUT_BUTTON = '//a[@id="logout_sidebar_link"]'

    # compose message elements
    COMPOSE = '//div[text()="Compose"]'
    RECIPIENT = '//textarea[@aria-label="To"]'
    SUBJECT = '//input[@aria-label="Subject"]'
    MESSAGE = '//div[@aria-label="Message Body"]'
    SEND = '//div[@aria-label="Send ‪(⌘Enter)‬"]'

    # selection of item
    # item 1
    BACKPACK = "//button[@name='add-to-cart-sauce-labs-backpack']"
    BACKPACK_REMOVE_BTN = "//button[@name='remove-sauce-labs-backpack']"

    # item 2
    BIKE_LIGHT = "//button[@name='add-to-cart-sauce-labs-bike-light']"
    BIKE_LIGHT_REMOVE_BTN = "//button[@name='remove-sauce-labs-bike-light']"

    # shopping card
    SHOPPING_CARD = "//a[@class='shopping_cart_link']"
    CHECKOUT_BUTTON = "//button[@name='checkout']"

    # check out page
    CHECKOUT_PERSONAL_DATA_FIRST_NAME = "//input[@id='first-name']"
    CHECKOUT_PERSONAL_DATA_LAST_NAME = "//input[@id='last-name']"
    CHECKOUT_PERSONAL_DATA_POSTAL_CODE = "//input[@id='postal-code']"
    CONTINUE_BTN = "//input[@id='continue']"
    YOUR_INFORMATION_REQ = "//h3[@data-test='error'][contains(.,'Error: First Name is required')]"
    CHECKOUT_AFTER_PERSONAL_DATA_ERROR = "//h3[contains(@data-test,'error')]"

    # checkout overview page

    CHECKOUT_OVERVIEW_ITEM_BACK_PACK = "//div[@class='inventory_item_name'][contains(.,'Sauce Labs Backpack')]"
    CHECKOUT_OVERVIEW_ITEM_BACK_PACK_QUANTITY_1 = "(//div[@class='cart_quantity'][contains(.,'1')])[1]"
    CHECKOUT_OVERVIEW_ITEM_BIKE_LIGHT = "//div[@class='inventory_item_name'][contains(.,'Sauce Labs Bike Light')]"
    CHECKOUT_OVERVIEW_ITEM_BIKE_LIGHT_QUANTITY_1 = "(//div[@class='cart_quantity'][contains(.,'1')])[2]"
    CHECKOUT_OVERVIEW_FINISH_BTN = "//button[@id='finish']"
    CHECKOUT_OVERVIEW_CANCEL_BTN = "//button[@id='cancel']"

    # checkout complete

    CHECKOUT_ORDER_COMPLETE_HEADER = "//h2[@class='complete-header']"
    CHECKOUT_ORDER_COMPLETE_TEXT = "//div[@class='complete-text'] "
    CHECKOUT_ORDER_BACK_HOME_BTN = "//button[@id='back-to-products']"

    # search and filter elements
    SEARCH = '#aso_search_form_anchor > div > input'
    RESULT = '// *[ @ id = "link_vsm"]'


class ProductsPage(Browser):
    # inbox actions

    def navigate_to_inbox(self):
        self.driver.get(ProductsPageElements.SHOPPING_PAGE)

    def assert_login_success(self):
        # if burger button is present we have logged in
        assert_true(self.driver.find_element_by_xpath("//button[@id='react-burger-menu-btn']"))

    def get_page_title(self):
        return self.driver.title

    def message_sent_assert(self):
        view_message_link = WebDriverWait(self.driver, 1000).until(
            EC.presence_of_element_located((By.XPATH, ProductsPageElements.RESULT))
        )
        view_message_link.click()

    def select_message(self):
        select_button = WebDriverWait(self.driver, 1000).until(
            EC.presence_of_element_located((By.XPATH, ProductsPageElements.MESSAGE_SELECT))
        )
        select_button.click()

    def compose_message(self, recipient, subject, message):
        compose_button = WebDriverWait(self.driver, 1000).until(
            EC.presence_of_element_located((By.XPATH, ProductsPageElements.COMPOSE))
        )
        compose_button.click()

        self.driver.find_element_by_xpath(ProductsPageElements.RECIPIENT).send_keys(recipient)
        self.driver.find_element_by_xpath(ProductsPageElements.SUBJECT).send_keys(subject)
        self.driver.find_element_by_xpath(ProductsPageElements.MESSAGE).send_keys(message)

    def send_message(self):
        self.driver.find_element_by_xpath(ProductsPageElements.SEND).click()

    def search_for_message(self, search_term):
        search = WebDriverWait(self.driver, 1000).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ProductsPageElements.SEARCH))
        )
        search.send_keys(search_term)
        search.send_keys(Keys.ENTER)

    def filter_result(self):
        self.select_message()

    def delete_message(self):
        WebDriverWait(self.driver, 1000)
        self.select_message()
        self.driver.find_element_by_xpath(ProductsPageElements.DELETE).click()

    def delete_success(self):
        self.driver.find_element_by_css_selector(ProductsPageElements.DELETE_SUCCESS)

    def move_message_to_folder(self, folder_name):
        WebDriverWait(self.driver, 1000)

        self.select_message()

        wait_for_folder_dropdown = WebDriverWait(self.driver, 1000).until(
            EC.presence_of_element_located((By.XPATH, ProductsPageElements.MOVE_TO))
        )
        wait_for_folder_dropdown.click()

        actions = ActionChains(self.driver)
        actions.send_keys(folder_name)
        actions.perform()

        self.driver.find_element_by_xpath('//span[contains(text(), "Test Folder"]').click()

    def assert_message_moved(self, folder_name):
        self.driver.find_element_by_xpath('//span[@title="' + folder_name + '"]').click()
        self.delete_message()

    def multiple_item_selection(self):
        self.driver.find_element_by_xpath(ProductsPageElements.BACKPACK).click()
        assert_true(EC.presence_of_element_located((By.XPATH, ProductsPageElements.BACKPACK_REMOVE_BTN)))

        self.driver.find_element_by_xpath(ProductsPageElements.BIKE_LIGHT).click()
        assert_true(EC.presence_of_element_located((By.XPATH, ProductsPageElements.BIKE_LIGHT_REMOVE_BTN)))

    def shopping_card(self):
        self.driver.find_element_by_xpath(ProductsPageElements.SHOPPING_CARD).click()

        # validate that selected items are in the shopping card
        assert_true(EC.presence_of_element_located((By.XPATH, ProductsPageElements.BACKPACK_REMOVE_BTN)))
        assert_true(EC.presence_of_element_located((By.XPATH, ProductsPageElements.BIKE_LIGHT_REMOVE_BTN)))
        assert_true(EC.presence_of_element_located((By.XPATH, ProductsPageElements.CHECKOUT_BUTTON)))

    def checkout_personal_data(self, first_name, last_name, postal_code):
        self.driver.find_element_by_xpath(ProductsPageElements.CHECKOUT_BUTTON).click()
        self.driver.find_element_by_xpath(ProductsPageElements.CONTINUE_BTN).click()

        # validate text field validation
        assert_true(EC.presence_of_element_located((By.XPATH, ProductsPageElements.YOUR_INFORMATION_REQ)))

        self.driver.find_element_by_xpath(ProductsPageElements.CHECKOUT_PERSONAL_DATA_FIRST_NAME).send_keys(first_name)
        self.driver.find_element_by_xpath(ProductsPageElements.CHECKOUT_PERSONAL_DATA_LAST_NAME).send_keys(last_name)
        self.driver.find_element_by_xpath(ProductsPageElements.CHECKOUT_PERSONAL_DATA_POSTAL_CODE).send_keys(
            postal_code)
        self.driver.find_element_by_xpath(ProductsPageElements.CONTINUE_BTN).click()

    @staticmethod
    def checkout_overview_validation():
        # validation of selected items exists
        assert_true(EC.presence_of_element_located((By.XPATH, ProductsPageElements.CHECKOUT_OVERVIEW_ITEM_BACK_PACK)))
        assert_true(EC.presence_of_element_located(
            (By.XPATH, ProductsPageElements.CHECKOUT_OVERVIEW_ITEM_BACK_PACK_QUANTITY_1)))
        assert_true(EC.presence_of_element_located((By.XPATH, ProductsPageElements.CHECKOUT_OVERVIEW_ITEM_BIKE_LIGHT)))
        assert_true(EC.presence_of_element_located(
            (By.XPATH, ProductsPageElements.CHECKOUT_OVERVIEW_ITEM_BIKE_LIGHT_QUANTITY_1)))

        # validation of cancel and finish buttons exist
        assert_true(EC.presence_of_element_located(
            (By.XPATH, ProductsPageElements.CHECKOUT_OVERVIEW_CANCEL_BTN)))
        assert_true(EC.presence_of_element_located(
            (By.XPATH, ProductsPageElements.CHECKOUT_OVERVIEW_FINISH_BTN)))

    def checkout_finish(self):
        self.driver.find_element_by_xpath(ProductsPageElements.CHECKOUT_OVERVIEW_FINISH_BTN).click()
        assert_true(EC.presence_of_element_located(
            (By.XPATH, ProductsPageElements.CHECKOUT_ORDER_COMPLETE_HEADER)))
        assert_true(EC.presence_of_element_located(
            (By.XPATH, ProductsPageElements.CHECKOUT_ORDER_COMPLETE_TEXT)))
        # back home btn click and validation
        self.driver.find_element_by_xpath(ProductsPageElements.CHECKOUT_ORDER_BACK_HOME_BTN).click()
        assert_true(EC.presence_of_element_located(
            (By.XPATH, ProductsPageElements.BURGER_BUTTON)))

    def logout(self):
        burger_button = WebDriverWait(self.driver, 1000).until(
            EC.presence_of_element_located((By.XPATH, ProductsPageElements.BURGER_BUTTON))
        )
        burger_button.click()

        self.driver.find_element_by_xpath(ProductsPageElements.LOGOUT_BUTTON).click()
