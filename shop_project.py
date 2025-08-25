import requests
import pandas as pd
from bs4 import BeautifulSoup
from sel_login import selenium_import


datas = []
for i in range(1,51):
    if i == 1:
        url = "https://fashion-studio.dicoding.dev/"
    else:
        url = f"https://fashion-studio.dicoding.dev/page{i}"

    try:
        driver = selenium_import()
        print(url, 'using selenium')
        driver.get(url)
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        elements = soup.find_all("div", class_="collection-card")   
        for element in elements:
            title = element.find("h3", class_="product-title")
            price = element.find("span", class_="price")
            if price is None:
                price = ""
            else:
                price = price.text
            collection = element.find_all("p")
            rating = collection[0]
            colors = collection[1]
            size = collection[2]
            gender = collection[3]
            desc = {
                "product_name": title.text,
                "price": price, 
                "rating": rating.text.replace("Rating: ⭐ ", ""),
                "color": colors.text.strip(' Colors'),
                "size": size.text.strip('Size: '),
            }
        driver.quit()
    except Exception as e:
        e = requests.get(url)
        soup = BeautifulSoup(e.text, 'html.parser')
        elements = soup.find_all("div", class_="collection-card")
        for element in elements:
            title = element.find("h3", class_="product-title")
            price = element.find("span", class_="price")
            if price is None:
                price = ""
            else:
                price = price.text
            collection = element.find_all("p")
            rating = collection[0]
            colors = collection[1]
            size = collection[2]
            gender = collection[3]

            desc = {
                "product_name": title.text,
                "price": price, 
                "rating": rating.text.replace("Rating: ⭐ ", ""),
                "color": colors.text.strip(' Colors'),
                "size": size.text.strip('Size: '),
                "gender":gender.text.replace('Gender: ', "")
            }
            print(desc)
            datas.append(desc)
        print(len(datas), "products found on page", i)
    convert = pd.DataFrame(datas)
    convert.to_excel("shop2.xlsx", index=False)
print (datas)