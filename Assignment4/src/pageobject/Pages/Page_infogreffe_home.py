from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from Assignment4.src.pageobject.Locator import Locator




class home_infogreffe(object):

    def __init__(self, driver):
        self.driver = driver
        self.Search_Box = driver.find_element(By.CSS_SELECTOR, Locator.Search_Box)
        self.Search_Submit = driver.find_element(By.XPATH, Locator.Search_Submit)



    def set_Search_Box(self,text_to_search):
        self.Search_Box.click()
        print(text_to_search)
        self.Search_Box.send_Keys(text_to_search)


    def click_Search_button(self):
        self.Search_Submit.click()

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







