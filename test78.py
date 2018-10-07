#!/usr/bin/python
import os
import webbrowser

import requests
from bs4 import BeautifulSoup
'''
headers = { 'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}
'''

input_func = None

try:
    input_func = input('Enter the song to be played:')
except NameError:
    input_func = input('Enter the song to be played:')

query = input_func.replace('', '+')

#search for the best similar matching video

url = 'https://youtube.com/results?search_query' + query

source_code = requests.get(url,timeout=15)
plain_text = source_code.text
soup = BeautifulSoup(plain_text, "html.parser")


#fetches the url of video

songs = soup.findAll('div', {'class': 'yt-lockup-video'})
song = songs[0].contents[0].contents[0].contents[0]


try:
    link = song['href']
    webbrowser.open('https://www.youtube.com' + link)
except KeyError:
    print("Can't find any song,check your network or try a new word")


#########
'''
:python$ ./test78.py 
Enter the song to be played:'hele dil'
it will open youtube and play the songs acc to serach
'''





