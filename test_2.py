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
import requests

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
        

# https://stackoverflow.com/questions/52760842/selenium-doesnt-open-the-specified-url-and-shows-data



# Path to Chromium bin
chromium_path = "Drivers/chrome-linux64/chrome"  # Replace with the actual path

# Set up Chrome options
chrome_options = Options()
chrome_options.binary_location = chromium_path

url = "https://www.kavak.com/mx/usado/kia-soul-20_ex_ivt_auto-suv-2021"
s = Service("chromedriver-linux64/chromedriver")

# General information
XPATH_NAME = '/html/body/app-root/div/app-landing/kdl-layout-main/main/app-main-grid/div[1]/div/div[2]/app-buy-box/section/div[1]/div[1]/h1'
XPATH_KM_CITY = '/html/body/app-root/div/app-landing/kdl-layout-main/main/app-main-grid/div[1]/div/div[2]/app-buy-box/section/div[1]/div[1]/p'


# Price
XPATH_PRICE = '/html/body/app-root/div/app-landing/kdl-layout-main/main/app-main-grid/div[1]/div/div[2]/app-buy-box/section/aui-price-product/div/div/div[2]/span[2]'
XPATH_PRICE_MONTH = '/html/body/app-root/div/app-landing/kdl-layout-main/main/app-main-grid/div[1]/div/div[2]/app-buy-box/section/aui-price-product/div/div/div[3]/span'

# Spects
XPATH_YEAR = '/html/body/app-root/div/app-landing/kdl-layout-main/main/app-main-grid/div[1]/div/div[2]/app-buy-box/section/app-filters/aui-accordion/div[1]/aui-accordion-group/div/h3/div/div[1]/div[2]'
XPATH_MODEL = '/html/body/app-root/div/app-landing/kdl-layout-main/main/app-main-grid/div[1]/div/div[2]/app-buy-box/section/app-filters/aui-accordion/div[2]/aui-accordion-group/div/h3/div/div[1]/div[2]'
XPATH_COMPLEMENTS = '//html/body/app-root/div/app-landing/kdl-layout-main/main/app-main-grid/div[1]/div/div[2]//aside'
# XPATH_COMPLEMENTS = '/html/body/app-root/div/app-landing/kdl-layout-main/main/app-main-grid/div[1]/div/div[3]/app-highlights/section/aui-carousel/div/div[2]/div/div'

XPATH_GENERAL_DESCRIPTIONS = '/html/body/app-root/div/app-landing/kdl-layout-main/main/app-main-grid/div[1]/div/div[3]/aui-features[1]/section'

# Special equipment
XPATH_SPECIAL_EQUIPMENT = '/html/body/app-root/div/app-landing/kdl-layout-main/main/app-main-grid/div[1]/div/div[3]/app-highlights/'

# Main Charecteristic
XPATH_CLOSE = '/html/body/app-root/div/app-landing/kdl-layout-main/main/app-main-grid/div[1]/div/div[2]/ahl-modal-auth/aui-drawer/div/div[2]/div[1]/aui-svg[2]'

XPATH_MAIN_CHARACTERISTICS_GENERAL_B = '/html/body/app-root/div/app-landing/kdl-layout-main/main/app-main-grid/div[1]/div/div[3]/aui-features[2]/section/aui-accordion/aui-accordion-group[1]/div/h3'
XPATH_MAIN_CHARACTERISTICS_GENERAL = '/html/body/app-root/div/app-landing/kdl-layout-main/main/app-main-grid/div[1]/div/div[3]/aui-features[2]/section/aui-accordion/aui-accordion-group[1]'
XPATH_MAIN_CHARACTERISTICS_OUTSIDE = '/html/body/app-root/div/app-landing/kdl-layout-main/main/app-main-grid/div[1]/div/div[3]/aui-features[2]/section/aui-accordion//aui-accordion-group[2]'
XPATH_MAIN_CHARACTERISTICS_EQUIPMENT_COMFORT = '/html/body/app-root/div/app-landing/kdl-layout-main/main/app-main-grid/div[1]/div/div[3]/aui-features[2]/section/aui-accordion/aui-accordion-group[3]/div/h3'
XPATH_MAIN_CHARACTERISTICS_SECURITY = '/html/body/app-root/div/app-landing/kdl-layout-main/main/app-main-grid/div[1]/div/div[3]/aui-features[2]/section/aui-accordion/aui-accordion-group[4]'
XPATH_MAIN_CHARACTERISTICS_INTERIOR = '/html/body/app-root/div/app-landing/kdl-layout-main/main/app-main-grid/div[1]/div/div[3]/aui-features[2]/section/aui-accordion/aui-accordion-group[5]'
XPATH_MAIN_CHARACTERISTICS_ENTERTAINMENT = '/html/body/app-root/div/app-landing/kdl-layout-main/main/app-main-grid/div[1]/div/div[3]/aui-features[2]/section/aui-accordion/aui-accordion-group[6]'

