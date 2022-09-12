from pages.base_page import BasePage
from pages.locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert 'login' in self.browser.current_url, 'No "login" in url'
        # assert self.url
        # assert True

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_presented(*LoginPageLocators.LOGIN_FORM), 'No login form on page'

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_presented(*LoginPageLocators.REGISTER_FORM), 'No register form on page'
        # assert True