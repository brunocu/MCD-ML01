import time
import os 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

import lxml.html as html
import json
import requests

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
        
def parse_link(html_tree):
  try:
    parsed = html_tree
    try:
        json_parsed = {}
        json_parsed['name'] = parsed.xpath(XPATH_NAME)
        json_parsed['KM-city'] = parsed.xpath(XPATH_KM_CITY)
        json_parsed['price'] = parsed.xpath(XPATH_PRICE)
        json_parsed['month_price'] = parsed.xpath(XPATH_PRICE_MONTH)
        json_parsed['year'] = parsed.xpath(XPATH_YEAR)
        json_parsed['model'] = parsed.xpath(XPATH_MODEL)

        print('Complements', parsed.xpath(XPATH_COMPLEMENTS))

        driver.get(url)
        print('Complements 2', driver.find_element(By.XPATH_COMPLEMENTS,XPATH_NAME)
        json_parsed['complements'] = parsed.xpath(XPATH_COMPLEMENTS)

        # json_parsed['complements'] = parsed.xpath(XPATH_COMPLEMENTS)
        
        # # General descriptions
        # json_parsed['general_descriptions'] = parse_arr(parsed.xpath(XPATH_GENERAL_DESCRIPTIONS).copy())

        # # Special equipment
        # json_parsed['special_equipment'] = parse_arr(parsed.xpath(XPATH_SPECIAL_EQUIPMENT).copy())

        # # Main Charecteristic
        # json_parsed['main_characteristics'] = {}
        # json_parsed['main_characteristics']['general'] = parse_arr(parsed.xpath(XPATH_MAIN_CHARACTERISTICS_GENERAL).copy())['attributes']
        # json_parsed['main_characteristics']['outside'] = parse_arr(parsed.xpath(XPATH_MAIN_CHARACTERISTICS_OUTSIDE).copy())['attributes']
        # json_parsed['main_characteristics']['equipment_confort'] = parse_arr(parsed.xpath(XPATH_MAIN_CHARACTERISTICS_EQUIPMENT_COMFORT).copy())['attributes']
        # json_parsed['main_characteristics']['security'] = parse_arr(parsed.xpath(XPATH_MAIN_CHARACTERISTICS_SECURITY).copy())['attributes']
        # json_parsed['main_characteristics']['interior'] = parse_arr(parsed.xpath(XPATH_MAIN_CHARACTERISTICS_INTERIOR).copy())['attributes']
        # json_parsed['main_characteristics']['entretaiment'] = parse_arr(parsed.xpath(XPATH_MAIN_CHARACTERISTICS_ENTERTAINMENT).copy())['attributes']

        # # Imperfections
        # json_parsed['imperfections'] = len(parse_arr(parsed.xpath(XPATH_IMPERFECTIONS).copy()))

        print(json_parsed)

    except IndexError:
        return
    else:
       pass
    #   raise ValueError(f'Error:{response.status_code}')
  except ValueError as ve:
    print(ve)
  # return json_parsed



# https://stackoverflow.com/questions/52760842/selenium-doesnt-open-the-specified-url-and-shows-data



# Path to Chromium bin
chromium_path = "Drivers/chrome-linux64/chrome"  # Replace with the actual path

# Set up Chrome options
chrome_options = Options()
chrome_options.binary_location = chromium_path

url = "https://www.kavak.com/mx/usado/kia-soul-20_ex_ivt_auto-suv-2021"
s = Service("chromedriver-linux64/chromedriver")

# General information
XPATH_NAME = '/html/body/app-root/div/app-landing/kdl-layout-main/main/app-main-grid/div[1]/div/div[2]/app-buy-box/section/div[1]/div[1]/h1/text()'
XPATH_KM_CITY = '/html/body/app-root/div/app-landing/kdl-layout-main/main/app-main-grid/div[1]/div/div[2]/app-buy-box/section/div[1]/div[1]/p/text()'


# Price
XPATH_PRICE = '/html/body/app-root/div/app-landing/kdl-layout-main/main/app-main-grid/div[1]/div/div[2]/app-buy-box/section/aui-price-product/div/div/div[2]/span[2]/text()'
XPATH_PRICE_MONTH = '/html/body/app-root/div/app-landing/kdl-layout-main/main/app-main-grid/div[1]/div/div[2]/app-buy-box/section/aui-price-product/div/div/div[3]/span/text()'

# Spects
XPATH_YEAR = '/html/body/app-root/div/app-landing/kdl-layout-main/main/app-main-grid/div[1]/div/div[2]/app-buy-box/section/app-filters/aui-accordion/div[1]/aui-accordion-group/div/h3/div/div[1]/div[2]//text()'
XPATH_MODEL = '/html/body/app-root/div/app-landing/kdl-layout-main/main/app-main-grid/div[1]/div/div[2]/app-buy-box/section/app-filters/aui-accordion/div[2]/aui-accordion-group/div/h3/div/div[1]/div[2]//text()'
XPATH_COMPLEMENTS = '//html/body/app-root/div/app-landing/kdl-layout-main/main/app-main-grid/div[1]/div/div[2]//aside/text()'
# XPATH_COMPLEMENTS = '/html/body/app-root/div/app-landing/kdl-layout-main/main/app-main-grid/div[1]/div/div[3]/app-highlights/section/aui-carousel/div/div[2]/div/div'

# General descriptions
XPATH_GENERAL_DESCRIPTIONS = '/html/body/app-root/div/app-landing/kdl-layout-main/main/app-main-grid/div[1]/div/div[3]/aui-features[1]/section//text()'

# Special equipment
XPATH_SPECIAL_EQUIPMENT = '/html/body/app-root/div/app-landing/kdl-layout-main/main/app-main-grid/div[1]/div/div[3]/app-highlights//text()'

# Main Charecteristic
XPATH_MAIN_CHARACTERISTICS_GENERAL = '/html/body/app-root/div/app-landing/kdl-layout-main/main/app-main-grid/div[1]/div/div[3]/aui-features[2]/section/aui-accordion/aui-accordion-group[1]//text()'
XPATH_MAIN_CHARACTERISTICS_OUTSIDE = '/html/body/app-root/div/app-landing/kdl-layout-main/main/app-main-grid/div[1]/div/div[3]/aui-features[2]/section/aui-accordion//aui-accordion-group[2]/text()'
XPATH_MAIN_CHARACTERISTICS_EQUIPMENT_COMFORT = '/html/body/app-root/div/app-landing/kdl-layout-main/main/app-main-grid/div[1]/div/div[3]/aui-features[2]/section/aui-accordion/aui-accordion-group[3]//text()'
XPATH_MAIN_CHARACTERISTICS_SECURITY = '/html/body/app-root/div/app-landing/kdl-layout-main/main/app-main-grid/div[1]/div/div[3]/aui-features[2]/section/aui-accordion/aui-accordion-group[4]//text()'
XPATH_MAIN_CHARACTERISTICS_INTERIOR = '/html/body/app-root/div/app-landing/kdl-layout-main/main/app-main-grid/div[1]/div/div[3]/aui-features[2]/section/aui-accordion/aui-accordion-group[5]//text()'
XPATH_MAIN_CHARACTERISTICS_ENTERTAINMENT = '/html/body/app-root/div/app-landing/kdl-layout-main/main/app-main-grid/div[1]/div/div[3]/aui-features[2]/section/aui-accordion/aui-accordion-group[6]//text()'

# Imperfections
XPATH_IMPERFECTIONS = '/html/body/app-root/div/app-landing/kdl-layout-main/main/app-main-grid/div[2]/app-dimples/section/div/div[1]/div/app-dimple/div/div//text()'


# Pass the options to the WebDriver
with webdriver.Chrome(service=s, options=chrome_options) as driver:
    
    driver.get(url)
    # texto_1=driver.find_element(By.XPATH,XPATH_NAME)
    # print(texto_1.text)
    # print(texto_1)

    # Get the HTML content of the webpage
    html_content = driver.page_source

    # Process the HTML content using lxml.html
    tree = html.fromstring(html_content)
    print(tree)
    # time.sleep(10)
    parse_link(tree)
    
