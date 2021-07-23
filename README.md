# TDmatch

TDmatch is a Python library developed to perform matching tasks in three categories:
 * Text to Data which matches tuples of a table to text docuemts
 * Text to Structured text matches hierarchical taxonomy concepts to text docuemtns
 * Text to Text matches two copora of text documents


## Folder `notebooks` contains notebooks for running different scenarios.

First, the model creates a graph from document copora, next it trains a word embedding model on random walks generated by tracersing the graph and fainally, by employing the generated model we can match metadata between two corpora.


We used 4 datasets in testing different tasks:
 * Two fact checking datasets: **Politifact** and **Snopes** which we use for Text to Text matching. These datasets are presented in [That-is-a-Known-Lie](https://github.com/sshaar/That-is-a-Known-Lie)
 * Two datasets for Text to Data matching: **IMDB** which is created form  [IMDB top 1000 movies of all time](https://www.imdb.com/search/title/?groups=top_1000&sort=user_rating,desc&view=simple). **CoronaCheck** dataset is presented in [Scrutinizer](https://github.com/geokaragiannis/statchecker)


# How to run
Use the notebook for the required task to generate the results for the required dataset.

All the notebooks have the similar structure:

1. Creating the gaph
2. (optional) Expanding the graph with external sources
3. (optional) Compressing the graph with `MSP`
4. Generating random walks on the graph and training Word embedding model on random walks.  
5. Matching metadata nodes with model and printing the results. 



# Using `SSuM` compression
* First install the library following instructions [Here](https://github.com/KyuhanLee/SSumM)
* Use the code in `SSuM` block to generate input
* Generate the compressed graph: ``./run.sh input_path compression_ratio reconstruction_error``  



# Expanding with ConceptNet
* After installing [conceptnet_lite](https://github.com/ldtoolkit/conceptnet-lite), download ConceptNet DB from [this link](https://conceptnet-lite.fra1.cdn.digitaloceanspaces.com/conceptnet.db.zip)



