from selenium import webdriver


class Browser(object):
    driver = webdriver.Chrome('drivers/chromedriver')
    driver.implicitly_wait(30)
    driver.set_page_load_timeout(30)
    driver.maximize_window()

    def close(self):
        self.driver.close()
