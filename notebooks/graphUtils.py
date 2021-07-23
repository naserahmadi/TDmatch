import networkx as nx
import csv
import random
from tqdm import tqdm

import random
def random_walk(G,node,l):
    res = ''
    
    p = 0
    chosen = node
    
    res += chosen

    while (p<l):
        chosen = random.sample([n for n in nx.neighbors(G,chosen)],1)[0]
        res += ' ' + chosen
        p+=1
        
    return res


def generate_random_walks(G,k,l):
    rws = []
    
    for i in tqdm(range(0,k),position=0):
        for node in G.nodes():
            if len([n for n in nx.neighbors(G,node)]) == 0:
                continue
            rws.append(random_walk(G,node,l))
    return rws



from gensim.parsing.preprocessing import remove_stopwords
from nltk.tokenize import word_tokenize
import nltk
ps = nltk.stem.PorterStemmer()



def return_n_grams(text,k):
    tokens = word_tokenize(remove_stopwords(text))
    n_grams = set()
    for i in range(0,len(tokens)-(k-1)):
        n_grams.add( ' '.join( ( [tk for tk in tokens[i:i+k]]) ))
        
    return n_grams




def find_all_n_grams (text,n):
    n_grams = []
    for k in range(1,n+1):
        k_grams = return_n_grams(text,k)
        for g in k_grams: n_grams.append(g)
    return n_grams



