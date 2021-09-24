from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_the_backed(self):
        link = self.browser.find_element(*ProductPageLocators.ADD_TO_BACKED_BUTTON)
        link.click()
        self.solve_quiz_and_get_code()

    def should_be_message_the_product_has_been_added_to_the_backed(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_LINK), "Login url is not presented"
        login_link = self.browser.find_element(*LoginPageLocators.LOGIN_LINK)
        login_link.click()
        assert "login" in self.browser.current_url, "There is not login in url"