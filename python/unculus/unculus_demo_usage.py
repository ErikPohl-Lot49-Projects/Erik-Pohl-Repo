from unculus_node import unculus_node

one = unculus_node('one')
two = unculus_node('two')

one.add_option(None,1)
one.add_option(two, 2)
two.add_option(one,3)
two.add_option(two,4)

head = one
z = [2,3,2,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,3,1]
head.consume(z)
print(head.is_consumed_completing_sequence(z))

z = [2,3,2,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,3]
print(head.is_consumed_completing_sequence(z))

z = [1]
print(head.is_consumed_completing_sequence(z))

z = [2,3,1,2]
print(head.is_consumed_completing_sequence(z))

z = [7,3,1,2]
print(head.is_consumed_completing_sequence(z))




