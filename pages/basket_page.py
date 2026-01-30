from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_be_basket_empty(self):
        # Проверяем, что нет товаров в корзине
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
            "Basket is not empty, but should be"
    
    def should_be_empty_basket_message(self):
        # Проверяем, что есть сообщение о пустой корзине
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), \
            "Empty basket message is not presented"