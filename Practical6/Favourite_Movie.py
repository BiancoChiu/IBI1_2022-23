import matplotlib.pyplot as plt
# Store number of students in favor of each genre in a dictionary
d = {'Comedy': 73, 'Action': 42, 'Romance': 38, 'Fantasy': 28,
     'Science-fiction': 22, 'Horror': 19, 'Crime': 18, 'Documentary': 12,
     'History': 8, 'War': 7}
# print the dictionary
print(d)
# Create two lists and store keys and values one to one correspondence in them
keys = list()
values = list()
for k, v in d.items():
    keys.append(k)
    values.append(v)
# I drew this plot with the help of matplotlib official doc
# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.pie.html
plt.pie(values, explode=[0.05, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        labels=keys, autopct='%.2f%%')
plt.show()
'''
We pretend the input to be Horror
Input is coming!
'''
In = 'Horror'
print(d[In])
