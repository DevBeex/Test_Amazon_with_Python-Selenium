from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome('C://selenium-java-4.5.3/chromedriver.exe')
#Hacemos la pestaña del navegador mas grande y eliminamos cookies
driver.maximize_window()
driver.delete_all_cookies()

#Comienza la prueba e identificamos los lugares del HTML de interés por ID y clase 
driver.get("https://www.amazon.com/")
driver.find_element(By.ID, "twotabsearchtextbox").send_keys("HP Pavilion azul")
driver.find_element(By.ID, "nav-search-submit-button").click()
driver.find_element(By.CLASS_NAME, "a-price-whole").click()
driver.find_element(By.CLASS_NAME, "a-button-inner").click()
driver.find_element(By.ID, "quantity_1").click()
driver.find_element(By.ID, "add-to-cart-button").click()
driver.find_element(By.CLASS_NAME, "a-button-inner").click()
#Termina la prueba

time.sleep(100)
driver.quit()