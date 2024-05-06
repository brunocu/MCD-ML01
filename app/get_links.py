import scrapper_utils as scrapper_utils
import time
# Path to Chromium bin
chromium_path =  "app/drivers/chrome-linux64/chrome"
service_path = "app/drivers/chromedriver-linux64/chromedriver"
HOME_URL = 'https://www.kavak.com/mx/seminuevos?page={}'
begin_page = 30
max_pages = 35
# max_pages = 203
XPATH = {
    # 'XPATH_LINK_TO_CARS' : '/html/body/app-root/div/app-landing/aui-layout-main/main/asw-widget-main/div/div[2]/asw-widget-grid/div/div[5]/@href',
    # 'XPATH_LINK_TO_CARS' : '//a[contains(@href,"https://www.kavak.com/mx/usado/")',
    'XPATH_LINK_TO_CARS' : '//a[@class="card-product"]',
    'XPATH_CLOSE' : '/html/body/app-root/div/app-landing/kdl-layout-main/main/app-main-grid/div[1]/div/div[2]/ahl-modal-auth/aui-drawer/div/div[2]/div[1]/aui-svg[2]',
    'XPATH_COOKIES' : '//*[@id="onetrust-accept-btn-handler"]',
    'XPATH_END' : '/html/body/app-root/div/app-landing/aui-layout-main/main/asw-widget-main/section'
}

for page in range(begin_page,max_pages):
    url_completo = HOME_URL.format(page)
    car_links = scrapper_utils.get_car_links(chromium_path, service_path, XPATH, url_completo)
    print("Scraping page {}".format(page))
    scrapper_utils.create_json_file(car_links, "app/links/page_{}".format(page))
    time.sleep(30)