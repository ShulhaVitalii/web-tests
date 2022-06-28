import random
import time

import pytest

from locators.elements_page_locators import LinksPageLocators
from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablePage, ButtonsPage, LinksPage


class TestElements:
    class TestTextBox:

        def test_text_box(self, driver):
            test_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            test_box_page.open()
            input_data = test_box_page.fill_all_fields()
            output_data = test_box_page.check_filled_form()
            for i in range(len(input_data)):
                assert input_data[i] == output_data[i], f'data {input_data[i]} does not match'

    class TestCheckBox:
        def test_check_box(self, driver):
            check_box_page = CheckBoxPage(driver, 'https://demoqa.com/checkbox')
            check_box_page.open()
            check_box_page.open_full_list()
            check_box_page.click_on_random_checkbox_ten_times()
            check_box_page.check_result()
            time.sleep(5)

    class TestRadioButton:
        def test_radio_button(self, driver):
            radio_button_page = RadioButtonPage(driver, 'https://demoqa.com/radio-button')
            radio_button_page.open()
            radio_button_page.click_on_yes_radio()
            radio_button_page.click_on_impressive_radio()
            radio_button_page.click_on_no_radio()

    class TestWebTable:
        def test_web_table_add_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            web_table_page.checking_that_new_person_is_in_table()
            time.sleep(5)

        def test_web_table_search_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            key = web_table_page.new_person()[random.randint(0, 5)]
            web_table_page.search_some_person(key)
            table_result = web_table_page.check_search_person()
            assert key in table_result, f'Key {key} is not found in the table'

        def test_web_table_update_person_info(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            lastname = web_table_page.new_person()[1]
            web_table_page.search_some_person(lastname)
            age = web_table_page.update_person_info()
            row = web_table_page.check_search_person()
            assert age in row, 'The person card has not been changed'

        def test_web_table_delete_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            email = web_table_page.new_person()[3]
            web_table_page.search_some_person(email)
            web_table_page.delete_person()
            text = web_table_page.check_deleting()
            assert text == 'No rows found', f'Person with email: {email} do not deleted'

        def test_web_table_change_count_row(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            count = web_table_page.select_up_to_some_rows()
            assert count == [5, 10, 20, 25, 50, 100], 'The number of rows in the table has not been changed or ' \
                                                      'changed incorrect'

    class TestButtons:
        def test_all_buttons_are_working_correctly(self, driver):
            button_page = ButtonsPage(driver, 'https://demoqa.com/buttons')
            button_page.open()
            button_page.click_on_the_buttons()

    class TestLinks:
        @pytest.mark.parametrize('link', [LinksPageLocators.LINK_HOME, LinksPageLocators.DYNAMIC_LINK])
        def test_new_page_open_after_click_on_link(self, driver, link):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            links_page.check_that_new_page_is_opened(link)

        @pytest.mark.parametrize('link, code, text', [(LinksPageLocators.LINK_CREATE, 201, 'Created'),
                                                      (LinksPageLocators.LINK_NO_CONTENT, 204, 'No Content'),
                                                      (LinksPageLocators.LINK_MOVED, 301, 'Moved Permanently'),
                                                      (LinksPageLocators.LINK_BAD_REQUEST, 400, 'Bad Request'),
                                                      (LinksPageLocators.LINK_UNAUTHORIZED, 401, 'Unauthorized'),
                                                      (LinksPageLocators.LINK_FORBIDDEN, 403, 'Forbidden'),
                                                      (LinksPageLocators.LINK_NO_FOUND, 404, 'Not Found')])
        def test_api_call_send_correct(self, driver, link, code, text):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            links_page.check_api_call(link, code, text)
