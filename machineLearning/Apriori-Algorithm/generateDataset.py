import random


crops = ["Wheat", "Jowar", "Bajra", "Rice", "Moong", "Toor", "Rajma", "Sugarcane", "Saunf", "Dhania"]
automobileStuff = ["SideLight", "HeadLight", "Engine", "SteeringWheel", "WindShield", "Oil", "BreakPad", "Wheels", "Tires", "Car"]
otherStuff = ["Fertlizer1", "Fertlizer2", "Pesticide1", "Pesticide2",]


selected = []

#File 1
file = open('otherStuff.txt' ,'a') 
file.truncate()
for j in range(25):
    for x in range(10):
        selected.append(otherStuff[random.randint(0,3)])
    selected = set(selected)
    selected = list(selected)
    for i in range(len(selected)):
        if i != len(selected) - 1:
            file.write(selected[i] + ',')
        else:
            file.write(selected[i])
    selected = []
    file.write('\n')  

#File 2
file = open('crops.txt' ,'a') 
file.truncate()
for j in range(25):
    for x in range(10):
        selected.append(crops[random.randint(0,9)])
    selected = set(selected)
    selected = list(selected)
    for i in range(len(selected)):
        if i != len(selected) - 1:
            file.write(selected[i] + ',')
        else:
            file.write(selected[i])
    selected = []
    file.write('\n')  

#File 3
file = open('automobileStuff.txt' ,'a') 
file.truncate()
for j in range(25):
    for x in range(10):
        selected.append(automobileStuff[random.randint(0,9)])
    selected = set(selected)
    selected = list(selected)
    for i in range(len(selected)):
        if i != len(selected) - 1:
            file.write(selected[i] + ',')
        else:
            file.write(selected[i])
    selected = []
    file.write('\n')  

