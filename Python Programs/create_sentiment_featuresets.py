'''
[chair, table, spoon, monitor] # lexicon

I pulled the chair up to the table # string of words

[1 1 0 0]   # vector of words matching lexicon
'''

import nltk
from nltk.tokenize import word_tokenize # separates the words in a sentence
from nltk.stem import WordNetLemmatizer # removes ing and ed, running = run, runs = run
import numpy as np 
import random, pickle  # pickle = to bytes for quicker processing
from collections import Counter

lemmatizer = WordNetLemmatizer()
hm_lines = 1000000  # might run out of RAM

def create_lexicon(pos, neg):
	lexicon = []
	for fi in [pos, neg]:
		with open(fi, 'r') as f:
			contents = f.readlines()
			for l in contents[:hm_lines]:
				all_words = word_tokenize(l.lower())  # take each line and separate into words
				lexicon += list(all_words)  # populate the lexicon with all the words

	lexicon = [lemmatizer.lemmatize(i) for i in lexicon]
	w_counts = Counter(lexicon) # dictionary that tells how many times each word appears in the set
	l2 = []
	for w in w_counts:
		# do not want most common words, but also do not want obscure words
		if 1000 > w_counts[w] > 50:
			l2.append(w)

	print(len(l2))
	return l2

def sample_handling(sample, lexicon, classification):
	featureset = [] # list of lists with hot array with index of words that appear in lexicon
	with open(sample, 'r') as f:
		contents = f.readlines()
		for l in contents[:hm_lines]:
			current_words = word_tokenize(l.lower())
			current_words = [lemmatizer.lemmatize(i) for i in current_words]
			features = np.zeros(len(lexicon))
			for word in current_words:
				if word.lower() in lexicon:
					index_value = lexicon.index(word.lower())
					features[index_value] += 1

			features = list(features)
			featureset.append([features, classification])

	return featureset

def create_feature_sets_and_labels(pos, neg, test_size = 0.1):
	lexicon = create_lexicon(pos,neg)
	features = []
	features += sample_handling('pos.txt', lexicon, [1,0])
	features += sample_handling('neg.txt', lexicon, [0,1])
	random.shuffle(features)

	features = np.array(features)

	testing_size = int(test_size * len(features))
	# featureset = [[]] 
	'''
	[[features, label],
	 [features, label],
	 [features, label],
	 [features, label]]
	'''

	train_x = list(features[:,0][:-testing_size])
	train_y = list(features[:,1][:-testing_size])

	test_x = list(features[:,0][-testing_size:])
	test_y = list(features[:,1][-testing_size:])

	return train_x, train_y , test_x, test_y

if __name__=='__main__':
	train_x, train_y, test_x, test_y = create_feature_sets_and_labels('pos.txt', 'neg.txt')
	with open('sentiment_set.pickle', 'wb') as f:
		pickle.dump([train_x, train_y, test_x, test_y], f)

