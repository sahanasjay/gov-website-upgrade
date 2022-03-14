# Government website upgrade: final submission

Our government website upgrade attempt consisted of two major parts: Scraping/acquiring the data and finding a way to present it. I began by inspecting the Maryland Health Department’s page on overdoes deaths; I found that links to both annual and quarterly pdf reports were contained in html table tags. Our first web scraper dealt with tables, so I cribbed some code from there, using the requests and BeautifulSoup libraries to visit a url and find the tbody, tr and td tags containing the links. Each link was missing its first half — just like those in our first web scraper — so I appended them as I added the links to a list. I functionized the link-getting code so I could grab both years and quarters easily. Next came a decision: Should I download the pdfs, transform them and then parse them, or find a way to parse them without writing them onto my machine? I toyed with some code to just lay out the pdfs as text without writing them as files on my machine, but it messed with the formatting and I wasn’t sure how to parse them without actually having them (I’d love to learn how, though, or talk about whether that might be a better approach, especially for larger numbers of pdfs). I wrote a function to download each pdf and write it to a specified subdirectory. I revisited this code and tried to the pdfs before I wrote them out — I was only interested in the pages after the one that said “TABLES.” I looked at PyPDF, PDFMiner and tabula-py, but the results I got weren’t great. Instead, I manually went thought the yearly pdfs and found the page numbers where the tables began. Then, I used xpdf command line tool pdftotext, with -layout and -f flags to preserve tabular format and specify page number. I ended up with 8 .txt files, each containing several labeled tables …. but the formatting was still messed up. Some numbers weren’t in the right columns, and there were dots everywhere. The end goal would have been to get that data into an even, comma-separated format. I’d like to know how to write a parser that might let me do that. All my code is in [scrape.py](https://github.com/sahanasjay/gov-website-upgrade/blob/main/scrape.py) 

In the meantime, lacking the data to deploy a tableau application, Mary drew up [sketches](https://drive.google.com/file/d/1_Wdc3wGzyzUlM3Ulp-5qYpE1g4inXbfK/view?usp=sharing) and a [final wireframes](https://docs.google.com/drawings/d/1kN-aSRtbGq-c-W8HtOdph-LQ8vePJlvv7lqCKRFVyvo/edit?usp=sharing) of what our application might look like. We took elements of the Washington Post’s DEA news app, creating dropdowns for users to select the Maryland county they’re interested in, as well as the drug (prescription opioid, heroin, fentanyl etc.) and demographics breakdowns (by age, race, sex, etc.). We thought adding the demographics button would let users see an extra layer of nuance, but weren’t sure whether it would muddle the usefulness of the dropdown — would love thoughts. Opioid entries would be accompanied by naloxone distribution information. Interactive choropleth maps accompanied would put counties in context next to one another, and Maryland in the context of the country.  An interactive line graph would let users more clearly see individual county trends with year-over-year changes, showing data from 2020 compared to 2021.
