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
        for x in range (sheet['search_element'].count()):
            if (x>1):
                self.driver.get(sheet['url'].values[0])
            homepage = home_infogreffe(driver)
            #homepage.Search_Box(sheet['search_element'].values[x])
            homepage.Search_Submit()
            search_table  = search_table(driver)
            comp_name = search_table.get_company_Name()
            print("Company Name: "+comp_name)
            comp_address = search_table.get_Address()
            print("Company Address: "+comp_address)
            comp_siret = search_table.get_Siret()
            print("Compony Siret: "+comp_siret)


