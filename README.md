# Dark Lyrics Analysis

## Resume
Natural Language Processing techniques examples, exploring metal song lyrics, from the DarkLyrics collection.
Comparisons between subgenres of Black Metal and Power Metal are made, using wordclouds, LDA, ScatterText and some embedding manipulation. 
The analysis were made in the english subset of lyrics. 

## Detail 

The notebooks were created to explore the meaning behind a collection of lyrics of Metal Music, and to apply natural language techniques from basic to advanced while learning in practice.

The global process starts with a collection of txt files, each of one has a full album on it, inside a folder for each artist: artist/lyrics_album_n.txt

<a href="http://htmlpreview.github.io/?https://github.com/seba54322/dark_lyrics_analysis/blob/master/new_lda_total_english.html" target="_blank">LDA On the whole english corpus (PyLDAvis)</a>

<a href="https://github.com/seba54322/dark_lyrics_analysis/blob/master/similar_words.png" target="_blank">tSNE visualization of the 10 closest words, for 10 random words, with PCA into 2 dimensions.</a>

This are 2 Scattertext examples. Each one is a html file 
<a href="https://github.com/seba54322/dark_lyrics_analysis/blob/master/new_power_black_v3_pretty.html" target="_blank">Scatterplot visualization of words from Power Metal vs Black Metal, ranked by frequency percentile.</a>34MB

<a href="https://github.com/seba54322/dark_lyrics_analysis/blob/master/power_black_LOPriorvsLog_pretty.html" target="_blank">More sophisticated Scattertext visualization of words comparisson of Power Metal vs Black Metal.</a>36MB
