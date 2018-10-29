#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
data_dict.pop("TOTAL", 0)
features = ["salary", "bonus"]
data = featureFormat(data_dict, features)

max_salary = 0
### your code below
for point in data:
    salary = point[0]
    bonus = point[1]
    if max_salary < salary:
        max_salary = salary

    if salary > 1000000 and bonus > 5000000:
        print "salary:", salary, ",bonus:", bonus
    matplotlib.pyplot.scatter(salary, bonus)

for key in data_dict.keys():
    if data_dict.get(key).get("salary") == max_salary:
        print "maxSalary:", key
    if data_dict.get(key).get("salary") == 1072321.0:
        print "salary:1072321.0 is ", key
    if data_dict.get(key).get("salary") == 1111258.0:
        print "salary:1111258.0 is ", key

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()

