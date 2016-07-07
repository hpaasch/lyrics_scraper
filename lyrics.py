
import requests
from bs4 import BeautifulSoup


number_of_pages = 4  # might work with high number to cover all
band_name = "Indigo Girls"
url_name = band_name.lower().replace(' ', '-')  # this is awesome

with open('{}_lyrics.txt'.format(url_name), 'w') as outfile:  # creates a file and opens it for writing

    for counter in range(1, number_of_pages + 1):  # range does not include the upward boundary
        url = 'http://www.metrolyrics.com/{}-alpage-{}.html'.format(url_name, counter)

        # url = 'http://www.metrolyrics.com/taylor-swift-alpage-1.html'
        content = requests.get(url).text  # grabs a string of html-y text
        souper = BeautifulSoup(content, "html.parser")  # complex object(results set)
        results = souper.find_all('a', class_='title ')

        for result in results:
            alt = result.attrs['alt']
            if band_name in alt:
                lyric_url = result.attrs['href']
                content = requests.get(lyric_url).text  # grabs a string of html-y text
                souper = BeautifulSoup(content, "html.parser")  # complex object(results set)
                results = souper.find(id='lyrics-body-text')  # this is from the html
                outfile.write(results.text)
