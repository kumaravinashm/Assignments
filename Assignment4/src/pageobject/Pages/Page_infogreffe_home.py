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

class search_table(object):
    def __init__(self, driver):
        self.driver = driver
        self.comany_name = driver.find_element(By.CSS_SELECTOR, Locator.comany_name)
        self.company_address = driver.find_element(By.XPATH, Locator.company_address)
        self.company_siret = driver.find_element(By.XPATH, Locator.company_siret)

    def get_company_Name(self):
        comany_name = self.comany_name.text
        return comany_name


    def get_Address(self):
        company_address = self.company_address.text
        return  company_address

    def get_Siret(self):
        company_siret = self.company_siret.text
        return  company_siret



