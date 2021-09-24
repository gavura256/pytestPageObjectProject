from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_the_backed(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BACKED_BUTTON), "Login url is not presented"
        link = self.browser.find_element(*ProductPageLocators.ADD_TO_BACKED_BUTTON)
        link.click()
        self.solve_quiz_and_get_code()

    def should_be_message_the_product_has_been_added_to_the_backed(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        message_text = self.browser.find_element(*ProductPageLocators.MESSAGES).text
        assert product_name in message_text, "No product name in messages"

    def price_should_be_as_expected(self):
        product_price = '9.99'
        message_text = self.browser.find_element(*ProductPageLocators.MESSAGES).text
        assert product_price in message_text, "Wrong price for the product"
