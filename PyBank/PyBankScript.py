#imports
import pandas as pd
import numpy as np

#read file and save as dataframe
df=pd.read_csv('budget_data.csv')
df1 = pd.DataFrame(df)

#change
change = df1['Profit/Losses'].diff()
change.head()

#avg change
avg_change = change.mean()
avg_change

#months
total_months = len(df1['Date'].unique())
total_months

#sum
total_amount = df1['Profit/Losses'].sum()
total_amount

#max index
profit_index = (df1['Profit/Losses'].idxmax())
profit_index

#min index
loss_index = (df1['Profit/Losses'].idxmin())
loss_index

#profit
def profit():
    return df1.iloc[profit_index]['Date'], df1['Profit/Losses'].max()

#losses
def loss():
    return df1.iloc[loss_index]['Date'], df1['Profit/Losses'].min()

def Financial_Analysis():
    print(f'Total Months: {total_months}')
    print(f'Total P&L: ${total_amount}')
    print(f'Average  Change: ${avg_change}')
    print(f'Greatest Decrease in Profits: {profit()}')
    print(f'Greatest Increase in Profits: {loss()}')

Financial_Analysis()

# exportable format
summary_table = pd.DataFrame({'Category': ['Total Months:', 'Total P&L:', 'Average Change:', 'Greatest Increase in Profits:', 'Greatest Decrease in Profits:'],
                              'Answer': [total_months, total_amount, avg_change, profit(), loss()]
                              })

summary_table.to_csv('PyBank.csv',index=False)