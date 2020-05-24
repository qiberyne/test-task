import numpy as np
import random

import matplotlib.pyplot as plt
import squarify
import pandas as pd

def show(word_frequency_dict_noun, word_frequency_dict_verb, word_frequency_dict_npro, word_frequency_dict_adjs):
	# NOUN bubble

	noun_keys = list(word_frequency_dict_noun.keys())
	noun_values = list(word_frequency_dict_noun.values())

	x = np.random.randint(100, 10000, len(noun_keys))
	y = np.random.randint(100, 50000, len(noun_keys))
	s = noun_values
	labels = noun_keys

	df = pd.DataFrame(dict(x=x, y=y, s=s, labels=labels))

	fig, ax = plt.subplots(facecolor='w')

	plt.rcParams.update({'font.size': 6})
	plt.axis('off')


	for key, row in df.iterrows():
		ax.scatter(row['x'], row['y'], s=row['s']*200, alpha=.5, c='blue')
		ax.annotate(row['labels'], xy=(row['x'], row['y']))


	# Verb bubble

	verb_keys = list(word_frequency_dict_verb.keys())
	verb_values = list(word_frequency_dict_verb.values())

	x = np.random.randint(100, 10000, len(verb_keys))
	y = np.random.randint(100, 50000, len(verb_keys))
	s = verb_values
	labels = verb_keys

	df = pd.DataFrame(dict(x=x, y=y, s=s, labels=labels))

	fig, ax = plt.subplots(facecolor='w')

	plt.rcParams.update({'font.size': 6})
	plt.axis('off')
	

	for key, row in df.iterrows():
		ax.scatter(row['x'], row['y'], s=row['s']*200, alpha=.5, c='yellow')
		ax.annotate(row['labels'], xy=(row['x'], row['y']))

	# Pronoun bubble

	npro_keys = list(word_frequency_dict_npro.keys())
	npro_values = list(word_frequency_dict_npro.values())

	x = np.random.randint(100, 10000, len(npro_keys))
	y = np.random.randint(100, 50000, len(npro_keys))
	s = npro_values
	labels = npro_keys

	df = pd.DataFrame(dict(x=x, y=y, s=s, labels=labels))

	fig, ax = plt.subplots(facecolor='w')

	plt.rcParams.update({'font.size': 6})
	plt.axis('off')

	for key, row in df.iterrows():
		ax.scatter(row['x'], row['y'], s=row['s']*200, alpha=.5, c='red')
		ax.annotate(row['labels'], xy=(row['x'], row['y']))


	# Adjective bubble

	adjs_keys = list(word_frequency_dict_adjs.keys())
	adjs_values = list(word_frequency_dict_adjs.values())

	x = np.random.randint(100, 10000, len(adjs_keys))
	y = np.random.randint(100, 50000, len(adjs_keys))
	s = adjs_values
	labels = adjs_keys

	df = pd.DataFrame(dict(x=x, y=y, s=s, labels=labels))

	fig, ax = plt.subplots(facecolor='w')

	plt.rcParams.update({'font.size': 6})
	plt.axis('off')

	for key, row in df.iterrows():
		ax.scatter(row['x'], row['y'], s=row['s']*200, alpha=.5, c='green')
		ax.annotate(row['labels'], xy=(row['x'], row['y']))


	# Graph	

	plt.show()