import pandas as pd
from mlxtend.frequent_patterns import apriori
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import association_rules


dataset = [['Milk', 'Onion', 'Nutmeg', 'Kidney Beans', 'Eggs', 'Yogurt'],
           ['Dill', 'Onion', 'Nutmeg', 'Kidney Beans', 'Eggs', 'Yogurt'],
           ['Milk', 'Apple', 'Kidney Beans', 'Eggs'],
           ['Milk', 'Unicorn', 'Corn', 'Kidney Beans', 'Yogurt'],
           ['Corn', 'Onion', 'Onion', 'Kidney Beans', 'Ice cream', 'Eggs']]

te = TransactionEncoder()
te_ary = te.fit(dataset).transform(dataset)
df = pd.DataFrame(te_ary, columns=te.columns_)
frequent_itemsets = apriori(df, min_support=0.6, use_colnames=True)

#print(frequent_itemsets)
x=association_rules(frequent_itemsets, metric="confidence", min_threshold=0.7)
print((x))
#print((x['1']))
print(x.iloc[5, 2])
cosine=[0] * 11
certainty_factor=[0] * 11 
for i in range(0,11):
	cosine[i]=pow( ( ( (x.iloc[i, 2] * x.iloc[i, 5] ) / x.iloc[i, 3]) * x.iloc[i,5]),0.5)
	certainty_factor[i]= (x.iloc[i, 5] - x.iloc[i, 3] ) / ( 1 - x.iloc[i, 3])
print('Cosine:')
print(cosine)
print('Certainty Factor:')
print(certainty_factor)
