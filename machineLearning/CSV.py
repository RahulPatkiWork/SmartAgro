import csv
import random	
from datetime import datetime
import random
 

products=["Apple","Orange","Banana","Spinach","Cabbage","Potato","Wheat","Corn","Rice","Cotton","Sugercane","Pulses","Multinutrient","Nitrogen","Phosphet","Potassium","Organic","Compound","Insecticides","Herbicides","Rodenticides","Bacteriacides","Fungicides","Larvicides","Milletes","Sunflower","Niger","Pumkin","Cabbage_Seed","Spinach_Seed"]
#products=["Apple","Banana","Potato","Rice","Wheat"]
p_size=len(products)
with open('names1.csv', 'a') as csvfile:
    fieldnames = ['Customer_ID_Number', 'Transaction_ID','Product_Purchased','Date']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for i in range(50):
        c1=random.randint(1,10)
        p1=products[random.randint(1,p_size-1)]
        year = random.choice(range(2019, 2020))
        month = random.choice(range(1, 2))
        day = random.choice(range(1, 19))
        d1 = datetime(year, month, day)
	t1=random.randint(1,50)
        writer.writerow({'Customer_ID_Number':c1, 'Transaction_ID':t1,'Product_Purchased':p1,'Date':d1})



