import time
import os 
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait       
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import lxml.html as html

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

def scrap_page(chromium_path, service_path, XPATH, url):
    s = Service(service_path)
    chrome_options = Options()
    chrome_options.binary_location = chromium_path
    with webdriver.Chrome(service=s, options=chrome_options) as driver:
        driver.get(url)
        driver.maximize_window()
        close_cookies(driver, XPATH['XPATH_COOKIES'])
        json_parsed = {}
        json_parsed['url'] = url
        json_parsed['name'] = driver.find_element(By.XPATH,XPATH['XPATH_NAME']).text
        json_parsed['KM-city'] = driver.find_element(By.XPATH,XPATH['XPATH_KM_CITY']).text
        json_parsed['price'] = driver.find_element(By.XPATH,XPATH['XPATH_PRICE']).text
        json_parsed['month_price'] = driver.find_element(By.XPATH,XPATH['XPATH_PRICE_MONTH']).text
        json_parsed['year'] = driver.find_element(By.XPATH,XPATH['XPATH_YEAR']).text
        json_parsed['model'] = driver.find_element(By.XPATH,XPATH['XPATH_MODEL']).text
        # json_parsed['complements'] = driver.find_element(By.XPATH,XPATH_COMPLEMENTS).text

        # General descriptions
        json_parsed['general_descriptions'] = parse_arr(string_to_array(driver.find_element(By.XPATH,XPATH['XPATH_GENERAL_DESCRIPTIONS']).text))['attributes']

        # Special equipment
        # json_parsed['special_equipment'] = parse_arr(driver.find_element(By.XPATH,XPATH_SPECIAL_EQUIPMENT).text)

        # Main Charecteristic
        json_parsed['main_characteristics'] = {}

        open_menu(driver, XPATH['XPATH_MAIN_CHARACTERISTICS_GENERAL'], 'General', XPATH['XPATH_CLOSE'])
        json_parsed['main_characteristics']['general'] = parse_arr(string_to_array(driver.find_element(By.XPATH,XPATH['XPATH_MAIN_CHARACTERISTICS_GENERAL']).text))['attributes']
        # time.sleep(15)
        open_menu(driver,XPATH['XPATH_MAIN_CHARACTERISTICS_OUTSIDE'], 'Outside', XPATH['XPATH_CLOSE'])
        json_parsed['main_characteristics']['outside'] = parse_arr(string_to_array(driver.find_element(By.XPATH,XPATH['XPATH_MAIN_CHARACTERISTICS_OUTSIDE']).text))['attributes']

        open_menu(driver,XPATH['XPATH_MAIN_CHARACTERISTICS_EQUIPMENT_COMFORT'], 'Comfort', XPATH['XPATH_CLOSE'])
        json_parsed['main_characteristics']['equipment_confort'] = parse_arr(string_to_array(driver.find_element(By.XPATH,XPATH['XPATH_MAIN_CHARACTERISTICS_EQUIPMENT_COMFORT']).text))['attributes']

        open_menu(driver,XPATH['XPATH_MAIN_CHARACTERISTICS_SECURITY'], 'Security', XPATH['XPATH_CLOSE'])
        json_parsed['main_characteristics']['security'] = parse_arr(string_to_array(driver.find_element(By.XPATH,XPATH['XPATH_MAIN_CHARACTERISTICS_SECURITY']).text))['attributes']

        open_menu(driver,XPATH['XPATH_MAIN_CHARACTERISTICS_INTERIOR'], 'Interior', XPATH['XPATH_CLOSE'])
        json_parsed['main_characteristics']['interior'] = parse_arr(string_to_array(driver.find_element(By.XPATH,XPATH['XPATH_MAIN_CHARACTERISTICS_INTERIOR']).text))['attributes']

        open_menu(driver,XPATH['XPATH_MAIN_CHARACTERISTICS_ENTERTAINMENT'], 'Entertaiment', XPATH['XPATH_CLOSE'])
        json_parsed['main_characteristics']['entretaiment'] = parse_arr(string_to_array(driver.find_element(By.XPATH,XPATH['XPATH_MAIN_CHARACTERISTICS_ENTERTAINMENT']).text))['attributes']

        # Imperfections
        # json_parsed['imperfections'] = len(parse_arr(driver.find_element(By.XPATH,XPATH_IMPERFECTIONS).text))

        # Stock ID
        print(f'Creando documento {json_parsed["general_descriptions"]["Stock ID"]} json')
        create_json_file(json_parsed, json_parsed["general_descriptions"]["Stock ID"])
        time.sleep(5)

# if __name__ == "__main__":
# 	run()