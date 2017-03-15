import statistics
import math

example_list = [ 5, 6, 7, 12, 45, 21, 62]

x = statistics.stdev(example_list)
variance = x ** 2

actualvar = statistics.variance(example_list)

print(x)
print(variance)
print(actualvar)