import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from pageobjects.Amazonpage import Amazon_Login
from utilities import xlutils


class Test_Amazon():
    fpath="D:\\credence\\Amazon_pytest_project\\testcases\\testdata\\amazon_login.xlsx"

    def test_amazon_login_001(self,setup):
        self.driver = setup
        self.alp = Amazon_Login(self.driver)

        self.row = xlutils.RowCount(self.fpath,"Sheet1")
        print(self.row)
        exp_result_list = []
        for r in range (2,self.row+1):
            self.email = xlutils.ReadData(self.fpath,"Sheet1",r,2)
            self.password = xlutils.ReadData(self.fpath, "Sheet1", r, 3)
            self.exp_result = xlutils.ReadData(self.fpath,"Sheet1",r,4)

            self.alp.Click_Signin()
            self.alp.Entry_email(self.email)
            self.alp.Continue_Button()
            self.alp.Entry_Password(self.password)
            # self.alp.Login_status()
            self.alp.Signin_Button()
            time.sleep(3)
            if self.alp.Login_status()==True:
                if self.exp_result == "pass":
                    exp_result_list.append("pass")
                    time.sleep(5)
                    self.alp.Click_Signout()
                    # a = ActionChains(self.driver)
                    # m = self.driver(By.XPATH,'//span[@id="nav-link-accountList-nav-line-1"]')
                    # a.move_to_element(m).perform()
                    # n = self.driver(By.XPATH,'//a[@id="nav-item-signout"]/span')
                    # a.move_to_element(n).click().perform()

                elif self.exp_result == "fail":
                    exp_result_list.append("fail")
                    time.sleep(5)
                    self.alp.Click_Signout()

                    # a = ActionChains(self.driver)
                    # m = self.driver(By.XPATH, "//span[@id='nav-link-accountList-nav-line-1']")
                    # a.move_to_element(m).perform()
                    # n = self.driver(By.XPATH, '//a[@id="nav-item-signout"]/span')
                    # a.move_to_element(n).click().perform()

            if self.alp.Login_status()==False:
                if self.exp_result == "pass":
                    exp_result_list.append("fail")
                    self.driver.get("https://www.amazon.in/")
                elif self.exp_result == "fail":
                    exp_result_list.append("pass")
                    self.driver.get("https://www.amazon.in/")

        print(exp_result_list)
        if "fail" not in exp_result_list:
            assert True
        else:
            assert False


