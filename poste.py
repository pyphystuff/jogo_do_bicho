import requests
from bs4 import BeautifulSoup
import datetime
URL = "https://www.ojogodobicho.com/deu_no_poste.htm"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
#print(page.text)

#td_elements = soup.find_all("td", class_="yescx")
#td_elements = soup.find_all("td", class_=["yescx", "yligx","yesc"])
td_elements = soup.find_all("td", class_=["ylig","yesc"])
th_elements = soup.find_all("th", class_=["ylig","yesc"])



#print(td_elements)
th_texts = [th.text.strip() for th in th_elements] #headers
#print(th_texts)

# Convert to text and strip
td_texts = [td.text.strip() for td in td_elements]  #clean the text

# Set the number of columns per row (adjust based on your data)
cols_per_row = 5
#print data:
x = datetime.datetime.now()
print("Resultados para o dia de hoje/Results for today ",x)

#header
print("\t".join(th_texts))
# Print as a table
for i in range(0, len(td_texts), cols_per_row):
    row = td_texts[i:i+cols_per_row]
    print("\t".join(row))  # Tab-separated columns

print("Resultados extraidos de: https://www.ojogodobicho.com/deu_no_poste.htm")

