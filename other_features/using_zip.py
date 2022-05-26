# zip is nothing to do with compression or archiving

# some collections
days =  ('mon', 'tue', 'wed', 'thu', 'fri')
fruit = ['banana', 'orange', 'kiwi', 'durian']
drink = ['coffee', 'tea', 'water', 'soya']

# zip lets us combine collections
j = zip(days, fruit, drink)

print(j)

for d, f, dr in j:
    print('On {} I ate {} with {}'.format(d, f, dr))