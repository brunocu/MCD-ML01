import scrapper_utils as scrapper_utils
import time
# Path to Chromium bin
chromium_path =  "/home/thinkpad/Documents/MCD/MachineLearning_01/Scrapper/Drivers/chrome-linux64/chrome" #"Drivers/chrome-linux64/chrome" 
service_path = "/home/thinkpad/Documents/MCD/MachineLearning_01/Scrapper/chromedriver-linux64/chromedriver"
HOME_URL = 'https://www.kavak.com/mx/seminuevos?page={}'
max_pages = 1
# max_pages = 203
XPATH = {
    # 'XPATH_LINK_TO_CARS' : '/html/body/app-root/div/app-landing/aui-layout-main/main/asw-widget-main/div/div[2]/asw-widget-grid/div/div[5]/@href',
    # 'XPATH_LINK_TO_CARS' : '//a[contains(@href,"https://www.kavak.com/mx/usado/")',
    'XPATH_LINK_TO_CARS' : '//a[@class="card-product"]',
    'XPATH_CLOSE' : '/html/body/app-root/div/app-landing/kdl-layout-main/main/app-main-grid/div[1]/div/div[2]/ahl-modal-auth/aui-drawer/div/div[2]/div[1]/aui-svg[2]',
    'XPATH_COOKIES' : '//*[@id="onetrust-accept-btn-handler"]'}

for page in range(0,max_pages):
    url_completo = HOME_URL.format(page)
    car_links = scrapper_utils.get_car_links(chromium_path, service_path, XPATH, url_completo)
    scrapper_utils.create_json_file(car_links, "app/page_{}".format(page))