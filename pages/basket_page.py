from pages.base_page import BasePage
from pages.locators import BasketPageLocators


class BasketPage(BasePage):
    def should_see_empty_basket_message(self):
        basket_has_no_items = self.browser.execute_script("return $('#content_inner').children().length == 1;")
        assert basket_has_no_items, "Basket has products in the list"

    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "Basket is not empty"
