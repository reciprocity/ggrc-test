'''
Created on Feb 11, 2013

@author: diana.tzinov
'''
from os.path import expanduser 
import sys, os

# the possible environment values are "STAGE", "USER"   "PRODUCTION","INTEGRATION",

#url = os.getenv('TEST_SITE_URL', "http://grc-test.appspot.com/")


url = os.getenv('TEST_SITE_URL', "http://localhost:8080")
remote_webdriver_url = os.getenv('REMOTE_WEBDRIVER_URL', None)
use_remote_webdriver = bool(remote_webdriver_url)
chrome_driver_filename = os.getenv('CHROME_DRIVER_PATH', "~/chromedriver")
file_download_path = os.getenv('FILE_DOWNLOAD_PATH', '.')
test_db = os.getenv('TEST_DB_PATH', "/test_db")
username = os.getenv('TEST_SITE_USERNAME', None)
password = os.getenv('TEST_SITE_PASSWORD', None)
jasmine_url = "file:///Users/diana.tzinov/Downloads/jasmine/jasmine-all-good.htm"
browser = "chrome"
environment = ""
user = ""