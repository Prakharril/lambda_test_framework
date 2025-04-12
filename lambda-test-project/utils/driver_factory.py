import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from dotenv import load_dotenv

load_dotenv()
username = os.getenv("LT_USERNAME")
access_key = os.getenv("LT_ACCESS_KEY")

def get_driver(test_name, build_name):
    options = ChromeOptions()
    options.browser_version = "135"
    options.platform_name = "Windows 10"

    lt_options = {
        "username": username,
        "accessKey": access_key,
        "build": build_name,
        "project": "HackathonProject",
        "name": test_name,
        "w3c": True,
        "plugin": "python-python"
    }

    options.set_capability('LT:Options', lt_options)

    driver = webdriver.Remote(
        command_executor=f"https://{username}:{access_key}@hub.lambdatest.com/wd/hub",
        options=options
    )
    return driver
