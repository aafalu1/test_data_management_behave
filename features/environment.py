import base64

from behave import *
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from features.utility.csv_util import CsvUtil
from features.utility.data_storage import DataStorage


def get_webdriver(browser):
    driver_exe_dir = os.environ.get("DRIVERS_EXECUTABLES")
    chrome_driver_file = os.path.join(driver_exe_dir, "chromedriver.exe")
    chrome_exe_dir = os.environ.get("CHROME_DIR")
    chrome_binary_location = os.path.join(chrome_exe_dir, "chrome.exe")
    if not os.path.isfile(chrome_driver_file):
        raise ValueError(f"Chrome driver file not found at: {
                         chrome_driver_file}")

    options = Options()
    options.binary_location = chrome_binary_location
    options.add_argument('--disable-gpu')
    service = Service(executable_path=chrome_driver_file)
    return webdriver.Chrome(service=service, options=options)


def maximize_window(context):
    context.driver.maximize_window()


def quit_driver(context):
    context.driver.quit()


def embed_screenshot(context, caption):
    screenshot_data = context.driver.get_screenshot_as_png()
    # Read the screenshot file as binary data
    base64_encoded_data = base64.b64encode(screenshot_data).decode()
    context.formatter.embed(mime_type="image/png",
                            data=base64_encoded_data, caption=caption)


@fixture
def browser_fixture(context, **kwargs):
    browser = "chrome"
    context.driver = get_webdriver(browser)
    maximize_window(context)
    yield context.driver
    quit_driver(context)


def before_all(context):
    context.data_storage = DataStorage()
    excel_data = CsvUtil.read_excel_file("test_data.xlsx")
    context.excel_data = excel_data
    for formatter in context._runner.formatters:
        if formatter.name == "html-pretty":
            context.formatter = formatter
        if "html" in formatter.name:
            context.html_formatter = formatter


def before_scenario(context, scenario):
    context.config.userdata['my_input_runner_tag']=context.tags
    # use_fixture(browser_fixture, context, driver=scenario)


def after_scenario(context, scenario):
    pass
    # if scenario.status == "failed":
    # embed_screenshot(context, caption="Screenshot")


def after_all(context):
    tags= context.config.userdata['my_input_runner_tag']
    if "input" in tags:
        data = dict(context.data_storage.data_dict)
        CsvUtil().write_to_csv(data, context.config.userdata['csv_file_path'])