from unculus_node import unculus_node

def collect(z):
    zaz.append(z)

bartlett = unculus_node('start', None, None, None)
bartlett.add_default_turnstile(bartlett)
inquotes = unculus_node('inquote', None, None, collect)
bartlett.add_turnstile(inquotes, '"')
inquotes.add_default_turnstile(inquotes)
inquotes.add_turnstile(bartlett, '"')

sample = 'Shelby told him "I would like the sweet tea, please"'
samplelist = list(sample)
zaz = []
start = bartlett
for n in samplelist:
    start = start.evaluate_token(n)
print(''.join(zaz))
