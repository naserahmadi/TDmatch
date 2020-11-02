from TDmatch.utils import *
from TDmatch.graphUtils import *
import pandas as pd
import os

import argparse
if not os.path.exists('graphs'):	os.makedirs('graphs')

configuration = {
    'tokens': 3,
    'first_file': 'data/corona/claims_USR.csv',
    'second_file': 'data/corona/claims_USR.csv',
    'scenario': 't2d',
    'output_file': 'test',
    
    'normalize': False,
    'bucketing': False,
}

def parse_args(args):
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--first_file', required=True)
    parser.add_argument('-i', '--second_file', required=True)

    parser.add_argument('-o','--output_file', required=True)
    parser.add_argument('')

docs = read_csv(configuration['first_file'],True)
docs2 = read_csv(configuration['second_file'],True)

graph = graph_generator(docs,docs2,configuration)

nx.write_gml(graph,'graphs/'+configuration['output_file']+'.gml')
