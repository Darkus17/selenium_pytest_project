from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    browser.get(link)

    login_link = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.ID, "login_link"))
    )
    login_link.click()
