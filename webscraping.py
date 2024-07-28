import requests 
from bs4 import BeautifulSoup

f = open("paragraphdata.txt","w+")
g = open("anchordata.txt","w+")
h = open("imagedata.txt","w+")

# link = input("Please enter the link of thewebsite you want to scrape- ")    
req = requests.get("https://en.wikipedia.org/wiki/Mughal_Empire")

soup = BeautifulSoup(req.content, "html.parser")

paragraph = soup.find_all('p')


for i in paragraph:     #TO EXTRACT PARAGRAPH DATA FROM THE WEBSITE AND STORE IT IN PARAGRAPHDATA.TXT
    f.write(i.get_text())
    f.write("\n")

for i in paragraph:     #TO EXTRACT ALL THE ANCHOR TAGS LINKS AND DATA FROM THE PARAGRAPHS AND STORE IT IN ANCHORDATA.TXT
    anchor = i.find_all("a")

    for link in anchor:
        g.write(link.get('href'))
        g.write("\n")
        g.write(link.get_text())
        g.write("\n")
        g.write("\n")
        g.write("\n")


images = soup.find_all("img")   #TO EXTRACT ALL THE IMAGE LINKS AND STORE IT IN IMAGEDATA.TXT
for i in images:
    h.write(i.get("src"))
    h.write("\n")
    h.write("\n")




f.close()
g.close()
h.close()


