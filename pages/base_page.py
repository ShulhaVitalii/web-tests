from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def element_is_visible(self, locator, timeout=10):
        self.go_to_element(self.element_is_present(locator))
        return wait(self.driver, timeout).until(ec.visibility_of_element_located(locator))

    def element_are_visible(self, locator, timeout=10):
        return wait(self.driver, timeout).until(ec.visibility_of_all_elements_located(locator))

    def element_is_present(self, locator, timeout=10):
        return wait(self.driver, timeout).until(ec.presence_of_element_located(locator))

    def element_are_present(self, locator, timeout=10):
        return wait(self.driver, timeout).until(ec.presence_of_all_elements_located(locator))

    def element_is_not_visible(self, locator, timeout=10):
        return wait(self.driver, timeout).until(ec.invisibility_of_element_located(locator))

    def element_is_clickable(self, locator, timeout=10):
        return wait(self.driver, timeout).until(ec.element_to_be_clickable(locator))

    def go_to_element(self, locator):
        self.driver.execute_script("arguments[0].scrollIntoView();", locator)

    def action_right_click(self, locator):
        action = ActionChains(self.driver)
        action.context_click(locator).perform()

    def action_double_click(self, locator):
        action = ActionChains(self.driver)
        action.double_click(locator).perform()

    def switch_to_new_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    def remove_footer(self):
        self.driver.execute_script("document.getElementsByTagName('footer')[0].remove();")
        self.driver.execute_script("document.getElementById('close-fixedban').remove();")
        self.driver.execute_script("document.getElementById('adplus-anchor').remove();")

    def check_new_tab(self, locator1, locator2):
        self.element_is_visible(locator1).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        text = self.element_is_visible(locator2).text
        return text
