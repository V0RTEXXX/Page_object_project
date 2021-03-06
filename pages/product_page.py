from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def press_button_add_to_basket(self):
        button_add_to_basket = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        button_add_to_basket.click()

    def should_be_message_about_adding(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), (
            "Название товара отсутствует")
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME_IN_MESSAGE), (
            "Сообщение об успешном добавлении отсутствует")
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_name_in_message = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_MESSAGE).text
        assert product_name == product_name_in_message, (
            "Название товара не соответствует названию в сообщении")

    def should_be_message_basket_total(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_BASKET_TOTAL), (
            "Отсутствует сообщение basket total")
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), (
            "Отсутствует цена товара")
        message_basket_total = self.browser.find_element(*ProductPageLocators.MESSAGE_BASKET_TOTAL).text
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        assert product_price in message_basket_total, (
            "Отсутствует цена товара в сообщении")

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), (
            "Появляется положительное сообщение, хотя не должно было")

    def success_message_should_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), (
            "Положительное сообщение не появляется, хотя должно было")