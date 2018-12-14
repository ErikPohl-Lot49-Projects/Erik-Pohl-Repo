'''
Created on Dec 14, 2018

@author: Erik Pohl
'''

from Countput import Countput
word_sentence = 'a b c d e f g h i a c e g i c g'
word_list = word_sentence.split(' ')



MyCountput = Countput(word_list)
print(MyCountput.return_list(2, ' - '))
MyCountput.output_topn(2, ' - ')
print(MyCountput.return_dict())
