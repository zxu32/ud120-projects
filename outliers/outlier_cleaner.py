#!/usr/bin/python
import heapq


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).
        :param predictions: list of predicted targets from regression
        :param ages: list of ages in the training set
        :param net_worths: list of actual NW in the training set
        :returns a list of tuples named cleaned_data where each tuple is of the form (age, net_worth, error).
    """
    dataSize = len(predictions)
    rawData = []
    for i in range(dataSize):
        rawData.append((ages[i], net_worths[i], abs(predictions[i]-net_worths[i])))
    cleaned_data = heapq.nsmallest(int(0.9*dataSize), rawData, key=lambda item: item[2])

    return cleaned_data
