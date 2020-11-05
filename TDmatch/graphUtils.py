import networkx as nx
import csv
import random
from tqdm import tqdm
import pickle


def graph_generator(firstDocs,secondDocs,configuration ):
    metadata_maps = {}
    i = 0
    G=nx.Graph()

    for doc in tqdm(firstDocs):
        i+=1
        if type(doc) ==list: text = ' '.join([r for r in doc])
        else: text = doc.lower()
        doc_name = str('FM'+str(i))

        metadata_maps[doc_name] = text
        metadata_maps[text] = doc_name

        G.add_node(doc_name , label= doc_name, type='Metadata1')

        j=0
        if configuration['scenario'] == 't2d':
            for cl in doc:
                j+=1
                col_name = str('COL'+str(j))
                if not G.has_node(col_name):     G.add_node(col_name , label= col_name, type='Column')
                    
                n_grams = [gr.replace(' ','_') for gr in find_all_n_grams(str(cl),configuration['tokens'])]

                for tg in n_grams:
                    if not G.has_node(tg): G.add_node(tg,label=tg, type='Data')
                    G.add_edge(doc_name,tg)
                    G.add_edge(col_name,tg)
        else:
            n_grams = [gr.replace(' ','_') for gr in find_all_n_grams(str(doc),configuration['tokens'])]

            for tg in n_grams:
                if not G.has_node(tg): G.add_node(tg,label=tg, type='Data')
                G.add_edge(doc_name,tg)

    
    i = 0

    for doc in tqdm(secondDocs):
        text = doc.lower()
        i += 1
        doc_name = str('SM'+str(i))
        metadata_maps[doc_name] = text
        metadata_maps[text] = doc_name

        G.add_node(doc_name , label= doc_name, type='Metadata2')

        n_grams = [gr.replace(' ','_') for gr in find_all_n_grams(text,configuration['tokens'])]

        for tg in n_grams:
            token = tg
            if not G.has_node(token): continue

            if not G.has_edge(doc_name,token):            G.add_edge(doc_name,token)
          
    #pickle.dump(metadata_maps,open('graphs/metadata_maps.pkl','wb'))
    return G,metadata_maps



def generate_walks(G,configuration):
    rws = []
    
    for i in tqdm(range(0,configuration['random_walks']),position=0):
        for node in G.nodes():
            if len([n for n in nx.neighbors(G,node)]) == 0:                continue
            if G.node[node]['type'] not in ['Data']:
                rws.append(random_walk(G,node,configuration['length']))
    return rws

def random_walk(G,node,l):
    res = ''
    
    p = 0
    chosen = node
    
    res += str(chosen)

    while (p<l):
        chosen = random.sample([n for n in nx.neighbors(G,chosen)],1)[0]
        #if G.node[chosen]['type'] not in ['Data']:
        res += ' ' + str(chosen)
        p+=1
        
    return res





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



