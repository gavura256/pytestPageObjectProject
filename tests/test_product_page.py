import pytest

from pages.product_page import ProductPage
from pages.login_page import LoginPage

LINK = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"


@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param(
                                      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                      marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    browser.delete_all_cookies()
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_the_backed()
    page.should_be_message_the_product_has_been_added_to_the_backed()
    page.price_should_be_as_expected()


@pytest.mark.xfail
def test_guest_cannot_see_success_message_after_adding_product_to_basket(browser):
    browser.delete_all_cookies()
    page = ProductPage(browser, LINK)
    page.open()
    page.add_product_to_the_backed()
    page.should_not_be_success_message()


def test_guest_cannot_see_success_message(browser):
    browser.delete_all_cookies()
    page = ProductPage(browser, LINK)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basked(browser):
    browser.delete_all_cookies()
    page = ProductPage(browser, LINK)
    page.open()
    page.add_product_to_the_backed()
    page.success_message_should_disappeared()


def test_guest_should_see_login_link_on_product_page(browser):
    browser.delete_all_cookies()
    page = ProductPage(browser, LINK)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    browser.delete_all_cookies()
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()
