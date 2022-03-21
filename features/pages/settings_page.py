from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

from features.browser import Browser


class SettingsPageElements(object):

    ACCOUNT_BUTTON = '#gb > div.gb_pd.gb_Fd.gb_xd.gb_5b > div.gb_wc.gb_Ka.gb_vc.gb_Dd > div > div.gb_Fa.gb_Qc.gb_bg.gb_f.gb_kf > div > a'

    # folder elements
    ADD_FOLDER = '//*[contains(text(), "Create new label")]'
    FOLDER_SUBMIT = 'ok'
    # the notification that a folder was created
    FOLDER_SUCCESS = '/html/body/div[7]/div[3]/div/div[1]/div[5]/div[1]/div/div[3]/div/div/div[2]/span/span'
    FOLDER_DELETE = '//*[@id=":89"]/div'
    FOLDER_DELETE_BUTTON = '/html/body/div[27]/div[3]/button[1]'

    # settings elements
    SETTINGS_TITLE = '#\:4 > div > div.nH.qZ.G-atb > div.du > h2'
    SETTINGS_LINK = 'https://mail.google.com/mail/u/0/#settings/labels'


class SettingsPage(Browser):

    def navigate_to_settings(self):
        WebDriverWait(self.driver, 5000).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, SettingsPageElements.ACCOUNT_BUTTON))
        )
        self.driver.get(SettingsPageElements.SETTINGS_LINK)

    def create_folder(self, folder_name):
        WebDriverWait(self.driver, 5000).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, SettingsPageElements.SETTINGS_TITLE))
        )
        self.driver.execute_script('window.scrollTo(0, 1080)')
        create_folder_button = self.driver.find_element_by_xpath(SettingsPageElements.ADD_FOLDER)
        create_folder_button.click()

        actions = ActionChains(self.driver)
        actions.send_keys(folder_name)
        actions.perform()
        # actions.send_keys(Keys.ENTER)

        self.driver.find_element_by_name(SettingsPageElements.FOLDER_SUBMIT).click()

    def delete_folder(self):
        self.driver.find_element_by_xpath(SettingsPageElements.FOLDER_DELETE).click()
        self.driver.find_element_by_xpath(SettingsPageElements.FOLDER_DELETE_BUTTON).click()

    def folder_success(self):
        return self.driver.find_element_by_xpath(SettingsPageElements.FOLDER_SUCCESS)
