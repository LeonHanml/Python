import nltk
import matplotlib.pyplot as plt
fig = plt.figure()
from nltk.corpus import  gutenberg
raw = gutenberg.raw('melville-moby_dick.txt')
fdist = nltk.FreqDist(i.lower() for i in raw if i.isalpha())
fdist.plot()
fig.show()