# imports
from bs4 import BeautifulSoup
import requests
import csv
import re
import collections

# this function returns a soup page object
def getPage(url):
    r = requests.get(url)
    data = r.text
    spobj = BeautifulSoup(data, "lxml")
    return spobj

	
# scraper website: greyhound-data.com
def main():

	wortliste = []
	for i in range(0,4,1):
		fobj = open('heise-data.csv', 'w')
		csvw = csv.writer(fobj, delimiter = ';')      
		heise_url = "https://www.heise.de/thema/https?seite=" + str(i)
		content = getPage(heise_url).find("div", { "id" : "mitte_uebersicht" })
		content = content.find("nav")
		content = content.findAll('a', href=True)
		
		for c in content:
			c = re.findall("\w+(?=-)" ,c['href'])
			c = [x.lower() for x in c]
			wortliste.extend(c)

	fobj.close()                                # close file
	
	
	counter=collections.Counter(wortliste)
	
	print(counter)
	
	print("\nDONE !\n\n\nHeise.com was scraped.\n")



# main program

if __name__ == '__main__':
    main()