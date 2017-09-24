import numpy as np

import pandas as pd
'''
data = [[1,2,3],[4,5,6],[7,8,9]]
index = [0,1,2]
columns=['a','b','c']
df = pd.DataFrame(data=data, index=index, columns=columns)
print (df.loc[2] )



count = 1
# used in the naming of the new txt files

txtFile = "his.txt"
# histogram text file

splitTxt = " Histogram           DN     Npts    Total   Percent   Acc Pct"
# string used to split the lines of code into sections/blocks

with open(txtFile,"r") as myResults:

    blocks = myResults.read()

for contents in blocks.split(splitTxt)[1:]:

    lines = contents.split('\n')

    with open('Results_{}.txt'.format(count), 'w') as op:

        op.writelines('{}'.format(splitTxt))

        for i in range(8):

            op.writelines('{}\n'.format(lines[i]))

    count = count + 1
'''
