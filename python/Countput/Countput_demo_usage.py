'''
Created on Dec 14, 2018

@author: Erik Pohl
'''

from Countput import Countput
word_sentence = 'a b c d e f g h i a c e g i c g'
word_list = word_sentence.split(' ')


MyCountput = Countput(word_list)
print(
    'return_as_list of strings : ' + str(
          MyCountput.return_topn_as_list_of_strings(
              n=2,
              delimiter=' - Value',
              prefix='[Term: ',
              suffix=' ]',
              header='Header'
          )
      )
)

print(
    'return_as_list of strings for sort_as_list_of_strings: ' + str(
          MyCountput.return_topn_as_list_of_strings(n=2)
      )
)

MyCountput.formatted_topn_output(
    n=2,
    delimiter=' - Value:',
    prefix='[Term: ',
    suffix=" ]"
)

MyCountput.formatted_topn_output(
    n=2,
    delimiter=' - Value:',
    prefix='[Term: ', suffix=" ]",
    header='Formatted Output with header:'
)

print(MyCountput.return_as_dict())

print(MyCountput.return_as_dict(1))
