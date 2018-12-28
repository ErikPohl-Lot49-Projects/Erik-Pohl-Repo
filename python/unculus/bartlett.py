from unculus_node import unculus_node
from string import ascii_uppercase


def collect(z):
    zaz.append(z)


def foo():
    # return ['"','a'] to truncate the quote at the 'a'
    return ['"']

bartlett = unculus_node('start')
bartlett.add_default_turnstile(bartlett, None)
inquotes = unculus_node('inquote')
bartlett.add_turnstile(['"', '%'], inquotes, None)
bartlett.add_turnstile(list(ascii_uppercase), bartlett, print)
inquotes.add_default_turnstile(inquotes, collect)
inquotes.add_turnstile(foo(), bartlett, None)

samplelist = list('Shelby TOLD him, "I would like the sweet tea, please."')
zaz = []
start = bartlett
for n in samplelist:
    start = start.evaluate_token(n)
print(''.join(zaz))
