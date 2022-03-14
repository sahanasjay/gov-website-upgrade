import os
import requests
import urllib
import tabula
from bs4 import BeautifulSoup
#from xpdf_python import to_text

# set url equal to a variable
url = "https://health.maryland.gov/vsa/Pages/overdose.aspx"
path_year = '/Users/sahanajayaraman/Desktop/JOUR328O/gov-website-upgrade/pdf_year'
path_quarter = '/Users/sahanajayaraman/Desktop/JOUR328O/gov-website-upgrade/pdf_quarter'
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
list_of_years = []
list_of_quarters = []

### GOING TO FUNCTIONIZE THIS###
def get_pdf(list, table):
    for row in table.find_all('tr'):
        for cell in row.find_all('td'):
            if cell.find('a'):
                list.append("https://health.maryland.gov" + cell.find('a')['href'])
    print(list)

get_pdf(list_of_years, annual_table)
get_pdf(list_of_quarters, quarterly_table)


#tabula.convert_into_by_batch("pdf_year", output_format="csv", pages="all")
def download_pdf(list,path):
    counter = 0
    for i in list:
        counter+=1
        response = urllib.request.urlopen(i)
        print(response)
        file = open(os.path.join(path, str(counter) + ".pdf"), 'wb')
        file.write(response.read())
        file.close()

download_pdf(list_of_years, path_year)
download_pdf(list_of_quarters, path_quarter)


# convert all tables of a PDF file into a single CSV file
# supported output_formats are "csv", "json" or "tsv"
# convert all PDFs in a folder into CSV format
# `pdfs` folder should exist in the current directory

#pdf_location = '/Users/sahanajayaraman/Desktop/JOUR328O/gov-website-upgrade/3.pdf'
#text = to_text(pdf_location)
#print(text) # this is better done with
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
