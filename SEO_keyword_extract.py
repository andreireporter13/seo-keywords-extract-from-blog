# New scraper idea - scrape keywords from blogs;
#
# Author: Andrei C. Cojocaru
# Github: https://github.com/andreireporter13
# LinkedIn: https://www.linkedin.com/in/andrei-cojocaru-985932204/
# Twitter: https://twitter.com/andrei_reporter
# Website: https://ideisioferte.ro && https://webautomation.ro
# date_time - 27.06.2022
#
#
import requests
#
from bs4 import BeautifulSoup
#
from rake_nltk import Rake
#
from fake_useragent import UserAgent
#
#
# -----------------------------------------------------> Logic of code <-------------------------------------------------------------
#
#
def set_headers():

    """ 
    This function is about setting headers for new_requests. Is import step to scraping!
    """
    user_agent = UserAgent() # after set a random fake_useragent;

    HEADERS = {
        'User-Agent': user_agent.random,
        'Accept-Language': 'en-US,en;q=0.5',
        'Refer': 'https://google.com',
        'DNT': '1'
    }

    return HEADERS


def extract_text():
    """ 
        This function return a text from link of blog!
    """ 

    link = 'http://lauracaltea.ro/articlesite/medici-si-sarlatani-in-cautarea-hormonului-pierdut-despre-excitat-de-randi-hutter-epstein'

    response = requests.get(link, headers=set_headers())
    soup = BeautifulSoup(response.content.decode('utf-8'), 'lxml')

    h_1 = soup.find('div', class_='main-article').find('h1').text
    p_elements = soup.find('div', class_='main-article').find_all('p')

    # extract all text from p_elements;
    new_text = ''
    for new_p in p_elements:
        new_text += new_p.text + '\n'

    concat_text = h_1 + '\n' + new_text

    return concat_text


# extract keyword from scraped text;
r = Rake()
r.extract_keywords_from_text(extract_text())

for rating, keywords in r.get_ranked_phrases_with_scores():
    if rating > 10:
        print(rating, keywords)