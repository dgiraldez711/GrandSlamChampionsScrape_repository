# GrandSlamChampionsScrape_repository

Scrapes the wikipedia webpage with multiple tables of data about tennis statistics for the four grand slams (US Open, Wimbeldon, Australian Open, French Open)

URLS used = "https://en.wikipedia.org/wiki/List_of_US_Open_men%27s_singles_champions", "https://en.wikipedia.org/wiki/List_of_Wimbledon_gentlemen%27s_singles_champions", "https://en.wikipedia.org/wiki/List_of_Australian_Open_men%27s_singles_champions", "https://en.wikipedia.org/wiki/List_of_French_Open_men%27s_singles_champions"

# Usage

General module to install:
```bash
pip install requests
```

Linux command to run:
```bash
chmod +x scrape.py
./scrape.py
```

# Preview of Output (Result)

{ Some of the output was cut out for space and practicality purposes (many rows that don't all fit in one screenshot) }

<img width="486" height="309" alt="Screenshot 2026-11-05 at 11 17 00 PM" src="https://github.com/user-attachments/assets/869e51e0-6b9d-4ed8-9b8c-cfc1c361e016" />

<img width="491" height="271" alt="Screenshot 2026-11-05 at 11 17 29 PM" src="https://github.com/user-attachments/assets/8e058afd-8510-4dc3-9282-da156ada2951" />

<img width="469" height="228" alt="Screenshot 2026-11-05 at 11 17 54 PM" src="https://github.com/user-attachments/assets/d5b69586-b5c9-461b-9869-0f78e1d3fed5" />

<img width="473" height="226" alt="Screenshot 2026-11-05 at 11 18 09 PM" src="https://github.com/user-attachments/assets/08fd3fd4-6689-4bec-810d-d2fea15773f8" />

# Performance Impact (Functional Programming and Concurrent.futures)

The functional programming was very useful and practical for this particular scraper as map() was used multiple times. The most impactful way it was used was implementing the get_columns(), get_rows() to the sequence of rows and columns as well as the clean() functions to the columns as these were large sequences of data. The map() was also applied to scrape all of the urls, however, in this case since there were only four urls it didn't have much of an impact but if more urls were implemented to this same program/scraper code, this would definitely have more of an impact in terms of time efficiency and use of memory. 

As shown above, the number of workers for the concurrent.futures module on this specific scraper did not impact the time as much and this is due to the fact that there are only four grand slams to scrape, so as explained above if more tournaments such as smaller ATP tournaments were included, this module would definitely have a bigger impact. Additionally, since the program takes 0.33 seconds to execute with only one worker which is already a relatively quick time, adding more workers would not really benefit as seen through the execution time. However, this all relates back to the number of tournaments which if more urls or tables (data to read) was added this would have an impact.    







