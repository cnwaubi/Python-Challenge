#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os 
import csv


# In[2]:


#created File Path
csvpath = os.path.join('Python-Challenge','PyPoll','election_data.csv')


# In[7]:


#empty list variables
County= []
Candidate= []
IndividualCandidate= []
IndividualCandidateVote= []
CandidateVotePercentage= []
TotalCount= 0

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    
    for row in csvreader:
        TotalCount = TotalCount + 1
        Candidate.append(row[2])
        
    for x in set (Candidate):
        IndividualCandidate.append(x)
        Candidate.count(x)
        IndividualCandidateVote.append(Candidate.count(x))
        CandidateVotePercentage.append(Candidate.count(x)/TotalCount)
        
    Winner = IndividualCandidate[IndividualCandidateVote.index(max(IndividualCandidateVote))]
    
    # Output Path File
    Output_path = os.path.join('Python-Challenge','PyPoll','PyPoll_Output_' + '.txt')
    
    #write Mode

with open('PyPoll_Output_' + '.txt', 'w') as text:
    
    text.write("Election Results for file 'election_data_"+ ".csv'"+"\n")
    text.write("----------------------------------------------------\n")
    text.write("Total Vote: " + str(TotalCount) + "\n")
    text.write("----------------------------------------------------\n")
    for i in range(len(set(Candidate))):
        text.write(IndividualCandidate[i] + ": " + str(round(CandidateVotePercentage[i]*100,1)) +"% (" + str(IndividualCandidateVote[i]) + ")\n")
    
    text.write("----------------------------------------------------\n")
    text.write("Winner: " + Winner + "\n")
    text.write("----------------------------------------------------\n")
with open(Output_path,'r')as readfile:
    print(readfile.read())
        


# In[ ]:





# In[ ]:




