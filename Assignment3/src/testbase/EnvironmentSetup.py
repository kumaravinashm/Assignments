import unittest
import datetime
from selenium import webdriver

class EnvironmentSetup(unittest.TestCase):

#setUP contains the browser setup attributes
    def setUp(self):
        self.driver = webdriver.Chrome('C:/Users/NEXUS/PycharmProjects/Test/Corefiles/chromedriver.exe')
        print ("Run Started at :"+str(datetime.datetime.now()))
        print("Chrome Environment Set Up")
        print("------------------------------------------------------------------")
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()

    def get_home_page(self):
        driver = self.driver
        driver.get("https://tqcfd-dev-cf-1.tradeturquoisenylontest.com/#/")
        driver.set_page_load_timeout(22)

#tearDown method just to close all the browser instances and then quit
    def tearDown(self):
        if (self.driver!=None):
            print("------------------------------------------------------------------")
            print("Test Environment Destroyed")
            print("Run Completed at :" + str(datetime.datetime.now()))
            #self.driver.close()
            #self.driver.quit()