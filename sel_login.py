from selenium import webdriver
# import requests

def selenium_import():
    driver = webdriver.Chrome()
    driver.get("https://fashion-studio.dicoding.dev/")
    return driver
    
