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
		heise_url = "https://www.heise.de/thema/https?seite=" + str(i)
		# ueberschriften extrahieren
		content = getPage(heise_url).find("div", { "id" : "mitte_uebersicht" })
		content = content.find("nav")
		content = content.findAll('a', href=True)
		
		for c in content:
			# wortliste fuellen
			c = re.findall("\w+(?=-)" ,c['href'])
			c = [x.lower() for x in c]
			wortliste.extend(c)
	
	
	#woerter zaehlen 
	counter=collections.Counter(wortliste)
	#anzahl ausgeben
	print(counter)
	
	print("\nDONE !\n\n\nHeise.com was scraped.\n")



# main program

if __name__ == '__main__':
    main()
