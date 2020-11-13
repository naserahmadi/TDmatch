from TDmatch.utils import *
from TDmatch.graphUtils import *
from gensim.models.word2vec import Word2Vec
from gensim.models.fasttext import FastText
import pickle
import os

import argparse
if not os.path.exists('output'):	os.makedirs('output')

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--model_address', required=True)
    parser.add_argument('-ii', '--graph_address', required=True)
    parser.add_argument('--model_type', required=True)
    parser.add_argument('--golds', required=False)
    
    parser.add_argument('--direction', required=False,default='r2l')

    parser.add_argument('-o','--res', required=False)
    return parser.parse_args()

args = parse_args()


G = nx.read_yaml(args.graph_address)
maps = pickle.load(open(args.graph_address.split('.')[0]+'_metadata.pkl','rb'))

if args.model_type == 'ft': model = FastText.load(args.model_address)
else: model = Word2Vec.load(args.model_address)

md1,md2 = [],[]
for n in G.nodes():
    if G.nodes()[n]['type'] == 'Metadata1': md1.append(n)
    elif G.nodes()[n]['type'] == 'Metadata2': md2.append(n)

if args.direction == 'r2l':    results = compare_lists(model,md2,md1)
else: results = compare_lists(model,md1,md2)

if args.golds is not None:
    golds = pickle.load(open(args.golds,'rb'))
    for K in [1,3,5,20,50]:
        print("##################### TOP-"+str(K)+" ##################")
        print(evaluate_results (results,golds,maps,K),'\n')