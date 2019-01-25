import csv
import pandas as pd
from mlxtend.preprocessing import OnehotTransactions
from mlxtend.frequent_patterns import apriori
 
with open('names1.csv') as csvfile:
	my_dict={}
	reader = csv.DictReader(csvfile)
	for row in reader:
		c=row['Customer_ID_Number']
		d=row['Date']
		test=c+d
		if test in my_dict.keys():
			my_dict[test].append(row['Product_Purchased'])
		else:
			my_dict[test]=[row['Product_Purchased']]


dataset=my_dict.values()
#print(dataset)
transactions=[]
for k in dataset:
	transactions.append(k)

print(transactions)
from efficient_apriori import apriori

itemsets, rules = apriori(transactions, min_support=0.5,  min_confidence=1)
print(rules)  # [{eggs} -> {bacon}, {soup} -> {bacon}]

