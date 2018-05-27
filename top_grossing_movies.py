# Summary: Parses the top grossing movies on the IMDB website.
#   The keywords are then found and sent to a file for each movie.
# Author: Jonah Kubath
# Date: 5/27/2018
#
# Requirements
#   requests - sudo pip install requests
#   BeautifulSoup - sudo pip install BeautifulSoup
import sys
import csv
from bs4 import BeautifulSoup
import requests

URL = "https://www.imdb.com/search/title?at=0&sort=boxoffice_gross_us,desc&start=1&year=2017,2017"

def main():
    #Main Method
    print "Starting the program"
    movies = get_top_grossing_movie_links(URL)
    #open the file
    with open('output.csv', 'w') as output:
        csvwriter = csv.writer(output)
        #iterate through each movie and get 
        for title, url in movies:
            splitUrl = url.split('/')
            #get an array of keywords
            keywords = get_keywords_for_movie(
                'http://imdb.com/' + format(splitUrl[1]) + '/' + format(splitUrl[2]) + '/keywords')
            print title
            #write the file
            csvwriter.writerow([title] + keywords)
            # To write the keywords as an array use:
            # csvwriter.writerow([title, keywords])
    
    pass

#Return the links to the movies and their name
def get_top_grossing_movie_links(url):
    print "Retrieving the top grossing movies"
    response = requests.get(url)
    movies_list = []
    for each_url in BeautifulSoup(response.text, "html.parser").select('h3.lister-item-header a'):
        #print each_url['href']
        movie_title = each_url.text
        if movie_title != 'X':
            movies_list.append((movie_title, each_url['href']))
    return movies_list
  
#Return the keywords in the movies
def get_keywords_for_movie(url):
    keywords = []
    returnArray = []
    maxRows = 5
    maxKeywords = 10
    rowCount = 0
    keywordCount = 0
    #Get the webpage with the keywords
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    #Find the data table
    tables = soup.find_all('table', class_='dataTable')
    table = tables[0]
    #Iterate through each keyword and get the text
    for tr in table.find_all('tr'):
        if rowCount >= maxRows or keywordCount >= maxKeywords:
            break
        else:
            rowCount += 1
        #Iterate through the row of keywords
        for td in tr.find_all('td'):
            if keywordCount >= maxKeywords:
                break
            else:
                keywordCount += 1

            data = td.select('div a')
            if len(data) > 0:
                returnArray += [data[0].text.encode("utf-8")]
    return returnArray


#Exit when done with main
if __name__ == '__main__':
    sys.exit(main())
