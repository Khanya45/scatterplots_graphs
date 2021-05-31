import matplotlib.pyplot as plt
import numpy as np

price = [220, 330, 190, 340, 410, 445, 415]
temperature = [14.2, 16.5, 11.8, 15.3, 18.8, 22.5, 19.5]
plt.xlabel("Temperature (degrees celcius)")
plt.ylabel("Price in (R)")
plt.title("Soup sales in relation to temperature")
plt.scatter(temperature, price)
m, b = np.polyfit(x, y, 1)
plt.show()


xs = [1,2,3,4,5]
ys = [x**3 for x in xs]

plt.plot(xs, ys)
plt.show()


import matplotlib.pyplot as plt
a = [1.3, 3.4, 2.3, 9.8]
b = [3.5, 4.9, 1.3, 2.2]
c = [9.7, 1.5, 4.3, 0.9, 11.2]
data1 = [a, b, c]
plt.subplot(121)
plt.boxplot(data1)
plt.xlabel("Colleges")
plt.ylabel("Scores")
plt.title("Boxplot for colleges")
plt.subplot(122)
plt.hist(data1, bins=5)
plt.show()


price = [220, 330, 190, 340, 410, 445, 415]
temperature = [14.2, 16.5, 11.8, 15.3, 18.8, 22.5, 19.5]
x_pos = [i for i, _ in enumerate(temperature)]
plt.bar(x_pos, price, color='#7A5C61')
plt.xlabel("Temperature (degrees celcius)")
plt.ylabel("Price in (R)")
plt.title("Soup sales in relation to temperature")
plt.xticks(x_pos, temperature)
plt.show()


