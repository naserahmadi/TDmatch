from TDmatch.utils import *
from TDmatch.graphUtils import *
from gensim.models.word2vec import Word2Vec
from gensim.models.fasttext import FastText
from gensim.parsing.preprocessing import remove_stopwords
from tqdm import tqdm 


def train_model(docs,configuration):
	tagged_data = []
	for d in tqdm(docs,position=0):    	tagged_data.append(word_tokenize(d))

	if configuration['model'] == 'ft':
		model = FastText(size=configuration['model_vec'], min_count=1, window=configuration['model_window'], sg=configuration['model_sg'], seed=0, workers = 4)
	else: 
		model = Word2Vec(size=configuration['model_vec'], min_count=1, window=configuration['model_window'], sg=configuration['model_sg'], seed=0, workers = 4)
	
	model.build_vocab(tagged_data)
	
	model.train(tagged_data, total_examples=model.corpus_count, epochs=configuration['model_epochs'])
	print('model is ready')

	return model

