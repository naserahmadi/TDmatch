from TDmatch.utils import *
from TDmatch.graphUtils import *
from TDmatch.word_embeddings import *
import pandas as pd
import os

import argparse
if not os.path.exists('models'):	os.makedirs('models')
if not os.path.exists('walks'):    os.makedirs('walks')


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--graph_file', required=True)
    parser.add_argument('-o','--model_name', required=True)
    parser.add_argument('--random_walks', required=False, default=10)
    parser.add_argument('--walks_length', required=False, default=25)
    #parser.add_argument('--save_walks', required=False, default=True)
    parser.add_argument('--model_class', required=False, default='w2v')
    return parser.parse_args()

args = parse_args()

configuration = {
    'graph_file': '',
    'random_walks': args.random_walks,
    'length': args.walks_length,
    'model': args.model_class,
    'output_file': '',
    'save_walks': True,
    'model_window':3,
    'model_sg':1,
    'model_vec':100,
    'model_epochs': 10,
    'normalize': False,
}



G = nx.read_gml(args.graph_file)

random_walks = generate_walks(G,configuration)
if configuration['save_walks']:
    pickle.dump(random_walks,open('walks/random_walks','wb'))

model = train_model(random_walks,configuration)

model.save('models/'+args.model_name)
