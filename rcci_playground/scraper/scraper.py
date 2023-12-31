from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

def get_price(driver : webdriver.Chrome) -> str:
    driver.get('https://www.royalcaribbean.com/cruises?search=ship:SY|startDate:2024-12-01~2024-12-31&itineraryPanel=SY07MIA-3946943081')
    balcony_element = WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, '//li[@aria-labelledby="Balcony"]')))
    balcony_element.click()
    date_element = WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, '//p[text()="Sun, Dec 22, 2024"]')))
    quote_element = date_element.find_element(By.XPATH, '../..')
    return quote_element.find_element(By.XPATH, './div[2]/span/p').text

def scrape() -> str:
    print('scraper')
    driver = webdriver.Chrome()
    price = get_price(driver=driver)
    print('found price: ' + price)
    return float(price.replace('$', '').replace(',', ''))