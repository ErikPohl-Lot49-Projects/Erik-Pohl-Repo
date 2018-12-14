'''
Created on Dec 14, 2018

@author: Erik Pohl
'''

from Countput import Countput
word_sentence = 'a b c d e f g h i a c e g i c g'
word_list = word_sentence.split(' ')



x = Countput(word_list)
print(x.return_list(2, ' - '))
x.output_topn(2, ' - ')
