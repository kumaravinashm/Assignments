from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from Assignment3.src.pageobject.Locator import Locator
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from lib2to3.tests.support import driver
from asyncio.tasks import sleep



class home_texsie(object):

    def __init__(self, driver):
        self.driver = driver

        self.Analyze = driver.find_element(By.XPATH, Locator.Analyze)
        self.Textbox_Sentiment = driver.find_element(By.XPATH, Locator.Textbox_Sentiment)



    def click_Analyze(self):
        self.Analyze.click()


    def set_text_Textbox_Sentiment(self, text):
        self.Textbox_Sentiment.clear()
        self.Textbox_Sentiment.send_keys(text)

class home_texsie_exe(object):

    def __init__(self, driver):
        self.driver = driver

        self.Average = driver.find_element(By.XPATH, Locator.Average)
        self.Selected_Keyword = driver.find_element(By.XPATH, Locator.Selected_Keyword)
        self.Positive_keyword = driver.find_element(By.XPATH, Locator.Positive_keyword)
        self.Keyword_Extract = driver.find_element(By.XPATH, Locator.Keyword_Extract)

    def get_Average(self):
        average = self.Average.text
        return average

    def get_selected_keyword(self):
        str_Selected_Key = self.Selected_Keyword.text
        return str_Selected_Key

    def get_Positive_keyword(self):
        str_pos_key = self.Positive_keyword.text
        return str_pos_key

    def click_Positive_keyword(self):
        self.Positive_keyword.click()

    def get_Keyword_Extract(self):
        str_Key_Extract = self.Keyword_Extract.text
        return str_Key_Extract







