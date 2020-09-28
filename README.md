# Dark Lyrics Analysis

## Resume

The notebooks presented here, were created to explore different techniques of natural language processing and analyze concepts and meanings behind the lyrics of hundreds of metal songs from the DarkLyrics collection. The data was collected in the year 2014.
<br>
Comparisons between subgenres of Power Metal and Black Metal were made, using wordclouds, LDA, ScatterText and some embeddings manipulation. 

All the analysis were made with the english subset of lyrics and is work in progress.

## Visualization description and examples 

### Word Clouds

The raw word frequency can be visualized as histograms (recommended for formal reports) and word clouds, which are a good option when the visual aspect is more important than the informative value, as in this case. The next image contains the top 50 frequent terms in the italian power metal corpus. 

#### Italian Power Metal word cloud
![](https://github.com/seba54322/dark_lyrics_analysis/blob/master/wordclouds/Ingl%C3%A9s%2C%20Power%20Metal%2C%20Italia.png)

### LDA MODEL

A LDA model was trained with Gensim, and then visualized with pyLDAvis. This kind of visualization is interactive, and you can see the terms inside a topic as well as its frequency within each topic. Click on the image to interact. The LDA was trained on the whole english corpus. 

#### Whole DarkLyrics interactive topic model visualization
![](https://github.com/seba54322/dark_lyrics_analysis/blob/master/images/lda_viz.png)(https://github.com/seba54322/dark_lyrics_analysis/lda_viz/new_lda_total_english.html)

### Embedding Exploration 

A word embedding model was created with Gensim for the whole english corpus, and some visualization experiments were made directly with it as input. Using t-SNE with 2 dimensions some images were created, considering words of interest given the nature of the corpus.  

#### Visualization of 10 random words, with its 10 similar words, using 2 dimensional embeddings
![](https://github.com/seba54322/dark_lyrics_analysis/blob/master/images/similar_words.png)

### Scattertext 

Scattertext is a tool available for text comparison which produces beautiful visualizations, using different frequency normalization methods.

All the HTML files, produced by the notebooks, are heavy, and the first step is to open it and wait for the browsser to load the data, wich can take time. After loading, an interactive file is avaliable in the browser, and when a word is selected, you can read the actual documments containing that particular word (hence, the amount of time loading). 

The following depicted image is a comparison of Power Metal and Black Metal, considering the most distinctive terms for one category, given the other. For one of the datasets, the number of total songs per country was filtered according to the top 5 of countries for each genre. 

Power Metal lyrics, top 5 countries | Black Metal lyrics, top 5 countries
--- | ---
Germany 3494|Norway 2388
United States 2406|Sweden 1517
Sweden 1592|United States 999
Finland 1436|Finland 943
Italy 1002|Germany 755
  
Click on the image and wait for interact with the data. 

#### Scatterplot of word frequency, normalized by Log Odds Ratio and Log Frequency for Power Metal and Black Metal, for the top 5 countries
![](https://github.com/seba54322/dark_lyrics_analysis/blob/master/images/st_top_countries_power_black_02.png)(https://github.com/seba54322/dark_lyrics_analysis/html_scattertext_files/st_top_countries_power_black_02.html)
