import io

import re
import pymorphy2

import graph_generator

input_file = 'filepath'

counter_noun = 0
counter_adjs = 0
counter_verb = 0
counter_npro = 0

functors_pos = { 'NOUN', 'ADJS', 'VERB', 'NPRO' }

word_frequency_dict_noun = dict()
word_frequency_dict_adjs = dict()
word_frequency_dict_verb = dict()
word_frequency_dict_npro = dict()

def text_preparator(text):
	no_latin_text = ''

	for word in text.split():
		if re.match(r'^[А-Яа-я]', word):
			no_latin_text += word + ' '

	rus_and_points_text = ''

	for symbol in no_latin_text:
		if re.match(r'^[А-Яа-я]', symbol):
			rus_and_points_text += symbol
		else:
			rus_and_points_text += ' '

	return rus_and_points_text

# Приводит слово в начальную форму. Распределяет части речи по словарям
def normalize_query_word(word):
	morph = pymorphy2.MorphAnalyzer()

	p = morph.parse(word)[0]

	if (p.tag.POS == 'NOUN'):
		global counter_noun
		counter_noun += 1
		count = word_frequency_dict_noun.setdefault(p.normal_form, 0)
		word_frequency_dict_noun[p.normal_form] = count + 1

	if (p.tag.POS == 'ADJS' or p.tag.POS == 'ADJF'):
		global counter_adjs
		counter_adjs += 1
		count = word_frequency_dict_adjs.setdefault(p.normal_form, 0)
		word_frequency_dict_adjs[p.normal_form] = count + 1

	if (p.tag.POS == 'VERB'):
		global counter_verb
		counter_verb += 1
		count = word_frequency_dict_verb.setdefault(p.normal_form, 0)
		word_frequency_dict_verb[p.normal_form] = count + 1

	if (p.tag.POS == 'NPRO'):
		global counter_npro
		counter_npro += 1
		count = word_frequency_dict_npro.setdefault(p.normal_form, 0)
		word_frequency_dict_npro[p.normal_form] = count + 1


def stat_collector(text):
	words = text.split()


	for word in words:
		normalize_query_word(word)


def main():

	with io.open(input_file, 'r', encoding='utf-8') as file:
		text = file.read()
		text = text_preparator(text)

		print (text)

		stat_collector(text)

		print ('noun ' + str(counter_noun))
		print ('verb ' + str(counter_verb))
		print ('npro ' + str(counter_npro))
		print ('adjs ' + str(counter_adjs))


		graph_generator.show(word_frequency_dict_noun, word_frequency_dict_verb, word_frequency_dict_npro, word_frequency_dict_adjs)


if __name__== '__main__':
  	main()