import utils
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait       
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import lxml.html as html


# Path to Chromium bin
chromium_path =  "/home/thinkpad/Documents/MCD/MachineLearning_01/Scrapper/Drivers/chrome-linux64/chrome" #"Drivers/chrome-linux64/chrome" 

# Set up Chrome options
chrome_options = Options()
chrome_options.binary_location = chromium_path

url = "https://www.kavak.com/mx/usado/kia-soul-20_ex_ivt_auto-suv-2021"
s = Service("/home/thinkpad/Documents/MCD/MachineLearning_01/Scrapper/chromedriver-linux64/chromedriver")

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
XPATH_COOKIES = '//*[@id="onetrust-accept-btn-handler"]'

XPATH_MAIN_CHARACTERISTICS_GENERAL = '/html/body/app-root/div/app-landing/kdl-layout-main/main/app-main-grid/div[1]/div/div[3]/aui-features[2]/section/aui-accordion/aui-accordion-group[1]'
XPATH_MAIN_CHARACTERISTICS_OUTSIDE = '/html/body/app-root/div/app-landing/kdl-layout-main/main/app-main-grid/div[1]/div/div[3]/aui-features[2]/section/aui-accordion//aui-accordion-group[2]'
XPATH_MAIN_CHARACTERISTICS_EQUIPMENT_COMFORT = '/html/body/app-root/div/app-landing/kdl-layout-main/main/app-main-grid/div[1]/div/div[3]/aui-features[2]/section/aui-accordion/aui-accordion-group[3]'
XPATH_MAIN_CHARACTERISTICS_SECURITY = '/html/body/app-root/div/app-landing/kdl-layout-main/main/app-main-grid/div[1]/div/div[3]/aui-features[2]/section/aui-accordion/aui-accordion-group[4]'
XPATH_MAIN_CHARACTERISTICS_INTERIOR = '/html/body/app-root/div/app-landing/kdl-layout-main/main/app-main-grid/div[1]/div/div[3]/aui-features[2]/section/aui-accordion/aui-accordion-group[5]'
XPATH_MAIN_CHARACTERISTICS_ENTERTAINMENT = '/html/body/app-root/div/app-landing/kdl-layout-main/main/app-main-grid/div[1]/div/div[3]/aui-features[2]/section/aui-accordion/aui-accordion-group[6]'

# Imperfections
# XPATH_IMPERFECTIONS = '/html/body/app-root/div/app-landing/kdl-layout-main/main/app-main-grid/div[2]/app-dimples/section/div/div[1]/div/app-dimple/div/div/'

# Pass the options to the WebDriver
with webdriver.Chrome(service=s, options=chrome_options) as driver:
    driver.get(url)
    driver.maximize_window()
    utils.close_cookies(driver, XPATH_COOKIES)

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
    json_parsed['general_descriptions'] = utils.parse_arr(utils.string_to_array(driver.find_element(By.XPATH,XPATH_GENERAL_DESCRIPTIONS).text))['attributes']

    # Special equipment
    # json_parsed['special_equipment'] = parse_arr(driver.find_element(By.XPATH,XPATH_SPECIAL_EQUIPMENT).text)

    # Main Charecteristic
    json_parsed['main_characteristics'] = {}

    utils.open_menu(driver, XPATH_MAIN_CHARACTERISTICS_GENERAL, 'General', XPATH_CLOSE)
    json_parsed['main_characteristics']['general'] = utils.parse_arr(utils.string_to_array(driver.find_element(By.XPATH,XPATH_MAIN_CHARACTERISTICS_GENERAL).text))['attributes']

    utils.open_menu(driver,XPATH_MAIN_CHARACTERISTICS_OUTSIDE, 'Outside', XPATH_CLOSE)
    json_parsed['main_characteristics']['outside'] = utils.parse_arr(utils.string_to_array(driver.find_element(By.XPATH,XPATH_MAIN_CHARACTERISTICS_OUTSIDE).text))['attributes']

    utils.open_menu(driver,XPATH_MAIN_CHARACTERISTICS_EQUIPMENT_COMFORT, 'Comfort', XPATH_CLOSE)
    json_parsed['main_characteristics']['equipment_confort'] = utils.parse_arr(utils.string_to_array(driver.find_element(By.XPATH,XPATH_MAIN_CHARACTERISTICS_EQUIPMENT_COMFORT).text))['attributes']

    utils.open_menu(driver,XPATH_MAIN_CHARACTERISTICS_SECURITY, 'Security', XPATH_CLOSE)
    json_parsed['main_characteristics']['security'] = utils.parse_arr(utils.string_to_array(driver.find_element(By.XPATH,XPATH_MAIN_CHARACTERISTICS_SECURITY).text))['attributes']

    utils.open_menu(driver,XPATH_MAIN_CHARACTERISTICS_INTERIOR, 'Interior', XPATH_CLOSE)
    json_parsed['main_characteristics']['interior'] = utils.parse_arr(utils.string_to_array(driver.find_element(By.XPATH,XPATH_MAIN_CHARACTERISTICS_INTERIOR).text))['attributes']

    utils.open_menu(driver,XPATH_MAIN_CHARACTERISTICS_ENTERTAINMENT, 'Entertaiment', XPATH_CLOSE)
    json_parsed['main_characteristics']['entretaiment'] = utils.parse_arr(utils.string_to_array(driver.find_element(By.XPATH,XPATH_MAIN_CHARACTERISTICS_ENTERTAINMENT).text))['attributes']

    # Imperfections
    # json_parsed['imperfections'] = len(parse_arr(driver.find_element(By.XPATH,XPATH_IMPERFECTIONS).text))

    # Stock ID
    print("Creando documento json")
    utils.create_json_file(json_parsed, json_parsed["general_descriptions"]["Stock ID"])
    time.sleep(5)