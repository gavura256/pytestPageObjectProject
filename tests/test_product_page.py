# pr

from pages.product_page import ProductPage

link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"


def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_the_backed()
    # time.sleep(999)
    page.should_be_message_the_product_has_been_added_to_the_backed()
    page.price_should_be_as_expected()
