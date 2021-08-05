from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):

        url = self.browser.current_url
        assert "login" in url

    def should_be_login_form(self):

        assert self.is_element_present(*LoginPageLocators.LOGIN_INPUT_EMAIL), (
            "Отсутствует форма ввода e-mail для логина")
        assert self.is_element_present(*LoginPageLocators.LOGIN_INPUT_PASSWORD), (
            "Отсутствует форма ввода пароля для логина")
        assert self.is_element_present(*LoginPageLocators.LOGIN_BUTTON_LOGIN), (
            "Отсутствует кнопка логина")

    def should_be_register_form(self):

        assert self.is_element_present(*LoginPageLocators.REGISTER_INPUT_EMAIL), (
            "Отсутствует форма ввода e-mail для регистрации")
        assert self.is_element_present(*LoginPageLocators.REGISTER_INPUT_PASSWORD), (
            "Отсутствует форма ввода пароля для регистрации")
        assert self.is_element_present(*LoginPageLocators.REGISTER_INPUT_PASSWORD_CONFIRM), (
            "Отсутствует форма ввода подтверждения пароля для регистрации")
        assert self.is_element_present(*LoginPageLocators.REGISTER_BUTTON_REGISTER), (
            "Отсутствует кнопка регистрации")
