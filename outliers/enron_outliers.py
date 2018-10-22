#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
data_dict.pop("TOTAL", 0)
data_dict.pop("SKILLING JEFFREY K", 0)
features = ["salary", "bonus"]
data = featureFormat(data_dict, features)


### your code below
maxSalary = 0
maxBonus = 0
for point in data:
    salary = point[0]
    bonus = point[1]
    if maxSalary < salary:
        maxSalary = salary
    if maxBonus < bonus:
        maxBonus = bonus
    print salary, bonus
    matplotlib.pyplot.scatter(salary, bonus)

print "maxSalary:", maxSalary, "maxBonus:", maxBonus
for each in data_dict.keys():
    if data_dict.get(each).get("salary") == maxSalary:
        print "key:", each

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()

