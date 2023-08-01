from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_guest_can_go_to_login_page(r_browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    browser = r_browser
    wait = WebDriverWait(browser, 8)
    browser.get(link)
    button_for_edding_in_basket = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "btn.btn-lg.btn-primary.btn-add-to-basket")))