#!/usr/bin/env python3

import requests
from concurrent.futures import ThreadPoolExecutor
import html
import re
import time

def get(url):
    '''Makes an HTTP request to retreive the HTML page from the url'''
    response = requests.get(url, headers = {"User-Agent": "USOPENHistoryChampions/1.0 "}, timeout=15)    
    response.raise_for_status()
    return response.text

def get_tables(htmlPage):
    '''Uses regular expressions to extract the tables from the htmlPage given'''
    return re.findall(r"<table\b[^>]*>.*?</table>", htmlPage, flags = re.DOTALL | re.IGNORECASE)

def get_rows(table):
    '''Uses regular expressions to extract the rows from the table given'''
    return re.findall(r"<tr\b[^>]*>(.*?)</tr>", table, flags = re.DOTALL | re.IGNORECASE)

def clean(column):
    '''Retreives readable text, removing HTML tags and removes whitespace'''
    text = re.sub(r"<[^>]+>", "", column)
    return html.unescape(text).strip()

def clean_country(country):
    '''Extracts only the three word country code for every country'''
    match = re.match(r"[A-Z]{3}", country)
    return match.group() if match else country

def clean_champion(champion):
    '''Extracts only the champion name no symbols or numbers after'''
    champion = re.sub(r"\(\d+/\d+\)", "", champion) # removes the numbers in parentheses (i.e.(3,4))
    champion = re.sub(r"[†‡◊*]", "", champion) # removes any symbols after the champion name
    return champion.strip()

def get_columns(row):
    '''Uses regular expressions to extract the columns from the row given'''
    columns = re.findall(r"<t[dh]\b[^>]*>(.*?)</t[dh]>", row, flags = re.DOTALL | re.IGNORECASE)
    return list(map(clean, columns)) # returns list of lists of each of the rows split up into columns (each element in each interior list is a column)

def parse_champions(table):
    '''Extracts only the champions from the table (along with the year they won and country where they're from)'''
    rows = get_rows(table)
    columns = list(map(get_columns, rows))
    results = []
    for cells in columns:
        # Filters out rows without champions listed
        if len(cells) >= 3 and re.fullmatch(r"[0-9]{4}", cells[0]):
                    results.append({"Year": cells[0], "Country": clean_country(cells[1]), "Champion": clean_champion(cells[2])}) 
            
    return results # returns a list of dictionaries with year, country, and champions

def scrape(urlTuple):
    '''Scrapes the results by retreiving the htmlPage, getting the tables, parsing the champions and returns champions and tournament'''
    tournament, url = urlTuple

    htmlPage = get(url)
    tables = get_tables(htmlPage)
    champions = parse_champions(tables[2])

    return tournament, champions # Returns a tuple with the tournament name (string) and the list of all champions, country they are from, and what year they won (dict[str, str, int])

def main():
    '''Executes the scrape on all four urls (grand slams) and returns result'''
    urls = [("US Open", "https://en.wikipedia.org/wiki/List_of_US_Open_men%27s_singles_champions"),
            ("Wimbeldon", "https://en.wikipedia.org/wiki/List_of_Wimbledon_gentlemen%27s_singles_champions"),
            ("Australian Open", "https://en.wikipedia.org/wiki/List_of_Australian_Open_men%27s_singles_champions"),
            ("French Open", "https://en.wikipedia.org/wiki/List_of_French_Open_men%27s_singles_champions")
    ]
    
    for workers in [1, 8, 16]:
        start = time.perf_counter()
        with ThreadPoolExecutor(max_workers=2) as executor:
            results = list(executor.map(scrape, urls))
        elapsed = time.perf_counter() - start
        print(f'{workers} worker(s): {elapsed:.3f} seconds')
    for tournament, champions in results:
        print(f'\n{tournament}')

        for champion in champions:
            print(champion)

if __name__ == "__main__":
    main()
