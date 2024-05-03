import time
import os 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait       
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

import lxml.html as html
import json

def string_to_array(input_string):
    lines = input_string.split('\n')
    result = []
    for line in lines:
        if line.strip():
            elements = line.split(',')
            for element in elements:
                element = element.strip()
                result.append(element)
    return result

def parse_arr(arr):
    category = arr.pop(0)
    json_data = {}
    json_data['category'] = category.strip()
    json_data['attributes'] = {}
    for i in range(0, len(arr), 2):
        key = arr[i].strip()
        value = arr[i + 1]
        json_data['attributes'][key] = value
    return json_data

def create_json_file(json_data, file_name):
    with open(f'{file_name}.json', 'w', encoding='utf-8') as json_file:
        json.dump(json_data, json_file, indent=4, ensure_ascii=False)

def close_cookies(driver, XPATH_COOKIES):
    try:
        print("Attempting to accept cookie terms popup")
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, XPATH_COOKIES))).click()
        print("Cookies accepted")
    except:
        print("Failed to accept cookie terms popup")
        pass

def close_popup(driver, XPATH_CLOSE):
    try:
        print("Trying to close the popup window")
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, XPATH_CLOSE))).click()
        print("Popup closed")
    except:
        print("Failed to close the window")
        pass

def open_menu(driver, xpath_menu, msg, XPATH_CLOSE):
    try:
        print("Trying to open the menu ->", msg, "<-")
        ActionChains(driver).move_to_element(WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath_menu)))).click().perform()
        print("Menu closed")
        ActionChains(driver).move_to_element(WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath_menu)))).click().perform()
        print("Menu opened")
    except:
        print('Failed to open the menu')
        print("Closing window")
        close_popup(driver, XPATH_CLOSE)
        print("Trying to click")
        ActionChains(driver).move_to_element(WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath_menu)))).click().perform()

# if __name__ == "__main__":
# 	run()