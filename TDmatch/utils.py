import re 
import pickle
import csv

import re
def normalize_text(text):
    text = re.sub(r'#+', ' ', text )
    text = re.sub(r'@[A-Za-z0-9]+', ' ', text)
    #text = re.sub(r'[0-9]+', '', text)
    text = re.sub('\W', ' ', text)
    #text = re.sub(r'\d+', ' ', text)
    text = re.sub('\s+', ' ', text)
    text = re.sub(r"\'s", ' ', text)
    #text = re.sub('[^A-Za-z]+', ' ', text)
    text = re.sub(r'\b\w\b', ' ', text)
    text = text.strip()
    text = re.sub('\s+', ' ', text).strip()
    text = re.sub('\n+', ' ', text).strip()
    text = re.sub('\t+', ' ', text).strip()
    
    
    return text.lower()



from gensim.parsing.preprocessing import remove_stopwords

import nltk
ps = nltk.stem.PorterStemmer()

def read_csv(file,hasHeader):
    all_claims = []
    with open(file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        if hasHeader:
            next(csv_reader)
        for r in csv_reader:
            all_claims.append(' '.join(str(rr) for rr in r))

    return all_claims


def sentencize_text(p):
    sents = []
    for sent in tokenize.sent_tokenize(str(p)):
        if sent != '':
            sents.append(normalize_text(sent))    
    
    return sents   


from numpy import dot
from numpy.linalg import norm
from nltk import tokenize
from nltk.tokenize import word_tokenize
from scipy import spatial
from sklearn.metrics.pairwise import cosine_similarity

import pandas as pd


def distance_w2v (model, word,target_list , num) :
    cosine_dict ={}
    word_list = []

    for item in target_list :
        if item not in model.wv:
            continue
            
        cosine_dict[item] = model.wv.similarity(word,item)
            
    dist_sort=sorted(cosine_dict.items(), key=lambda dist: dist[1],reverse = True)
    for item in dist_sort:
        word_list.append((item[0], item[1]))
    return word_list[0:num]



########################## METRICS

def HAS_POSITIVE(actual,preds):
    for i in range(0,len(preds)):
        if preds[i] in actual:
            return 1
    return 0

def MRR(actual,preds):
    for i in range(0,len(preds)):
        if preds[i] in actual:
            return 1/(i+1)
    return 0


def MAP_K(actual,preds):
    precision = 0
    hit = 0
    for i in range(0,len(preds)):
        if preds[i] in actual:
            hit += 1
            precision += hit/(i+1)
    return precision/len(actual)    
