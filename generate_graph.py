from TDmatch.utils import *
from TDmatch.graphUtils import *
import pandas as pd
import os

import argparse
if not os.path.exists('graphs'):	os.makedirs('graphs')

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--first_file', required=True)
    parser.add_argument('-ii', '--second_file', required=True)
    parser.add_argument('--scenario', required=False)
    parser.add_argument('--tokens', required=False, default=3)
    parser.add_argument('--normalize', required=False, default=True)
    parser.add_argument('--bucketing', required=False, default=False)

    parser.add_argument('-o','--output_file', required=True)
    return parser.parse_args()

args = parse_args()


configuration = {
    'tokens': args.tokens,
    'scenario': args.scenario,
    'normalize': args.normalize,
    'bucketing': args.bucketing,
}


docs = read_csv(args.first_file,True)
docs2 = read_csv(args.second_file,True)


graph = graph_generator(docs,docs2,configuration)

nx.write_gml(graph,'graphs/' + args.output_file+'.gml')