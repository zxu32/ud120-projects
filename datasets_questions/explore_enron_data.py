#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

from pickle import _Unpickler
unpickEnron = _Unpickler(open("../final_project/final_project_dataset.pkl", mode="rb"), fix_imports=True, errors='ignore')
enron_data = unpickEnron.load()

for item in enron_data['SKILLING JEFFREY K']:
    print(item, enron_data['SKILLING JEFFREY K'][item])

print(len(enron_data))
# print(enron_data['LAY KENNETH L'])
# print(enron_data['FASTOW ANDREW S'])

count1 = 0
count2 = 0
for person in enron_data:
    if enron_data[person]['total_payments'] == 'NaN':
        count1 += 1
    if enron_data[person]['poi']:
        count2 += 1

print(count1, count2)
