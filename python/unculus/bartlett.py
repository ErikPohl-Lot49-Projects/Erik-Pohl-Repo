from unculus_node import unculus_node

def collect(z):
    zaz.append(z)

bartlett = unculus_node('start')
bartlett.add_default_turnstile(bartlett,None)
inquotes = unculus_node('inquote')
bartlett.add_turnstile('"',inquotes, None)
inquotes.add_default_turnstile(inquotes, collect)
inquotes.add_turnstile('"', bartlett, None)

samplelist = list('Shelby told him, "I would like the sweet tea, please"')
zaz = []
start = bartlett
for n in samplelist:
    start = start.evaluate_token(n)
print(''.join(zaz))


