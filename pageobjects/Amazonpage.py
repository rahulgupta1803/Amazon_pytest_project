from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Amazon_Login():
    click_signin_XPATH = (By.XPATH,'//span[@id="nav-link-accountList-nav-line-1"]')
    text_email_XPATH = (By.XPATH,'//input[@id="ap_email"]')
    click_continue_button_XPATH = (By.XPATH,'//input[@id="continue"]')
    text_password_XPATH = (By.XPATH,'//input[@id="ap_password"]')
    click_signin_button_XPATH = (By.XPATH,'//input[@id="signInSubmit"]')
    login_status_XPATH = (By.XPATH,'//span[@id="nav-link-accountList-nav-line-1"]')
    # login_status_element_XPATH = (By.XPATH,'//a[@id="nav-link-accountList"]')
    click_signout_XPATH = (By.XPATH,'//a[@id="nav-item-signout"]/span')

    def __init__(self,driver):
        self.driver = driver

    def Click_Signin(self):
        self.driver.find_element(*Amazon_Login.click_signin_XPATH).click()

    def Entry_email(self,email):
        self.driver.find_element(*Amazon_Login.text_email_XPATH).send_keys(email)

    def Continue_Button(self):
        self.driver.find_element(*Amazon_Login.click_continue_button_XPATH).click()

    def Entry_Password(self,password):
        self.driver.find_element(*Amazon_Login.text_password_XPATH).send_keys(password)

    def Signin_Button(self):
        self.driver.find_element(*Amazon_Login.click_signin_button_XPATH).click()

    def Click_Signout(self):
        a = ActionChains(self.driver)
        m = self.driver.find_element(*Amazon_Login.login_status_XPATH)
        a.move_to_element(m).perform()
        n = self.driver.find_element(*Amazon_Login.click_signout_XPATH)
        a.move_to_element(n).click().perform()

    # def Login_Status_Element(self):
    #     self.driver.find_element(*Amazon_Login.login_status_element_XPATH).click()


    def Login_status(self):
        try:
            self.driver.find_element(*Amazon_Login.login_status_XPATH)
            return True
        except:
            return False






