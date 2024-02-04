import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# change this to the file you're using and change the index_col as needed
df = pd.read_excel("Sample Emissions.xlsx", index_col="Sector")

coefs = {}

# by changing the index above, each item should correspond to a row in the dataframe
# we want to loop through each row and get the slopes
for ind in df.index:

    # fit a line to the row
    reg = LinearRegression().fit(np.array(df.loc[ind].index).reshape(-1, 1), df.loc[ind])

    # store the slope
    coefs[ind] = reg.coef_

# convert the dictionary to a dataframe for sorting
pd.DataFrame.from_dict(coefs, orient='index', columns=['Coefficient'])


