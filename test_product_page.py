from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
import pytest
import time

def test_guest_can_add_product_to_basket(browser):

    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.press_button_add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_message_about_adding()
    page.should_be_message_basket_total()