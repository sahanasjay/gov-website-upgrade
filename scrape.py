import requests
from bs4 import BeautifulSoup

# set url equal to a variable
url = "https://health.maryland.gov/vsa/Pages/overdose.aspx"

# get the url
response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})

# get the content from the html response
html = response.content

# parse the html content you grabbed page
soup = BeautifulSoup(html, features="html.parser")

# set counter equal to zero
counter = 0

for cell in row.find_all('td'):
    for link in cell.find_all('a'):
        if('.pdf' in link.get('href', [])):
            counter+=1
            print("Downloading file:", counter)

            # get response object for link
            response = requests.get(link.get('href'))


            # write content into a pdf file
            pdf = open("pdf"/"pdf"+str(counter)+".pdf", 'wb'

# find all tables on the page
tables = soup.find_all("tbody")
annual_table = tables[0]
