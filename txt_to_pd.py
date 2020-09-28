# -*- coding: utf-8 -*-
#!/usr/bin/python

import re
import os
from os import walk
import bs4 
from bs4 import BeautifulSoup
import pandas as pd
import time
start = time.time()

path = './lyrics'
regex_end = 'Thanks to| for sending these lyrics. |Submits, comments, corrections are welcomed at webmaster@darklyrics.com | LYRICS'

cancion_con_todo = []
def parsefiles(path):
	
	for root, dirs, files in os.walk(path):
		files = [f for f in files if not f[0] == '.']
		dirs[:] = [d for d in dirs if not d[0] == '.']
		for file in files:
			if file.endswith(".txt"):
				with open(root + '/' + file) as album:
					file_contents = album.read()
					soup = BeautifulSoup(file_contents, 'html.parser')
					band_dirt = str(soup.a.string)
					band_name = band_dirt.replace(' LYRICS', '')
					album_dirt = str(soup.h2.string)
					album_name_year = album_dirt.replace('album:', '')
					album_name = str(re.findall(r'"([^"]*)"', album_name_year))
					album_name = album_name[2:-2]
					album_year = str(re.findall(r'\(([^"]*)\)', album_name_year))
					album_year = album_year[2:-2]
					lyrics_div = soup.find('div', class_='lyrics')
					lyrics = lyrics_div.prettify().split('<h3>')
					del lyrics[0]
					for lyric in lyrics:
						song_title = lyric.split('\n')[2]
						song_title = song_title.strip()
						cleanr = re.compile('<.*?>')
						lyric = re.sub(cleanr, '', lyric)
						lyric = lyric.replace("\n"," ")
						lyric = re.sub(regex_end, '', lyric)
						lyric = ' '.join(lyric.split())
						lyric = lyric.replace(str(band_name)," ")
						lyric = lyric.replace(str(song_title)," ")
						lyric = lyric.strip()
						cancion_con_todo.append((band_name,album_name,album_year,song_title,lyric))
parsefiles(path)

pd.set_option('display.max_columns', None)
df = pd.DataFrame(cancion_con_todo)
df.columns = ['band_name','album_name','album_year','song_title','lyric']
print (df)
print (df.shape)

end = time.time()
print('\ntime to process: ',end - start, 'seconds')
print ("fin")
