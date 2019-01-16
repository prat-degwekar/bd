
from fim import apriori, eclat, fpgrowth, fim
tracts = [ [ 1, 2, 3 ],
               [ 1, 4, 5 ],
               [ 2, 3, 4 ],
               [ 1, 2, 3, 4 ],
               [ 2, 3 ],
               [ 1, 2, 4 ],
               [ 4, 5 ],
               [ 1, 2, 3, 4 ],
               [ 3, 4, 5 ],
               [ 1, 2, 3 ] ]

print('transactions:')
for t in tracts: print(t)
print  ('\neclat(tracts, supp=-3, zmin=2):')
for r in eclat(tracts, supp=-3, zmin=2): print r
'''supp    minimum support of an item set         (default: 2)
        (positive: percentage, negative: absolute number)
        '''