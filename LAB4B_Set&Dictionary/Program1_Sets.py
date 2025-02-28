#Program 1
# initialize the sets based on the Venn Diagram
setA = {'a', 'b', 'c', 'd', 'f', 'g'}
setB = {'b', 'c', 'h', 'l', 'm', 'o'}
setC = {'c', 'd', 'f', 'h', 'i', 'j', 'k'}

#Elements in set a and b
print('-' * 60)
print('No. of Elements in Set A and Set B:', len(setA | setB))
print(setA | setB)
print('-' * 60)

#Elements in set b that are not part of set a and c
print('No. of Elements in Set B that are not in Set A and Set C:', len(setB - (setA.union(setC))))
print(setB.difference(setA.union(setC)))
print('-' * 60)

#Set Operations
#i. [h, i, j, k]
print('=' * 60)
print('PARTITIONS OF SETS'.center(60))
print('=' * 60)
print('Elements in Set C but not in Set A: ')
print(setC.difference(setA))
print('-' * 60)

#ii. [c, d, f]
print('Common Elements in Set A and Set C: ')
print(setA.intersection(setC))
print('-' * 60)

#iii. [b, c, h]
print('Intersection of Set B with other Sets: ')
print((setA.intersection(setB)).union(setB.intersection(setC)))
print('-' * 60)

#iv. [d, f]
print('Common Elements in Set A and Set C but not in Set B: ')
print(setA.intersection(setC.difference(setB)))
print('-' * 60)

#v. [c]
print('Intersection of All Three Sets ')
print(setA.intersection(setB).intersection(setC))
print('-' * 60)

#vi. [l, m, o]
print('Elements Unique to Set B')
print(setB.difference(setA.union(setC)))
print('-' * 60)

