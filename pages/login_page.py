from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.url == "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/", "No login in url" # проверка на корректный url адрес
       
    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"  # проверка, что есть форма логина

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented" # проверка, что есть форма регистрации на странице
        
    def register_new_user(self, email, password):
        email_element = self.browser.find_element(*LoginPageLocators.EMAIL)
        password_element = self.browser.find_element(*LoginPageLocators.PASSWORD1)
        confirm_password_element = self.browser.find_element(*LoginPageLocators.PASSWORD2)
       
        email_element.send_keys(email)
        password_element.send_keys(password)
        confirm_password_element.send_keys(password)
       
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register_button.click()
        