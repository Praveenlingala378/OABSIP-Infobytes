# -*- coding: utf-8 -*-
"""Untitled15.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1HO9lNEZuZrwKFgFnX2bP_DEBqw9t7qum

TASK-5 : SALES PREDICTION USING PYTHON

Author: **Lingala Praveen Sai**

Batch: July

Domain: Data Science
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("/content/Advertising.csv")

df.head()

df.shape

df.describe()

"""Average Expense spend is highest on TV
Avergae Expense Spend is lowest on Radio
Makeimu Sale is 27 & min 1.6
"""

sns.pairplot(df, x_vars=['TV', 'Radio','Newspaper'], y_vars='Sales', kind='scatter')
plt.show()

df['TV'].plot.hist(bins=10)

df['Radio'].plot.hist(bins=10, color="green", xlabel="Radio")

df['Newspaper'].plot.hist(bins=10,color="purple", xlabel="newspaper")

"""The Majority Sales is the result of low advertising cost in newspaper

"""

sns.heatmap(df.corr(),annot = True)
plt.show()

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(df[['TV']], df[['Sales']], test_size=0.2)

print(X_train)

print(y_train)

print(X_test)

print(y_test)

from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train,y_train)

res= model.predict(X_test)
print(res)

model.coef_

model.intercept_

0.05473199* 69.2 + 7.14382225

plt.plot(res)

plt.scatter(X_test, y_test)
plt.plot(X_test, 7.14382225 + 0.05473199 * X_test, 'r')
plt.show()

"""Conclusion: above mention solution is succesfully able to predict the sales uisng platform datasets"""

