import time
from selenium import webdriver

driver = webdriver.Chrome('./chromedriver.exe')  # Optional argument, if not specified will search path.
driver.get('http://www.google.com/');
# time.sleep(5) # Let the user actually see something!
search_box1 = driver.find_element_by_name('q')
search_box1.send_keys('Arroz')
search_box1.submit()
time.sleep(5) # Let the user actually see something!
search_box2 = driver.find_element_by_name('q')
search_box2.clear()
search_box2.send_keys('Feijão')
search_box2.submit()
time.sleep(5)
search_box3 = driver.find_element_by_name('q')
search_box3.clear()
search_box3.send_keys('Pimenta')
search_box3.submit()
time.sleep(5)
driver.quit()