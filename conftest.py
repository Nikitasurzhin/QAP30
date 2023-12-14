from selenium import webdriver
import pytest


@pytest.fixture(autouse=True)
def set():
   driver = webdriver.Chrome('C:\chromedriver-win64\chromedriver-win64')
   driver.get('http://petfriends.skillfactory.ru/login')

   yield

   driver.quit()