from TDmatch.utils import *
from TDmatch.graphUtils import *
from TDmatch.word_embeddings import *
import pandas as pd
import os

import argparse
if not os.path.exists('models'):	os.makedirs('models')
if not os.path.exists('walks'):    os.makedirs('walks')

configuration = {
    'graph_file': 'graphs/test.gml',
    'random_walks': 100,
    'length': 20,
    'model': 'w2v',
    'output_file': 'model_name',
    'save_walks': True,
    'model_window':3,
    'model_sg':1,
    'model_vec':100,
    'model_epochs': 10,
    
    'normalize': False,
}

def parse_args(args):
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--graph_file', required=True)
    parser.add_argument('-o','--model_name', required=True)
    parser.add_argument('')

G = nx.read_gml(configuration['graph_file'])

random_walks = generate_walks(G,configuration)

if configuration['save_walks']:
    pickle.dump(random_walks,open('walks/random_walks','wb'))

model = train_model(random_walks,configuration)

model.save('models/'+configuration['output_file']+_+configuration['model'])
