import matplotlib.pyplot as plt
# create two lists to store countries and costs in the same order
# sort costs list in ascending order
# draw bar plot using matplotlib
# I drew this plot with the help of matplotlib official doc
# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.bar.html#matplotlib.pyplot.bar
countries = ['Los_Angeles_1984', 'Seoul_1988', 'Barcelona_1992',
             'Atlanta_1996', 'Sydney_2000', 'Athens_2003',
             'Beijing_2008', 'London_2012']
costs = [1, 8, 15, 7, 5, 14, 43, 40]
print(sorted(costs))
plt.bar(range(8), costs)
plt.xticks(range(8), countries, rotation=20)
plt.show()
