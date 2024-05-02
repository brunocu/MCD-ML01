import selenium
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

#iniciar con el url
url='https://en.wikipedia.org/wiki/Main_Page'
path_driver=os.chdir('Drivers/chromedriver-linux64')
#objeto driver
# driver=webdriver.Chrome(executable_path='webdriver')

driver=webdriver.Chrome()
#obtener un url con driver
driver.maximize_window()
print(url)

driver.get('https://en.wikipedia.org/wiki/Main_Page')
#obtner texto women
# texto_1=driver.find_element(By.XPATH,'//nav/ol/li/a[contains(text(),"Wo")]')
#print(texto_1.text)


#textos_2=driver.find_elements(By.XPATH,'//nav/ol/li/a')
#for i in textos_2:
#    print(i.text)
# cuenta=driver.find_element(By.XPATH,'//span[contains(text(), "Account")]')
# cuenta.click()
# register=driver.find_element(By.XPATH, '//li/a[@title="Register"]')
# register.click()
# #rellenar formulario
# first_name=driver.find_element(By.XPATH,'//input[@id="firstname"]')
# first_name.send_keys('fernando')

# midle_name=driver.find_element(By.XPATH,'//input[@id="middlename"]')
# midle_name.send_keys('pullutasig')

# last_name=driver.find_element(By.XPATH,'//input[@id="lastname"]')
# last_name.send_keys('pullutasig')

# email=driver.find_element(By.XPATH,'//input[@id="email_address"]')
# email.send_keys('ejemplo@correo.com.ec')

# password=driver.find_element(By.XPATH,'//input[@id="password"]')
# password.send_keys('abc123')

# password_confir=driver.find_element(By.XPATH,'//input[@id="confirmation"]')
# password_confir.send_keys('abc123')

# check_input=driver.find_element(By.XPATH, '//input[@type="checkbox"]')
# check_input.click()

# registro=driver.find_element(By.XPATH,'//button[@title="Register"]')
# registro.click()

time.sleep(10)