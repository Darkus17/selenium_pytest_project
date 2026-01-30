from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):

    def add_product_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_button.click()

    # ✅ Метод для получения названия товара
    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    # ✅ Метод для получения цены товара
    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    # ✅ Проверка названия товара в сообщении
    def should_be_success_message(self, product_name):
        success_name = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE_PRODUCT_NAME).text
        assert product_name == success_name, "Product name in message does not match"

    # ✅ Проверка цены корзины
    def should_be_correct_basket_price(self, product_price):
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL).text
        assert product_price == basket_price, "Basket price does not match product price"
