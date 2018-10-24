#
#   First Web Scrape attempt following:-
#   https://medium.freecodecamp.org/how-to-scrape-websites-with-python-and-beautifulsoup-5946935d93fe
#   From FreeCodeCamp
#   Aim: To scrape stats for Tottenham Hotspurs
# 
# 
# 

# Step 1 - Import the necessary Libraries
import urllib2
from bs4 import BeautifulSoup

# Step 2 - Create the variables - quote_page 
quote_page = ‘https://www.tottenhamhotspur.com/matches/first-team/201819/brighton-hove-albion-v-spurs/'

# Page will have the html site returned to it
page = urllib2.urlopen(quote_page)

#parse the website into the variable soup
soup = BeautifulSoup(page, ‘html.parser’)

#Now that it is in the soup variable, parsed we look for the information. Here we are using the Class name to id the data
player_passes = soup.find('li', attrs={'class':'Opta-on'})
name = player_passes.text.strip()

print name