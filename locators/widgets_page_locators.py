from selenium.webdriver.common.by import By


class AccordianPageLocators:
    HEADER_SECTION1 = (By.ID, 'section1Heading')
    HEADER_SECTION2 = (By.ID, 'section2Heading')
    HEADER_SECTION3 = (By.ID, 'section3Heading')

    CONTENT_SECTION1 = (By.ID, 'section1Content')
    CONTENT_SECTION2 = (By.ID, 'section2Content')
    CONTENT_SECTION3 = (By.ID, 'section3Content')


class AutoCompletePageLocators:
    MULTI_INPUT = (By.ID, 'autoCompleteMultipleInput')
    MULTI_VALUE = (By.XPATH, '// div[@class="css-1rhbuit-multiValue auto-complete__multi-value"]')
    MULTI_VALUE_REMOVE = (By.XPATH, '// div[@class="css-xb97g8 auto-complete__multi-value__remove"]')

    SINGLE_INPUT = (By.ID, 'autoCompleteSingleInput')
    SINGLE_VALUE = (By.XPATH, '// div[@class="auto-complete__single-value css-1uccc91-singleValue"]')


class DatePickerPageLocators:
    INPUT_DATE = (By.ID, 'datePickerMonthYearInput')
    DATA_SELECT_MONTH = (By.XPATH, '// select[@class="react-datepicker__month-select"]')
    DATA_SELECT_YEAR = (By.XPATH, '// select[@class="react-datepicker__year-select"]')
    DATA_SELECT_DAY = (By.CSS_SELECTOR, 'div[class^="react-datepicker__day react-datepicker__day"]')

    INPUT_DATE_AND_TIME = (By.ID, 'dateAndTimePickerInput')
    DATA_AND_TIME_SELECT_MONTH = (By.XPATH, '//div[@class="react-datepicker__month-read-view"]')
    DATA_AND_TIME_SELECT_YEAR = (By.XPATH, '//div[@class="react-datepicker__year-read-view"]')
    DATA_AND_TIME_SELECT_DAY = (By.CSS_SELECTOR, 'div[class^="react-datepicker__day react-datepicker__day"]')
    DATA_AND_TIME_SELECT_TIME = (By.CSS_SELECTOR, 'li[class="react-datepicker__time-list-item "]')
    DATA_AND_TIME_SELECT_MONTH_LIST = (By.CSS_SELECTOR, 'div[class^="react-datepicker__month-option"]')
    DATA_AND_TIME_SELECT_YEAR_LIST = (By.CSS_SELECTOR, 'div[class^="react-datepicker__year-option"]')


class SliderPageLocators:
    SLIDER = (By.XPATH, '//input[@class="range-slider range-slider--primary"]')
    SLIDER_VALUE = (By.ID, 'sliderValue')


class ProgressBarPageLocators:
    START_STOP_BUTTON = (By.ID, 'startStopButton')
    PROGRESS_BAR_VALUE = (By.XPATH, '//div[@role="progressbar"]')


class TabsPageLocators:
    TAB_WHAT = (By.ID, 'demo-tab-what')
    WHAT_CONTENT = (By.CSS_SELECTOR, '#demo-tabpane-what p')
    ORIGIN_CONTENT = (By.CSS_SELECTOR, '#demo-tabpane-origin p')
    USE_CONTENT = (By.CSS_SELECTOR, '#demo-tabpane-use p')
    MORE_CONTENT = (By.CSS_SELECTOR, '#demo-tabpane-more p')
    TAB_ORIGIN = (By.ID, 'demo-tab-origin')
    TAB_USE = (By.ID, 'demo-tab-use')
    TAB_MORE = (By.ID, 'demo-tab-more')


class TooltipsPageLocators:
    BUTTON = (By.ID, 'toolTipButton')
    INPUT = (By.ID, 'toolTipTextField')
    LINK1 = (By.XPATH, '//div[@id="texToolTopContainer"]/a[1]')
    LINK2 = (By.XPATH, '//div[@id="texToolTopContainer"]/a[2]')

    TOOL_TIP = (By.XPATH, '//div[@class="tooltip-inner"]')


class MenuPageLocators:
    MENU_ITEM_LIST = (By. CSS_SELECTOR, 'ul[id="nav"] li a')


class SelectMenuPageLocators:

    SELECT_VALUE = (By.ID, 'withOptGroup')
    SELECT_VALUE_TEXT = (By.XPATH, '//div[@class=" css-1uccc91-singleValue"]')

    SELECT_ONE = (By.ID, 'selectOne')
    SELECT_ONE_TEXT = (By.XPATH, '//div[@class=" css-1uccc91-singleValue"]')

    OLD_STYLE_SELECT_MENU = (By.ID, 'oldSelectMenu')

