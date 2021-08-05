from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_be_message_about_empty_basket(self):
        text_about_empty_basket = self.browser.find_element(
            *BasketPageLocators.BASKET_EMPTY_TEXT).text
        assert text_about_empty_basket == "Your basket is empty. Continue shopping", (
            "Не отображается название товара"
        )

    def should_not_be_product_in_basket(self):

        assert self.is_not_element_present(*BasketPageLocators.BASKET_PRODUCT_NAME), (
            "Отображается название товара, хотя не должно"
        )