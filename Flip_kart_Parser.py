from bs4 import BeautifulSoup
import pandas as pd
import os

data_list=[]

base_dir = os.path.join(os.getcwd(), "Scrape_Data")

files = os.listdir(base_dir)

for file in files:
    file_path = os.path.join(base_dir, file)
    with open(file_path, 'r', encoding='utf-8') as f:
          d=f.read()
    soup=BeautifulSoup(d,'html.parser')
    price_tag = soup.find('div', class_="hZ3P6w DeU9vF")

    data_dic = {
        'name': soup.find('div', class_="RG5Slk").text if soup.find('div', class_="RG5Slk") else "N/A",
        'price': price_tag.text if price_tag else "N/A"
   }
    data_list.append(data_dic)
data=pd.DataFrame(data_list)

print(data)

csv_path = os.path.join(os.getcwd(), "output.csv")
data.to_csv(csv_path, index=False, encoding='utf-8')

print("Save in csv succesfully")


