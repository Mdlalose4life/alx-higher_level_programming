#!/usr/bin/python3
"""Finds a peak in an unsorted list of intergers"


def find_peak(list_of_intergers):
    """Returns a peak in a list"
    if list_of_intergers == []:
    	return None
    
    length = len(list_of_intergers)
    if length == 1:
    	return list_of_intergers[0]
    elif length == 2:
    	return max(list_of_intergers)
    	
    middle = int(length/2)
    peak = list_of_intergers[middle]
    if peak > list_of_intergers[middle - 1] and peak > list_of_intergers[middle + 1]:
    	return peak
    elif peak < list_of_intergers[middle -1]
    	return find_peak(list_of_intergers[:middle])
    else:
    	return find_peak(list_of_intergers[middle + 1:])
