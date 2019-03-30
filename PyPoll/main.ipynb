{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import os \n",
    "import csv"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "#created File Path\n",
    "csvpath = os.path.join('..','PyPoll','election_data.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<_csv.reader object at 0x000002312E4EC798>\n",
      "CSV Header: ['Voter ID', 'County', 'Candidate']\n",
      "Election Results for file 'election_data_.csv'\n",
      "----------------------------------------------------\n",
      "Total Vote: 3521001\n",
      "----------------------------------------------------\n",
      "Khan: 63.0% (2218231)\n",
      "Correy: 20.0% (704200)\n",
      "Li: 14.0% (492940)\n",
      "O'Tooley: 3.0% (105630)\n",
      "----------------------------------------------------\n",
      "Winner: Khan\n",
      "----------------------------------------------------\n",
      "\n"
     ]
    }
   ],
   "source": [
    "#empty list variables\n",
    "County= []\n",
    "Candidate= []\n",
    "IndividualCandidate= []\n",
    "IndividualCandidateVote= []\n",
    "CandidateVotePercentage= []\n",
    "TotalCount= 0\n",
    "\n",
    "with open(csvpath, newline='') as csvfile:\n",
    "    csvreader = csv.reader(csvfile, delimiter=',')\n",
    "    print(csvreader)\n",
    "    csv_header = next(csvreader)\n",
    "    print(f\"CSV Header: {csv_header}\")\n",
    "    \n",
    "    for row in csvreader:\n",
    "        TotalCount = TotalCount + 1\n",
    "        Candidate.append(row[2])\n",
    "        \n",
    "    for x in set (Candidate):\n",
    "        IndividualCandidate.append(x)\n",
    "        Candidate.count(x)\n",
    "        IndividualCandidateVote.append(Candidate.count(x))\n",
    "        CandidateVotePercentage.append(Candidate.count(x)/TotalCount)\n",
    "        \n",
    "    Winner = IndividualCandidate[IndividualCandidateVote.index(max(IndividualCandidateVote))]\n",
    "    \n",
    "    # Output Path File\n",
    "    Output_path = os.path.join('..','PyPoll','PyPoll_Output_' + '.txt')\n",
    "    \n",
    "    #write Mode\n",
    "\n",
    "with open('PyPoll_Output_' + '.txt', 'w') as text:\n",
    "    \n",
    "    text.write(\"Election Results for file 'election_data_\"+ \".csv'\"+\"\\n\")\n",
    "    text.write(\"----------------------------------------------------\\n\")\n",
    "    text.write(\"Total Vote: \" + str(TotalCount) + \"\\n\")\n",
    "    text.write(\"----------------------------------------------------\\n\")\n",
    "    for i in range(len(set(Candidate))):\n",
    "        text.write(IndividualCandidate[i] + \": \" + str(round(CandidateVotePercentage[i]*100,1)) +\"% (\" + str(IndividualCandidateVote[i]) + \")\\n\")\n",
    "    \n",
    "    text.write(\"----------------------------------------------------\\n\")\n",
    "    text.write(\"Winner: \" + Winner + \"\\n\")\n",
    "    text.write(\"----------------------------------------------------\\n\")\n",
    "with open(Output_path,'r')as readfile:\n",
    "    print(readfile.read())\n",
    "        \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
