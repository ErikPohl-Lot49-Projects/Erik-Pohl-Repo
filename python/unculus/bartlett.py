from unculus_node import unculus_node
from string import ascii_uppercase


def collect(z):
    zaz.append(z)


def foo():
    # return ['"','a'] to truncate the quote at the 'a'
    return ['"']

# create the pattern-matching start node
bartlett = unculus_node('start')
# any token which is not matched returns to the start node
bartlett.add_default_turnstile(bartlett, None)
# create a pattern-matching node for being in quotes
inquotes = unculus_node('inquote')
# if the token is a quote,
# go to the next pattern state, inquotes, and do nothing
bartlett.add_turnstile(['"'], inquotes, None)
# if the token is an uppercase letter,
# stay at the start state and print the token
bartlett.add_turnstile(list(ascii_uppercase), bartlett, print)
# if the token in quotes is anything but a quote or an uppercase,
# collect it using a handler function
inquotes.add_default_turnstile(inquotes, collect)
# if the token is a quote (demonstrate function call), go back to start state
inquotes.add_turnstile(foo(), bartlett, None)

# create a semi-interesting test case
samplelist = list('Shelby TOLD him, "I would like the sweet tea, please."')
# initialize the inquotes collection list
zaz = []
# set a start state
start = bartlett
# iterate through the semi-interesting test case
for n in samplelist:
    start = start.evaluate_token(n)
# output the collection of inquote tokens
print(''.join(zaz))
