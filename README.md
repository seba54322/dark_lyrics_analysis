# Dark Lyrics Analysis

## Resume

The notebooks presented here, were created to explore different techniques of natural language processing and analyze concepts and meanings behind the lyrics of houdreds of metal songs from the DarkLyrics collection.
<br>
Comparisons between subgenres of Power Metal and Black Metal were made, using wordclouds, LDA, ScatterText and some embedding manipulation.  
The analysis were made in the english subset of lyrics and is work in progress.

## Visualization description and examples 

### Word Clouds

The raw word frequency can be visualized as histograms (recommended for formal reports) and word clouds, which are a good option when the visual aspect is more important than the informative value, as in this case. The netxt image contains the top 50 frequent terms in the italian power metal corpus. 

![](https://github.com/seba54322/dark_lyrics_analysis/blob/master/wordclouds/Ingl%C3%A9s%2C%20Power%20Metal%2C%20Italia.png)

### LDA MODEL

A LDA model was trained with Gensim, and then visualized with pyLDAvis. This kind of visualization is interactive, and you can see the terms inside a topic as well as its frequency within each topic. Click on the image to interact. The LDA was trained on the whole english corpus. 

![](https://github.com/seba54322/dark_lyrics_analysis/blob/master/images/lda_viz.png)(https://github.com/seba54322/dark_lyrics_analysis/lda_viz/new_lda_total_english.html)

### Embedding Exploration 

A word embedding model was created with Gensim for the whole englih corpus, and some visualization experiments were made directly with it as input, and t-SNE with 2 dimensions for crating some images. 

![](https://github.com/seba54322/dark_lyrics_analysis/blob/master/images/similar_words.png)

### Scattertext 

Scattertext is a tool available for text comparisson which produces beautiful visualizations, using different frequency normalization methods.
All the HTML files, produced by the notebooks, are heavy, and first need to load and that can take time. After loading, an interactive file is avaliable in the browser, and when a word is selected, you can read the actual documments containing that particular word (hence, the amount of time loading). Click on the image and wait for interact with the data. 

![](https://github.com/seba54322/dark_lyrics_analysis/blob/master/images/st_top_countries_power_black_02.png)(https://github.com/seba54322/dark_lyrics_analysis/html_scattertext_files/st_top_countries_power_black_02.html)
