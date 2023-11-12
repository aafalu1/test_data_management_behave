from selenium import webdriver
import os

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


def get_chrome_driver():
    driver_path = os.environ.get("DRIVERS_EXECUTABLES")
    exe=os.path.join(driver_path, 'chromedriver.exe')
    chrome_binary = os.environ.get('CHROME_DIR')
    my_file= os.path.join(chrome_binary, "chrome.exe")
    options = Options()
    options.binary_location = my_file
    options.add_argument('--disable-gpu')
    options.add_argument("--no-sandbox")
    service = Service(executable_path=exe)
    driver=webdriver.Chrome(service=service, options=options)
    return driver
