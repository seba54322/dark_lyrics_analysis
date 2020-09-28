# Dark Lyrics Analysis

## Resume
Natural Language Processing techniques examples, exploring metal song lyrics, from the DarkLyrics collection.
Comparisons between subgenres of Black Metal and Power Metal are made, using wordclouds, LDA, ScatterText and some embedding manipulation. 
The analysis were made in the english subset of lyrics. 

## Detail 

The notebooks were created to explore the meaning behind a collection of lyrics of Metal Music, and to apply natural language techniques from basic to advanced while learning in practice.

The global process starts with a collection of txt files, with album lyrics, inside a folder for each artist: artist/lyrics_album_n.txt

### LDA MODEL

A LDA model was trained with Gensim, and then visualized with pyLDAvis. This kind of visualization is interactive, and you can see the terms inside a topic as well as its frequency within each topic. Click on the image to interact. 





Some embeddings were made with 10 random words
![](https://github.com/seba54322/dark_lyrics_analysis/blob/master/similar_words.png)

<a href="https://htmlpreview.github.io/?https://github.com/seba54322/dark_lyrics_analysis/blob/master/lda_viz/new_lda_total_english.html" target="_blank">LDA On the whole english corpus (PyLDAvis)</a>
