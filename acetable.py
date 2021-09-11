from bs4 import BeautifulSoup
import requests
import csv

url=('https://www.npci.org.in/what-we-do/upi/upi-ecosystem-statistics')
r=requests.get(url)
htmlContent=r.content


#print(htmlcontent)

soup=BeautifulSoup(htmlContent,'html.parser')
#print(soup.prettify())

april21 = soup.find('div' , class_='tab-content')
#print(april21.text)

may21=soup.find('div' , id='innerTabThreeMay21')
#print(may21.text)

june21=soup.find('div' , id='innerTabThreeJun21')
#print(june21.text)

july21=soup.find('div' , id='innerTabThreeJul21')
#print(july21.text)

feb21=soup.find('div',id='yearFeb2021')
#print(feb21.text)

jan21=soup.find('div',id='yearJan2021')
#print(jan21.text)

dec20=soup.find('div',id='yearDec2020')
#print(dec20.text)

Nov20=soup.find('div',id='yearNov2020')
#print(Nov20.text)

Oct20=soup.find('div',id='yearOct2020')
#print(Oct20.text)

Sep20=soup.find('div',id='yearSept2020')
#print(Sep20.text)

Aug20=soup.find('div',id='yearAug2020')
#print(Aug20.text)

July20=soup.find('div',id='yearJul2020')
#print(July20.text)

title=soup.find('th').strong
#print(title.text)



