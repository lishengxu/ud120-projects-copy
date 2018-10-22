#!/usr/bin/python

def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []

    cleaned_data.sort()
    ### your code goes here
    agesLen = len(ages)
    for i in range(agesLen - 1):
        cleaned_data.append([ages[i], net_worths[i], net_worths[i] - predictions[i]])

    def f(a, b):
        return cmp(abs(a[2]), abs(b[2]))

    cleaned_data.sort(cmp = f)

    return cleaned_data[0: agesLen * 9 / 10 - 1]

