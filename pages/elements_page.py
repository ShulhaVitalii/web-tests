import base64
import os
import random
import time

import allure
import requests
from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from generator.generator import generated_person, generated_file
from locators.elements_page_locators import TextBoxPageLocators, CheckBoxPageLocators, RadioButtonPageLocators, \
    WebTablePageLocators, ButtonsPageLocators, LinksPageLocators, UploadDownloadPageLocators, \
    DynamicPropertiesPageLocators
from pages.base_page import BasePage


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    @allure.step('Fill all fields')
    def fill_all_fields(self):
        person_info = next(generated_person())
        full_name = person_info.full_name
        email = person_info.email
        current_address = person_info.current_address.replace('\n', '')
        permanent_address = person_info.permanent_address.replace('\n', '')
        with allure.step('Filling fields'):
            self.element_is_visible(self.locators.FULL_NAME).send_keys(full_name)
            self.element_is_visible(self.locators.EMAIL).send_keys(email)
            self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(current_address)
            self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys(permanent_address)
        with allure.step('Click on the submit button'):
            self.element_is_clickable(self.locators.SUBMIT).click()
        return full_name, email, current_address, permanent_address

    @allure.step('Checking fields')
    def check_filled_form(self):
        full_name = self.element_is_present(self.locators.CREATED_FULL_NAME).text.split(':')[1]
        email = self.element_is_present(self.locators.CREATED_EMAIL).text.split(':')[1]
        current_address = self.element_is_present(self.locators.CREATED_CURRENT_ADDRESS).text.split(':')[1]
        permanent_address = self.element_is_present(self.locators.CREATED_PERMANENT_ADDRESS).text.split(':')[1]
        return full_name, email, current_address, permanent_address


class CheckBoxPage(BasePage):
    locators = CheckBoxPageLocators()

    @allure.step('Open full list')
    def open_full_list(self):
        self.element_is_visible(self.locators.BUTTON_EXPAND_ALL).click()

    @allure.step('Click on random checkbox')
    def click_random_check_box(self):
        item_list = self.element_are_visible(self.locators.ITEM_LIST)
        item = item_list[random.randrange(len(item_list))]
        self.go_to_element(item)
        item.click()

    @allure.step('Click on random checkbox 10 times')
    def click_on_random_checkbox_ten_times(self):
        for _ in range(10):
            self.click_random_check_box()

    @allure.step('Getting checking checkbox')
    def get_checked_checkboxes(self):
        checked_list = self.element_are_present(self.locators.CHECKED_ITEMS)
        data = []
        for box in checked_list:
            title_item = box.find_element(By.XPATH, self.locators.TITLE_ITEM)
            data.append(title_item.text.lower().replace(' ', '').replace('.doc', ''))
        return data

    @allure.step('Get output result')
    def get_output_result(self):
        output_result_list = self.element_are_present(self.locators.OUTPUT_RESULT)
        data = []
        for item in output_result_list:
            data.append(item.text.lower())
        return data

    @allure.step('Checking result')
    def check_result(self):
        checked, outputs = self.get_checked_checkboxes(), self.get_output_result()
        assert checked == outputs, f'list {checked} and {outputs} are not equal'


class RadioButtonPage(BasePage):
    locators = RadioButtonPageLocators()

    @allure.step('Click on Yes radio button')
    def click_on_yes_radio(self):
        self.element_is_clickable(self.locators.RADIO_YES).click()
        assert self.element_is_present(self.locators.SELECTED_RADIO).text == 'Yes', 'radio Yes is not active'

    @allure.step('Click on impressive radio button')
    def click_on_impressive_radio(self):
        self.element_is_clickable(self.locators.RADIO_IMPRESSIVE).click()
        assert self.element_is_present(self.locators.SELECTED_RADIO).text == 'Impressive',\
            'radio impressive is not active'

    @allure.step('Click on No radio button')
    def click_on_no_radio(self):
        self.element_is_clickable(self.locators.RADIO_NO).click()
        assert self.element_is_present(self.locators.SELECTED_RADIO).text == 'No', 'radio No is not active'


