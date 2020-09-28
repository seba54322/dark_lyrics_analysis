# Dark Lyrics Analysis

## Resume

The notebooks presented here, were created to explore different techniques of natural language processing, analyzing concepts and meanings behind the lyrics of houdreds of metal songs from the DarkLyrics collection.
<br>
Comparisons between subgenres of Black Metal and Power Metal are made, using wordclouds, LDA, ScatterText and some embedding manipulation.  
The analysis were made in the english subset of lyrics. 

## Visualization description and examples 

### LDA MODEL

A LDA model was trained with Gensim, and then visualized with pyLDAvis. This kind of visualization is interactive, and you can see the terms inside a topic as well as its frequency within each topic. Click on the image to interact. The LDA was trained on the whole english corpus. 

[![Conventions-Visualization.html](https://github.com/seba54322/dark_lyrics_analysis/blob/master/images/lda_viz.png)](https://github.com/seba54322/dark_lyrics_analysis/lda_viz/new_lda_total_english.html)
