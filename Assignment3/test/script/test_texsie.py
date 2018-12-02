from Assignment3.src.testbase.EnvironmentSetup import EnvironmentSetup
from Assignment3.src.pageobject.Pages.Page_texsie_Sentiment_Analysis import *
import pandas

class Texcie_Stride(EnvironmentSetup):

    def read_data(self):
        try:
            reader = pandas.ExcelFile("texsiedata.xlsx")
            sheet = reader.parse("textbox_data")
        except IOError:
            print("Error: File does not appear to exist.")
        return sheet




    def test_Home_Page(self):
        driver = self.driver
        sheet = Texcie_Stride.read_data(self)
        self.driver.get(sheet['url'].values[0])
        self.driver.set_page_load_timeout(22)
        sheet = Texcie_Stride.read_data(self)
    #validating title of the page
        self.assertIn("Stride | Text Analytics", self.driver.title)
    #Sending text and clicking analyse
        homepage = home_texsie(driver)
        homepage.set_text_Textbox_Sentiment(sheet['text'].values[0])
        homepage.click_Analyze()
    #validating the keywords
        homepagevalidation = home_texsie_exe(driver)
        average = homepagevalidation.get_Average()
        self.assertIn(str(sheet['average'].values[0]), average)
        positive_key = homepagevalidation.get_Positive_keyword()
        self.assertIn(str(sheet['positive_key'].values[0]), positive_key)
        Selected_keyword = homepagevalidation.get_selected_keyword()
        self.assertIn(str(sheet['positive_key'].values[0]), Selected_keyword)
        key_extract = homepagevalidation.get_Keyword_Extract()
        self.assertIn(str(sheet['keyword_extract'].values[0]), key_extract)

