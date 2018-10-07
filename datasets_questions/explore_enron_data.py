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

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))


print "numbers of person is ", len(enron_data)

print "property of person is ", len(enron_data.get(tuple(enron_data.keys())[0]))

count = 0
for key in enron_data.keys():
    if enron_data.get(key).get('poi'):
        count += 1
print "number of email poi:", count

for key in enron_data.keys():
    if key.lower() == "prentice james":
        print "total_stock_value:", enron_data.get(key).get("total_stock_value")

poiNumbers = []
with open("../final_project/poi_names.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        if line.startswith("("):
            poiNumbers.append(line.strip()[4:])
print "number of poi:", len(poiNumbers)

for key in enron_data.keys():
    if key.lower() == "Colwell Wesley".lower():
        print "from_this_person_to_poi:", enron_data.get(key).get("from_this_person_to_poi")

for key in enron_data.keys():
    if key.lower().find("Jeffrey".lower()) >= 0 and \
            key.lower().find("Skilling".lower()) >= 0:
        print enron_data.get(key).get("exercised_stock_options")