import pytest
from mimesis import Person
from mimesis.locales import EN

from pages.basket_page import BasketPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.product_page import ProductPage

LINK = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
LOGIN_PAGE_LINK = "http://selenium1py.pythonanywhere.com/accounts/login/"


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        browser.delete_all_cookies()
        page = LoginPage(browser, LOGIN_PAGE_LINK)
        page.open()
        page.should_be_login_page()
        person = Person(EN)
        page.register_new_user(person.email(), person.password(length=9))
        page.should_be_authorized_user()

    def test_user_cannot_see_product_in_basket_opened_from_main_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.go_to_basket_page()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.should_be_empty_basket()
        basket_page.should_see_empty_basket_message()

    def test_user_cannot_see_product_in_basket_opened_from_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.go_to_basket_page()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.should_be_empty_basket()
        basket_page.should_see_empty_basket_message()


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
    page.add_product_to_the_basket()
    page.should_be_message_the_product_has_been_added_to_the_basket()
    page.price_should_be_as_expected()


@pytest.mark.xfail
def test_guest_cannot_see_success_message_after_adding_product_to_basket(browser):
    browser.delete_all_cookies()
    page = ProductPage(browser, LINK)
    page.open()
    page.add_product_to_the_basket()
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
    page.add_product_to_the_basket()
    page.success_message_should_disappeared()


def test_guest_should_see_login_link_on_product_page(browser):
    browser.delete_all_cookies()
    page = ProductPage(browser, LINK)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    browser.delete_all_cookies()
    page = ProductPage(browser, LINK)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()
