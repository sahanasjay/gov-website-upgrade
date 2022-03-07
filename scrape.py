import requests
import urllib
from bs4 import BeautifulSoup
from xpdf_python import to_text

# set url equal to a variable
url = "https://health.maryland.gov/vsa/Pages/overdose.aspx"

# get the url
response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})

# get the content from the html response
html = response.content

# parse the html content you grabbed page
soup = BeautifulSoup(html, features="html.parser")

tables = soup.find_all("tbody")
annual_table = tables[0]
quarterly_table = tables[1]
#print(annual_table)
#print(quarterly_table)


#list_of_years = []
list_of_years = []
for row in annual_table.find_all('tr'):
    for cell in row.find_all('td'):
        if cell.find('a'):
            list_of_years.append("https://health.maryland.gov" + cell.find('a')['href'])
print(list_of_years)

list_of_quarters = []
for row in quarterly_table.find_all('tr'):
    for cell in row.find_all('td'):
        if cell.find('a'):
            list_of_quarters.append("https://health.maryland.gov" + cell.find('a')['href'])
print(list_of_quarters)

#set counter equal to zero

#def download_pdf(list):
    #counter = 0
    #for i in list:
        #counter+=1
        #response = urllib.request.urlopen(i)
        #file = open(str(counter) + ".pdf", 'wb')
        #file.write(response.read())
        #file.close()

#download_pdf(list_of_years)

pdf_location = '/Users/sahanajayaraman/Desktop/JOUR328O/gov-website-upgrade/3.pdf'
text = to_text(pdf_location)
print(text)
#response = requests.get(link.get("https://health.maryland.gov/vsa/Documents/Overdose/Annual_2020_Drug_Intox_Report.pdf"))
#print(response)
#def download_pdf(list):
#for link in list_of_years:
    #counter+=1
    #print("Downloading file:", counter)
    #response = requests.get(link.get())
    #print(response)
    #pdf = open("pdf"/"pdf"+str(counter)+".pdf", 'wb'


#download_pdf(list_of_years)
#for link in
        #if('.pdf' in link.get('href', [])):
            #counter+=1
            #print("Downloading file:", counter)
            # get response object for link
            #response = requests.get(link.get('href'))

            # write content into a pdf file
            #pdf = open("pdf"/"pdf"+str(counter)+".pdf", 'wb'

# find all tables on the page
#tables = soup.find_all("tbody")
#annual_table = tables[0]
#print(annual_table)
