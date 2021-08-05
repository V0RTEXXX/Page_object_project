from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
import pytest
import time


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page = ProductPage(browser, link)
    page.open()
    page.press_button_add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_message_about_adding()
    page.should_be_message_basket_total()

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):

    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.press_button_add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):

    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):

    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.press_button_add_to_basket()
    page.solve_quiz_and_get_code()
    page.success_message_should_disappear()