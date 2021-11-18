import Cards as ca
from matplotlib import pyplot as plt


# do a quick test to see how the card funkntion draws
list1 = ca.getcard(100000)

plt.rcParams["figure.autolayout"] = True

plt.hist(list1)


plt.show()
