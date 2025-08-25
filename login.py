import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

from utils import to_csv

def response():
    """
    ini proses login
    """

    driver = webdriver.Chrome()
    url="https://www.saucedemo.com/"
    driver.get(url)

    un=driver.find_element(By.ID,"user-name")
    pas=driver.find_element(By.ID,"password")

    un.send_keys("standard_user")
    pas.send_keys("secret_sauce")

    login_button= driver.find_element(By.ID, "login-button")
    login_button.click()

    time.sleep(5)

    return driver.page_source

def parser(response):
    products_list = []
    soup = BeautifulSoup(response, "html.parser")

    products = soup.find("div", attrs={"class":"inventory_list"}).find_all('div', attrs={"class":"inventory_item"})
    for product in products:
        title = product.find("div", attrs={"class":"inventory_item_name"}).text
        desc = product.find("div", attrs={"class":"inventory_item_desc"}).text
        price = product.find("div", attrs={"class":"inventory_item_price"}).text

        data_dict = {
            "title": title,
            "desc": desc,
            "price": price
        }

        products_list.append(data_dict)

    return products_list

def main():
    res = response()
    products_list = parser(res)
    to_csv(products_list, "products.csv")

    print("Mencari Data")
    datas = search("title", products_list)
    print(datas)

def search(query, database):
    datas = [data[query] for data in database if query in data]
    return datas

if __name__ == "__main__":
    main()
   
