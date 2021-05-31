import numpy
from scipy import stats
import matplotlib.pyplot as plt

test_scores = [12, 99, 86, 87, 88, 45, 87, 94, 78, 77, 85, 86]
my_mean = numpy.mean(test_scores)
print("the mean is : ", my_mean)

my_median = numpy.median(test_scores)
print("the median is : ", my_median)

my_mode = stats.mode(test_scores)
print("The mode is: ", my_mode)

my_range=numpy.ptp(test_scores)
print("The range is: ", my_range)

quartile = numpy.percentile(test_scores, 75)
print("The 75% percentile for the marks is: ", quartile)

my_stdn = numpy.std(test_scores)
print("The standard deviation is ", round(my_stdn, 2))

variance = numpy.var(test_scores)
print("The variance of the marks is:  ", variance)


test_scores = [12, 99, 65, 85, 42]
test_names = ["Andy", "Martin", "Zahara", "Vuyo", "Ziyaad"]
x_pos = [i for i, _ in enumerate(test_names)]
plt.bar(x_pos, test_scores, color='#7A5C61')
plt.xlabel("Student names")
plt.ylabel("Marks (%)")
plt.title("Python marks for 5 students")
plt.xticks(x_pos, test_names)
plt.show()






