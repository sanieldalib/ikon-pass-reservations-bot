import time
import os
import json

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from config import IKON_RESORTS

class IkonDriver:
    def __init__(self, preferences, username=os.environ.get('IKON_EMAIL'), password=os.environ.get('IKON_PASSWORD')):
        chrome_options = Options()

        self.driver = webdriver.Chrome(options=chrome_options, executable_path='/usr/local/bin/chromedriver')
        self.preferences = preferences
        self.wait = WebDriverWait(self.driver, 5)
        self.login_url = 'https://account.ikonpass.com/en/login'
        self.previous_url = self.login_url
        self.username = username
        self.password = password
        # self.reservation_date = reservation_date
        self.setup()

    def setup(self):
        self.driver.maximize_window()

    def get_login_form_info(self):
        self.driver.get(self.login_url)

        username_field_id = self.driver.find_element_by_id('email')
        password_field_id = self.driver.find_element_by_id('sign-in-password')
        submit_button_class = self.wait.until(ec.visibility_of_element_located((By.CLASS_NAME, 'submit')))

        return username_field_id, password_field_id, submit_button_class

    def login(self):

        username_field_id, password_field_id, submit_button_class = self.get_login_form_info()

        username_field_id.send_keys(self.username)
        password_field_id.send_keys(self.password)
        submit_button_class.click()

        self.validate_move()

    def get_availability(self, venue):
        url = 'https://account.ikonpass.com/api/v2/reservation-availability/{}'.format(venue)
        self.driver.get(url)

        if url != self.previous_url:
            self.validate_move()
        pre = self.driver.find_element_by_tag_name("pre").text
        data = json.loads(pre)
        return data['data'][0]['unavailable_dates']

    def check_dates(self, unavailable_dates):
        results = self.preferences.copy()
        for idx, pref in enumerate(results):
            if pref.date not in unavailable_dates[idx]:
                pref.available = True
        
        return results

    def check_availability(self):
        self.login()

        unavailable_dates = [self.get_availability(pref.resort_id) for pref in self.preferences]
        return self.check_dates(unavailable_dates)

    def validate_move(self):
        # We give the application 5 seconds to move to the new page before timing out
        timeout_count = 0

        while self.previous_url == self.driver.current_url:
            time.sleep(1)
            timeout_count += 1
            if timeout_count == 4:
                print(f'Failed to navigate from {self.previous_url}.')
                exit()

        print(f'Successfully navigated from {self.previous_url} to {self.driver.current_url}.')
        self.previous_url = self.driver.current_url

    def close_driver(self):
        print('Closing the Chrome WebDriver.')
        self.driver.close()