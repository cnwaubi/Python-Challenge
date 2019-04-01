#!/usr/bin/env python
# coding: utf-8

# In[25]:


import os
import csv


# In[26]:


#Sets file path as file 
csvpath = os.path.join('Python-Challenge','PyBoss','employee_data.csv')


# In[27]:


#State abbr dictionary
us_state_abbrev = {

    'Alabama': 'AL',

    'Alaska': 'AK',

    'Arizona': 'AZ',

    'Arkansas': 'AR',

    'California': 'CA',

    'Colorado': 'CO',

    'Connecticut': 'CT',

    'Delaware': 'DE',

    'Florida': 'FL',

    'Georgia': 'GA',

    'Hawaii': 'HI',

    'Idaho': 'ID',

    'Illinois': 'IL',

    'Indiana': 'IN',

    'Iowa': 'IA',

    'Kansas': 'KS',

    'Kentucky': 'KY',

    'Louisiana': 'LA',

    'Maine': 'ME',

    'Maryland': 'MD',

    'Massachusetts': 'MA',

    'Michigan': 'MI',

    'Minnesota': 'MN',

    'Mississippi': 'MS',

    'Missouri': 'MO',

    'Montana': 'MT',

    'Nebraska': 'NE',

    'Nevada': 'NV',

    'New Hampshire': 'NH',

    'New Jersey': 'NJ',

    'New Mexico': 'NM',

    'New York': 'NY',

    'North Carolina': 'NC',

    'North Dakota': 'ND',

    'Ohio': 'OH',

    'Oklahoma': 'OK',

    'Oregon': 'OR',

    'Pennsylvania': 'PA',

    'Rhode Island': 'RI',

    'South Carolina': 'SC',

    'South Dakota': 'SD',

    'Tennessee': 'TN',

    'Texas': 'TX',

    'Utah': 'UT',

    'Vermont': 'VT',

    'Virginia': 'VA',

    'Washington': 'WA',

    'West Virginia': 'WV',

    'Wisconsin': 'WI',

    'Wyoming': 'WY',

}


# In[28]:


#Lists for Parsed Data
Emp_id = []
First_name = []
Last_name = []
DOB = []
SSN = []
State = []


# In[29]:


with open(csvpath, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    #appends information to empty lists as well as alters appropriately 
    for row in reader:
        Emp_id.append(row['Emp ID'])
        First_name.append(row['Name'].split(" ")[0])
        Last_name.append(row['Name'].split(" ")[1])
        DOB.append(row['DOB'].split('-')[1] + '/' + row['DOB'].split('-')[2] + '/' + row['DOB'].split('-')[0])
        SSN.append('***-**-' + row['SSN'].split('-')[2])
        State.append(us_state_abbrev[row['State']])

        #Merges List
New_Employee_List = zip(Emp_id, First_name, Last_name, DOB, SSN, State)
#Sets Output Destination
output_path = os.path.join("Python-Challenge","PyBoss","NewList.csv")


#Opens and writes to CSV file
with open(output_path, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile,delimiter=',')
    
    csvwriter.writerow(['Emp_id','First_name','Last_name','DOB','SSN','State'])
    csvwriter.writerows(New_Employee_List)
    
 
    
    


# In[30]:


with open(output_path, 'r') as readfile:
    print(readfile.read())


# In[ ]:




