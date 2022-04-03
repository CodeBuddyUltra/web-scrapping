import requests
from bs4 import BeautifulSoup
import random

number = random.randint(0,174)
# This gives a random fact effect, I entered the last number as 174 as there are 175 facts in the website

r = requests.get("https://bestlifeonline.com/random-fun-facts/")
c = r.content
# Reading the contents

soup = BeautifulSoup(c, "html.parser")
#Specifying the parser
all =soup.find_all("div", {"class":"title"})
#Specifying what I want to scrap
splice = all[number]
#Gives the fact of a random number
print(splice.text)



#Magic!
