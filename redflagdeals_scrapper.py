from bs4 import BeautifulSoup
import csv
import requests


try:
    response=requests.get('https://www.redflagdeals.com/in/ottawa/deals/?search_type=latest').text
except Exception:
    print("Sorry! Couldn't connect to redflagdeals.com")

redflagdeals_data=BeautifulSoup(response,'lxml')

redflagdeals_csv=open('redflagdeals.csv', 'w')
writer_csv=csv.writer(redflagdeals_csv)
writer_csv.writerow(['Store Name','Deal'])


for deal in redflagdeals_data.find_all('div',class_='list_item'):
    try:
        Store_Name = deal.p.a.text
        print(Store_Name)

        Deal = deal.h2.a.text
        print(Deal)

        print()
        writer_csv.writerow([Store_Name, Deal])
    except Exception:
        writer_csv.writerow([None, None])



redflagdeals_csv.close()