# Imperfections
# XPATH_IMPERFECTIONS = '/html/body/app-root/div/app-landing/kdl-layout-main/main/app-main-grid/div[2]/app-dimples/section/div/div[1]/div/app-dimple/div/div/'


def close_number():
    try:
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, XPATH_CLOSE))).click()
        # ActionChains(driver).move_to_element(WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, XPATH_CLOSE)))).click().perform()

    except:
        pass

# Pass the options to the WebDriver
with webdriver.Chrome(service=s, options=chrome_options) as driver:
    driver.get(url)
    
    # WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, XPATH_CLOSE))).click()

    # driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, XPATH_MAIN_CHARACTERISTICS_GENERAL_BUTTON))))
    # ActionChains(driver).move_to_element(WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, XPATH_CLOSE)))).click().perform()
    
    # close_number()

    # ActionChains(driver).move_to_element(WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, XPATH_MAIN_CHARACTERISTICS_GENERAL_BUTTON)))).click().perform()
    
    try:
        ActionChains(driver).move_to_element(WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, XPATH_MAIN_CHARACTERISTICS_GENERAL_B)))).click().perform()
        # WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, XPATH_MAIN_CHARACTERISTICS_GENERAL_B))).click()
        # close_number()
    except:
        print('Falló')
        close_number()
        ActionChains(driver).move_to_element(WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, XPATH_MAIN_CHARACTERISTICS_GENERAL_B)))).click().perform()
        # WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, XPATH_MAIN_CHARACTERISTICS_GENERAL_B))).click()
    
    # try:
    #     WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, XPATH_MAIN_CHARACTERISTICS_OUTSIDE))).click().perform()
    #     # ActionChains(driver).move_to_element(WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, XPATH_MAIN_CHARACTERISTICS_OUTSIDE)))).click().perform()
    #     close_number()
    # except:
    #     close_number()
    #     WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, XPATH_MAIN_CHARACTERISTICS_OUTSIDE))).click().perform()
    #     # ActionChains(driver).move_to_element(WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, XPATH_MAIN_CHARACTERISTICS_OUTSIDE)))).click().perform()

    # try:
    #     WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, XPATH_MAIN_CHARACTERISTICS_EQUIPMENT_COMFORT))).click()
    #     # ActionChains(driver).move_to_element(WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, XPATH_MAIN_CHARACTERISTICS_EQUIPMENT_COMFORT)))).click().perform()
    #     close_number()
    # except:
    #     close_number()
    #     WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, XPATH_MAIN_CHARACTERISTICS_EQUIPMENT_COMFORT))).click()
    #     # ActionChains(driver).move_to_element(WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, XPATH_MAIN_CHARACTERISTICS_EQUIPMENT_COMFORT)))).click().perform()

    # try:
    #     WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, XPATH_MAIN_CHARACTERISTICS_SECURITY))).click()
    #     # ActionChains(driver).move_to_element(WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, XPATH_MAIN_CHARACTERISTICS_SECURITY)))).click().perform()
    #     close_number()
    # except:
    #     close_number()
    #     WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, XPATH_MAIN_CHARACTERISTICS_SECURITY))).click()
    #     # ActionChains(driver).move_to_element(WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, XPATH_MAIN_CHARACTERISTICS_SECURITY)))).click().perform()

    # try:
    #     WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, XPATH_MAIN_CHARACTERISTICS_INTERIOR))).click()
    #     # ActionChains(driver).move_to_element(WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, XPATH_MAIN_CHARACTERISTICS_INTERIOR)))).click().perform()
    #     close_number()
    # except:
    #     close_number()
    #     WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, XPATH_MAIN_CHARACTERISTICS_INTERIOR))).click()
    #     # ActionChains(driver).move_to_element(WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, XPATH_MAIN_CHARACTERISTICS_INTERIOR)))).click().perform()

    # try:
    #     WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, XPATH_MAIN_CHARACTERISTICS_ENTERTAINMENT))).click()
    #     # ActionChains(driver).move_to_element(WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, XPATH_MAIN_CHARACTERISTICS_ENTERTAINMENT)))).click().perform()
    #     close_number()
    # except:
    #     close_number()
    #     WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, XPATH_MAIN_CHARACTERISTICS_ENTERTAINMENT))).click()
    #     # ActionChains(driver).move_to_element(WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, XPATH_MAIN_CHARACTERISTICS_ENTERTAINMENT)))).click().perform()

    json_parsed = {}
    json_parsed['url'] = url
    json_parsed['name'] = driver.find_element(By.XPATH,XPATH_NAME).text
    json_parsed['KM-city'] = driver.find_element(By.XPATH,XPATH_KM_CITY).text
    json_parsed['price'] = driver.find_element(By.XPATH,XPATH_PRICE).text
    json_parsed['month_price'] = driver.find_element(By.XPATH,XPATH_PRICE_MONTH).text
    json_parsed['year'] = driver.find_element(By.XPATH,XPATH_YEAR).text
    json_parsed['model'] = driver.find_element(By.XPATH,XPATH_MODEL).text
    # json_parsed['complements'] = driver.find_element(By.XPATH,XPATH_COMPLEMENTS).text

    # General descriptions
    json_parsed['general_descriptions'] = parse_arr(string_to_array(driver.find_element(By.XPATH,XPATH_GENERAL_DESCRIPTIONS).text))

    # Special equipment
    # json_parsed['special_equipment'] = parse_arr(driver.find_element(By.XPATH,XPATH_SPECIAL_EQUIPMENT).text)

    # Main Charecteristic
    json_parsed['main_characteristics'] = {}

    print('text', driver.find_element(By.XPATH,XPATH_MAIN_CHARACTERISTICS_GENERAL).text)
    print('arr', string_to_array(driver.find_element(By.XPATH,XPATH_MAIN_CHARACTERISTICS_GENERAL).text))
    print('parse', parse_arr(string_to_array(driver.find_element(By.XPATH,XPATH_MAIN_CHARACTERISTICS_GENERAL).text)))
    json_parsed['main_characteristics']['general'] = parse_arr(string_to_array(driver.find_element(By.XPATH,XPATH_MAIN_CHARACTERISTICS_GENERAL).text))['attributes']



    # json_parsed['main_characteristics']['outside'] = parse_arr(string_to_array(driver.find_element(By.XPATH,XPATH_MAIN_CHARACTERISTICS_OUTSIDE).text))['attributes']
    # json_parsed['main_characteristics']['equipment_confort'] = parse_arr(string_to_array(driver.find_element(By.XPATH,XPATH_MAIN_CHARACTERISTICS_EQUIPMENT_COMFORT).text))['attributes']
    # json_parsed['main_characteristics']['security'] = parse_arr(string_to_array(driver.find_element(By.XPATH,XPATH_MAIN_CHARACTERISTICS_SECURITY).text))['attributes']
    # json_parsed['main_characteristics']['interior'] = parse_arr(string_to_array(driver.find_element(By.XPATH,XPATH_MAIN_CHARACTERISTICS_INTERIOR).text))['attributes']
    # json_parsed['main_characteristics']['entretaiment'] = parse_arr(string_to_array(driver.find_element(By.XPATH,XPATH_MAIN_CHARACTERISTICS_ENTERTAINMENT).text))['attributes']

    # Imperfections
    # json_parsed['imperfections'] = len(parse_arr(driver.find_element(By.XPATH,XPATH_IMPERFECTIONS).text))

    create_json_file(json_parsed, 'test')