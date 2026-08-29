import statistics
def mean_median_mode(list1):
    return statistics.mean(list1),statistics.median(list1),statistics.mode(list1)
    
a,b,c=(mean_median_mode([45,78,65,10,4,2,31,14,54,54]))
print(f"Mean: {a}\nMedian: {b}\nMode: {c}")