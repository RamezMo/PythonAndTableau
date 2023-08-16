# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 18:39:00 2023

@author: CompuFast
"""

import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#method 1 to read json data
json_file = open('loan_data_json.json')
data = json.load(json_file)




#method 2 to read json data
# with open ('loan_data_json.json') as json_file :
#     data = json.load(json_file)

#transfrom to data frame
loandata = pd.DataFrame(data)


#finding the unique values in the purpose col
loandata['purpose'].unique()


#use describe function to describe the data
loandata.describe()

#desctibe data for specifc col
loandata['int.rate'].describe()
loandata['fico'].describe()
loandata['dti'].describe()

 
#using exp() function to get the annual income
income =  np.exp(loandata['log.annual.inc'])
loandata['annual income'] = income


#working with arrays    note : arrays need to be declared by numpy function but lists does not
#the coming one is a 1D array
arr = np.array([1,2,3,4])

#0D array example : 
arr = np.array(5)

#2D array : 
arr = np.array([[1,2,3],[4,5,6]])


#working with if statement
a = 50 
b = 400
if b  > a : 
    print("b is greater than a !")



#let's add more conditions :
a = 40
b = 500 
c = 1000
if b > a and b < c :
    print("b is the greater than a but less than c !")





#FICO Score 
fico = 301
if fico >= 300 and fico < 400 : 
    ficocat = 'Very Poor'
    
elif fico >= 400 and fico < 600 :
    ficocat = 'Poor'
    
elif fico >= 601 and fico < 660: 
    ficocat = 'Fair'

elif fico >= 660 and fico < 700:
    ficocat = 'Good'

elif  fico >=700:
    ficocat = 'Excellent'

else : 
    ficocat = 'Unknown'

print(ficocat)




#working on for loops :
fruits = ['apple','banana','pear']
for x in fruits :
    print(x)
    y = x + " fruit"
    print(y)



for x in range (0,3) : 
    y = fruits[x]
    print(y)



length = len(loandata['fico'])
ficocat = []
for x in range(0,length):
    category = loandata['fico'][x]
    try : 
    
        if category >= 300 and category <400 :
            cat = "very poor"    
        elif category >= 400 and category < 600 :
            cat = "poor"  
        elif category >= 601 and category < 660 :
            cat = "Fair"   
        elif category >= 660 and category < 700 :
            cat = "Good"
        elif category >= 700 :
           cat = "Excellent"
        else : 
           cat = "Unknown"
    except :
       cat = "Unknown"
    ficocat.append(cat)



#to convert list to Series which is col
ficocat = pd.Series(ficocat)

loandata['fico.Category'] = ficocat







# #testing error 

# length = len(loandata['fico'])
# ficocat = []
# for x in range(0,length):
#     category = "red"
#     if category >= 300 and category <400 :
#         cat = "very poor"    
#     elif category >= 400 and category < 600 :
#         cat = "poor"  
#     elif category >= 601 and category < 660 :
#         cat = "Fair"   
#     elif category >= 660 and category < 700 :
#         cat = "Good"
#     elif category >= 700 :
#        cat = "Excellent"
#     else : 
#        cat = "Unknown"

#     ficocat.append(cat)





#df.loc as conditional statement
loandata.loc[loandata['int.rate'] > 0.12 , "int.rate.type"] = "High"
loandata.loc[loandata['int.rate'] < 0.12 , "int.rate.type"] = "Low"




#number of loans/rows by fico.category

catplot = loandata.groupby(['fico.Category']).size()
catplot.plot.bar(color = "green" , width = 0.1 )
plt.show()



purposecount = loandata.groupby(["purpose"]).size()
purposecount.plot.bar(color = "red" , width = 0.5)
plt.show()



#scatter plots :
ypoint = loandata['annual income']
xpoint = loandata['dti']
plt.scatter(xpoint, ypoint , color = "red")
plt.show()




loandata.to_csv("loan_cleaned.csv" , index = True)





























































