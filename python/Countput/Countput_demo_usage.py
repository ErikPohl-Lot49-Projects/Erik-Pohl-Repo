'''
Created on Dec 14, 2018

@author: Erik Pohl
'''

from Countput import Countput
word_sentence = 'a b c d e f g h i a c e g i c g'
word_list = word_sentence.split(' ')



MyCountput = Countput(word_list)
print('return_as_list of strings : ' + str(MyCountput.return_topn_as_list_of_strings(2, ' - Value', '[Term: ', ' ]' )))
MyCountput.formatted_topn_output(2, ' - Value:', '[Term: ', " ]")
print(MyCountput.return_as_dict())
