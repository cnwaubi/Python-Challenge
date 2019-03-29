#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import csv


# In[2]:


#Created File Path
csvpath = os.path.join('Python-Challenge','PyBank','budget_data.csv')


# In[3]:


#lists for month and revenue data
months = []
revenue = []


# In[4]:


#read csv and send data to lists
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    print(f" CSV Header: {csv_header}")
    
    for row in csvreader:
        months.append(row[0])
        revenue.append(int(row[1]))


#find total months
total_months = len(months)

#create greatest increase, decrease variables and set them equal to the first revenue entry
#Set total revenue = 0

greatest_increase = revenue[0]
greatest_decrease = revenue[0]
total_revenue = 0

#loop through revenue index and compare # to find greatest increase/decrease 
#also add each revenue to total revenue 
for r in range(len(revenue)):
    if revenue[r] >= greatest_increase:
        greatest_increase = revenue[r]
        greatest_increase_month = months[r]
    elif revenue[r] <= greatest_decrease:
        greatest_decrease = revenue[r]
        greatest_decrease_month = months[r]
    total_revenue += revenue[r]
        
#calculate average_change
average_change = round(total_revenue/total_months, 2)

#sets path for output file
PyBankoutput_path = os.path.join('Python-Challenge','PyBank','Pybank_Output_'  + '.txt')

with open(PyBankoutput_path, 'w', newline='') as csvfile:
    
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['Financial Analysis'])
    csvwriter.writerow(['----------------------------'])
    csvwriter.writerow(['Total Months: ' + str(total_months)])
    csvwriter.writerow(['Total Revenue: $' + str(total_revenue)])
    csvwriter.writerow(['Average Revenue Change: $' + str(average_change)])
    csvwriter.writerow(['Greatest Increase in Revenue: ' + greatest_increase_month + '($' + str(greatest_increase) + ')'])
    csvwriter.writerow(['Greatest Decrease in Revenue: ' + greatest_decrease_month + '($' + str(greatest_decrease) + ')'])


# In[5]:


with open(PyBankoutput_path, 'r') as readerfile:
    print(readerfile.read())


# In[ ]:




