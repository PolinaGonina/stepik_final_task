from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_not_be_products_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_IN_BASKET), \
        "Basket contains products, but should not"
    
    def should_be_message_about_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.MESSAGE_ABOUT_EMPTY_BASKET), \
            "Message about empty basket is not presented"
        message_about_empty_basket = self.browser.find_element(*BasketPageLocators.MESSAGE_ABOUT_EMPTY_BASKET).text
        empty_content = "empty"
        assert empty_content in message_about_empty_basket, "It is not mentioned that the basket is empty"