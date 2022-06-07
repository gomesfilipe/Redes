from math import sqrt

def min(list):
    if len(list) == 0:
        return None
    
    smallest = list[0]
    for item in list:
        if item < smallest:
            smallest = item
    
    return smallest

def max(list):
    if len(list) == 0:
        return None
    
    greatest = list[0]
    for item in list:
        if item > greatest:
            greatest = item
    
    return greatest

def avg(list):
    if len(list) == 0:
        return None
    
    sum = 0
    for item in list:
        sum = sum + item
    
    return sum / len(list)
    
def mdev(list):
    if len(list) == 0:
        return None
    
    average = avg(list)
    sum = 0
    for item in list:
        sum = sum + (item - average) ** 2

    return sqrt(sum / len(list))

def print_datas(list, total_pings, time_exec):
    if len(list) == 0:
        return None
    
    percent = (1 - len(list) / total_pings) * 100

    print('{} packets transmitted, {} received, {:.3f}% packet loss, time {}ms rtt min/avg/max/mdev = {:.3f}/{:.3f}/{:.3f}/{:.3f}ms'
            .format(total_pings, len(list), percent, int(time_exec), min(list), avg(list), max(list), mdev(list)))