class WebTablePage(BasePage):
    locators = WebTablePageLocators()

    @allure.step('Create new person')
    def new_person(self):
        count = 1
        while count != 0:
            person_info = next(generated_person())
            firstname = person_info.firstname
            lastname = person_info.lastname
            email = person_info.email
            age = person_info.age
            salary = person_info.salary
            department = person_info.department

            self.element_is_visible(self.locators.ADD_BUTTON).click()
            self.element_is_visible(self.locators.FIRSTNAME_INPUT).send_keys(firstname)
            self.element_is_visible(self.locators.LASTNAME_INPUT).send_keys(lastname)
            self.element_is_visible(self.locators.EMAIL_INPUT).send_keys(email)
            self.element_is_visible(self.locators.AGE_INPUT).send_keys(age)
            self.element_is_visible(self.locators.SALARY_INPUT).send_keys(salary)
            self.element_is_visible(self.locators.DEPARTMENT_INPUT).send_keys(department)

            self.element_is_visible(self.locators.SUBMIT).click()

            count -= 1
            return [firstname, lastname, str(age), email, str(salary), department]

    @allure.step('Check new person')
    def check_new_person(self):
        person_list = self.element_are_present(self.locators.FULL_PEOPLE_LIST)
        data = []
        for item in person_list:
            data.append(item.text.splitlines())
        return data

    @allure.step('Checking that new person is in the table')
    def checking_that_new_person_is_in_table(self):
        assert self.new_person() in self.check_new_person()

    @allure.step('Search person')
    def search_some_person(self, key):
        self.element_is_visible(self.locators.SEARCH_INPUT).send_keys(key)

    @allure.step('Checking search person')
    def check_search_person(self):
        delete_button = self.element_are_present(self.locators.DELETE_BUTTON)
        row = delete_button[0].find_element(By.XPATH, self.locators.ROW_PARENT)
        return row.text.splitlines()

    @allure.step('Updating person info')
    def update_person_info(self):
        person_info = next(generated_person())
        age = person_info.age
        self.element_is_visible(self.locators.EDIT_BUTTON).click()
        self.element_is_visible(self.locators.AGE_INPUT).clear()
        self.element_is_visible(self.locators.AGE_INPUT).send_keys(age)
        self.element_is_visible(self.locators.SUBMIT).click()
        return str(age)

    @allure.step('Deleting person')
    def delete_person(self):
        self.element_is_visible(self.locators.DELETE_BUTTON).click()

    @allure.step('Checking that person really deleted')
    def check_deleting(self):
        return self.element_is_present(self.locators.NO_ROWS_FOUND_TEXT).text

    @allure.step('Select up to some rows')
    def select_up_to_some_rows(self):
        count = [5, 10, 20, 25, 50, 100]
        data = []
        for x in count:
            count_row_button = self.element_is_visible(self.locators.COUNT_ROW_LIST)
            self.go_to_element(count_row_button)
            count_row_button.click()
            self.element_is_visible((By.CSS_SELECTOR, f'option[value={x}]')).click()
            data.append(self.check_count_rows())
        return data

    @allure.step('Checking count rows')
    def check_count_rows(self):
        rows_list = self.element_are_present(self.locators.FULL_PEOPLE_LIST)
        return len(rows_list)


class ButtonsPage(BasePage):
    locators = ButtonsPageLocators()

    @allure.step('Click on the buttons')
    def click_on_the_buttons(self):
        button_double_click = self.element_is_visible(self.locators.BUTTON_DOUBLE_CLICK_ME)
        self.action_double_click(button_double_click)
        text = self.check_clicked_on_the_button(self.locators.DOUBLE_CLICK_MESSAGE)
        assert text == 'You have done a double click', 'You have not done a double click'

        button_right_click = self.element_is_visible(self.locators.BUTTON_RIGHT_CLICK_ME)
        self.action_right_click(button_right_click)
        text = self.check_clicked_on_the_button(self.locators.RIGHT_CLICK_MESSAGE)
        assert text == 'You have done a right click', 'You have not done a right click'

        self.element_is_visible(self.locators.BUTTON_CLICK_ME).click()
        text = self.check_clicked_on_the_button(self.locators.DYNAMIC_CLICK_MESSAGE)
        assert text == 'You have done a dynamic click', 'You have not done a dynamic click'

    @allure.step('Checking click on the button')
    def check_clicked_on_the_button(self, element):
        return self.element_is_present(element).text


class LinksPage(BasePage):
    locators = LinksPageLocators()

    @allure.step('Checking that new page is open')
    def check_that_new_page_is_opened(self, locator):
        link = self.element_is_visible(locator)
        link_href = link.get_attribute('href')
        request = requests.get(link_href)
        if request.status_code == 200:
            link.click()
        self.switch_to_new_tab()
        assert self.driver.current_url == link_href

    @allure.step('Checking api call')
    def check_api_call(self, locator, code, tex):
        self.element_is_visible(locator).click()
        text = self.element_is_visible(self.locators.RESPONSE).text
        assert text == f'Link has responded with staus {code} and status text {tex}'


class UploadDownloadPage(BasePage):
    locators = UploadDownloadPageLocators()

    @allure.step('Uploading file')
    def upload_file(self):
        file_name, path = generated_file()
        self.element_is_present(self.locators.UPLOAD_BUTTON).send_keys(path)
        os.remove(path)
        text_after_upload = self.element_is_present(self.locators.UPLOADED_FILE_PATH).text
        assert text_after_upload == rf'C:\fakepath\{file_name}', 'The file has ho been upload'

    @allure.step('Downloading file')
    def download_file(self):
        link = self.element_is_present(self.locators.DOWNLOAD_BUTTON).get_attribute('href')
        print(link)
        link = base64.b64decode(link)
        path = rf'D:\Test-Framework-for-web\img{random.randint(1, 999)}.jpg'
        with open(path, 'wb+') as f:
            offset = link.find(b'\xff\xd8')
            f.write(link[offset:])
            check_file = os.path.exists(path)
            f.close()
        os.remove(path)
        assert check_file is True, 'The file has ho been download'


class DynamicPropertiesPage(BasePage):
    locators = DynamicPropertiesPageLocators()

    @allure.step('Checking color change')
    def check_change_of_color(self):
        color_button = self.element_is_present(self.locators.COLOR_CHANGED_BUTTON)
        color_before = color_button.value_of_css_property('color')
        time.sleep(5)
        color_after = color_button.value_of_css_property('color')
        assert color_before != color_after

    @allure.step('Checking that the button is enabled')
    def check_that_button_is_enabled(self):
        try:
            self.element_is_present(self.locators.ENABLED_AFTER_BUTTON)
        except TimeoutException:
            return False
        return True

    @allure.step('Checking the button is appear')
    def check_button_appear(self):
        try:
            self.element_is_visible(self.locators.VISIBLE_AFTER_BUTTON)
        except TimeoutException:
            return False
        return True

