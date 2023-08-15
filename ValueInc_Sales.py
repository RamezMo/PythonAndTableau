import pandas as pd
data = pd.read_csv('transaction.csv')
print(data)
data=pd.read_csv('transaction.csv',sep=';')
print(data)


#adding a col to display the cost price per transaction
data['CostPerTransaction'] = data['CostPerItem'] * data['NumberOfItemsPurchased']


#adding a col to display the selling price per transaction
data['SellingPricePerTransaction'] = data['SellingPricePerItem'] *  data['NumberOfItemsPurchased']


#adding a col to display the profit per transaction
data['ProfitPerTransaction'] = data['SellingPricePerTransaction'] - data['CostPerTransaction']


#adding a col to display the Markup per transaction "percentage of profit"
data['Markup'] = data['ProfitPerTransaction'] / data['CostPerTransaction']



#change the Day data col to str
day=data['Day'].astype(str)
print(day.dtype)


#change the year data col to str
year=data['Year'].astype(str)
print(year.dtype)


#make a data col to store the Date per transaction in
My_Date = day + "-" + data['Month'] + "-" + year
data['date']=My_Date


#using the split function to split the "Client Keywords" column
#new_var = col.str.split("sep",expand=True)
split_col=data['ClientKeywords'].str.split(',' , expand=True)


#creating new cols for the splitted Clinet Keywords Col
data['ClientAge'] = split_col[0]
data['ClientType'] = split_col[1]
data['LengthOfContract'] = split_col[2]

#Using replace function
data['ClientAge'] = data['ClientAge'].str.replace('[' , '')
data['LengthOfContract'] = data['LengthOfContract'].str.replace(']' , '')


#using the lower function to change col to Lower Case
data['ItemDescription'] = data['ItemDescription'].str.lower()


#How to merge files
#bringing in a newdataset
seasons = pd.read_csv("value_inc_seasons.csv",sep=";")

#merge the two data sets

data = pd.merge(data,seasons, on= 'Month')

data = data.drop(['Year' , 'ClientKeywords','Month' , 'Day'], axis =1)


#store the new file as csv file
data.to_csv("ValueInc_Cleaned.csv",index=False)













































