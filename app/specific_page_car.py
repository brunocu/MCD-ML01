import scrapper_utils as scrapper_utils
# Path to Chromium bin
chromium_path =  "app/drivers/chrome-linux64/chrome"
service_path = "app/drivers/chromedriver-linux64/chromedriver"

url = "https://www.kavak.com/mx/usado/honda-city-15_ex-sedan-2017"

XPATH = {
    # General information
    'XPATH_NAME' : '/html/body/app-root/div/app-landing/kdl-layout-main/main/app-main-grid/div[1]/div/div[2]/app-buy-box/section/div[1]/div[1]/h1',
    'XPATH_KM_CITY' : '/html/body/app-root/div/app-landing/kdl-layout-main/main/app-main-grid/div[1]/div/div[2]/app-buy-box/section/div[1]/div[1]/p',

    # Price
    'XPATH_PRICE' : '/html/body/app-root/div/app-landing/kdl-layout-main/main/app-main-grid/div[1]/div/div[2]/app-buy-box/section/aui-price-product/div/div/div[2]/span[2]',
    'XPATH_PRICE_MONTH' : '/html/body/app-root/div/app-landing/kdl-layout-main/main/app-main-grid/div[1]/div/div[2]/app-buy-box/section/aui-price-product/div/div/div[3]/span',

    # Spects
    'XPATH_YEAR' : '/html/body/app-root/div/app-landing/kdl-layout-main/main/app-main-grid/div[1]/div/div[2]/app-buy-box/section/app-filters/aui-accordion/div[1]/aui-accordion-group/div/h3/div/div[1]/div[2]',
    'XPATH_MODEL' : '/html/body/app-root/div/app-landing/kdl-layout-main/main/app-main-grid/div[1]/div/div[2]/app-buy-box/section/app-filters/aui-accordion/div[2]/aui-accordion-group/div/h3/div/div[1]/div[2]',
    'XPATH_COMPLEMENTS' : '//html/body/app-root/div/app-landing/kdl-layout-main/main/app-main-grid/div[1]/div/div[2]//aside',
    # XPATH_COMPLEMENTS : '/html/body/app-root/div/app-landing/kdl-layout-main/main/app-main-grid/div[1]/div/div[3]/app-highlights/section/aui-carousel/div/div[2]/div/div',

    'XPATH_GENERAL_DESCRIPTIONS' : '/html/body/app-root/div/app-landing/kdl-layout-main/main/app-main-grid/div[1]/div/div[3]/aui-features[1]/section',

    # Special equipment
    'XPATH_SPECIAL_EQUIPMENT' : '/html/body/app-root/div/app-landing/kdl-layout-main/main/app-main-grid/div[1]/div/div[3]/app-highlights/',

    # Main Charecteristic
    'XPATH_CLOSE' : '/html/body/app-root/div/app-landing/kdl-layout-main/main/app-main-grid/div[1]/div/div[2]/ahl-modal-auth/aui-drawer/div/div[2]/div[1]/aui-svg[2]',
    'XPATH_COOKIES' : '//*[@id="onetrust-accept-btn-handler"]',

    # /html/body/app-root/div/app-landing/kdl-layout-main/main/app-main-grid/div[1]/div/div[3]/aui-features[2]/section/aui-accordion/aui-accordion-group[1]/div/h3/div/div/div
    'XPATH_MAIN_CHARACTERISTICS_GENERAL' : '/html/body/app-root/div/app-landing/kdl-layout-main/main/app-main-grid/div[1]/div/div[3]/aui-features[2]/section/aui-accordion/aui-accordion-group[1]/div/h3/div/div/div',
    'XPATH_MAIN_CHARACTERISTICS_GENERAL' : '/html/body/app-root/div/app-landing/kdl-layout-main/main/app-main-grid/div[1]/div/div[3]/aui-features[2]/section/aui-accordion/aui-accordion-group[1]',
    'XPATH_MAIN_CHARACTERISTICS_OUTSIDE' : '/html/body/app-root/div/app-landing/kdl-layout-main/main/app-main-grid/div[1]/div/div[3]/aui-features[2]/section/aui-accordion//aui-accordion-group[2]',
    'XPATH_MAIN_CHARACTERISTICS_EQUIPMENT_COMFORT' : '/html/body/app-root/div/app-landing/kdl-layout-main/main/app-main-grid/div[1]/div/div[3]/aui-features[2]/section/aui-accordion/aui-accordion-group[3]',
    'XPATH_MAIN_CHARACTERISTICS_SECURITY' : '/html/body/app-root/div/app-landing/kdl-layout-main/main/app-main-grid/div[1]/div/div[3]/aui-features[2]/section/aui-accordion/aui-accordion-group[4]',
    'XPATH_MAIN_CHARACTERISTICS_INTERIOR' : '/html/body/app-root/div/app-landing/kdl-layout-main/main/app-main-grid/div[1]/div/div[3]/aui-features[2]/section/aui-accordion/aui-accordion-group[5]',
    'XPATH_MAIN_CHARACTERISTICS_ENTERTAINMENT' : '/html/body/app-root/div/app-landing/kdl-layout-main/main/app-main-grid/div[1]/div/div[3]/aui-features[2]/section/aui-accordion/aui-accordion-group[6]'

    # Imperfections
    # XPATH_IMPERFECTIONS = '/html/body/app-root/div/app-landing/kdl-layout-main/main/app-main-grid/div[2]/app-dimples/section/div/div[1]/div/app-dimple/div/div/'
}

json_parsed = scrapper_utils.get_car_info(chromium_path, service_path, XPATH, url)
print(f'Creando documento {json_parsed["general_descriptions"]["Stock ID"]} json')
scrapper_utils.create_json_file(json_parsed, './car_files/{}'.format(json_parsed["general_descriptions"]["Stock ID"]))