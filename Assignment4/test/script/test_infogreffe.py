from Assignment4.src.testbase.EnvironmentSetup import EnvironmentSetup
from Assignment4.src.pageobject.Pages.Page_infogreffe_home import *
import pandas

class Infogreffe_Stride(EnvironmentSetup):

    def read_data(self):
        try:
            reader = pandas.ExcelFile("testinfogreffe.xlsx")
            sheet = reader.parse("textbox_data")
        except IOError:
            print("Error: File does not appear to exist.")
        return sheet
    def test_Home_Page(self):
        driver = self.driver
        sheet = Infogreffe_Stride.read_data(self)
        self.driver.get(sheet['url'].values[0])
        self.driver.set_page_load_timeout(22)
    #validating title of the page
        self.assertIn(sheet['Home_Title'].values[0], self.driver.title)
    #Sending text and clicking search button
        homepage = home_infogreffe(driver)
        homepage.Search_Box("hi")
        homepage.Search_Submit()
