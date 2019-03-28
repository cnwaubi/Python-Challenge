{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 107,
   "metadata": {},
   "outputs": [],
   "source": [
    "import os\n",
    "import csv\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 108,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Created File Path\n",
    "csvpath = os.path.join('..','PyBank','budget_data.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 109,
   "metadata": {},
   "outputs": [],
   "source": [
    "#lists for month and revenue data\n",
    "months = []\n",
    "revenue = []"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 110,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " CSV Header: ['Date', 'Profit/Losses']\n"
     ]
    }
   ],
   "source": [
    "#read csv and send data to lists\n",
    "with open(csvpath, newline='') as csvfile:\n",
    "    csvreader = csv.reader(csvfile, delimiter=',')\n",
    "    csv_header = next(csvreader)\n",
    "    print(f\" CSV Header: {csv_header}\")\n",
    "    \n",
    "    for row in csvreader:\n",
    "        months.append(row[0])\n",
    "        revenue.append(int(row[1]))\n",
    "\n",
    "\n",
    "#find total months\n",
    "total_months = len(months)\n",
    "\n",
    "#create greatest increase, decrease variables and set them equal to the first revenue entry\n",
    "#Set total revenue = 0\n",
    "\n",
    "greatest_increase = revenue[0]\n",
    "greatest_decrease = revenue[0]\n",
    "total_revenue = 0\n",
    "\n",
    "#loop through revenue index and compare # to find greatest increase/decrease \n",
    "#also add each revenue to total revenue \n",
    "for r in range(len(revenue)):\n",
    "    if revenue[r] >= greatest_increase:\n",
    "        greatest_increase = revenue[r]\n",
    "        greatest_increase_month = months[r]\n",
    "    elif revenue[r] <= greatest_decrease:\n",
    "        greatest_decrease = revenue[r]\n",
    "        greatest_decrease_month = months[r]\n",
    "    total_revenue += revenue[r]\n",
    "        \n",
    "#calculate average_change\n",
    "average_change = round(total_revenue/total_months, 2)\n",
    "\n",
    "#sets path for output file\n",
    "PyBankoutput_path = os.path.join('.','Pybank_Output_'  + '.txt')\n",
    "\n",
    "with open(PyBankoutput_path, 'w', newline='') as csvfile:\n",
    "    \n",
    "    csvwriter = csv.writer(csvfile)\n",
    "    csvwriter.writerow(['Financial Analysis'])\n",
    "    csvwriter.writerow(['----------------------------'])\n",
    "    csvwriter.writerow(['Total Months: ' + str(total_months)])\n",
    "    csvwriter.writerow(['Total Revenue: $' + str(total_revenue)])\n",
    "    csvwriter.writerow(['Average Revenue Change: $' + str(average_change)])\n",
    "    csvwriter.writerow(['Greatest Increase in Revenue: ' + greatest_increase_month + '($' + str(greatest_increase) + ')'])\n",
    "    csvwriter.writerow(['Greatest Decrease in Revenue: ' + greatest_decrease_month + '($' + str(greatest_decrease) + ')'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 111,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Financial Analysis\n",
      "----------------------------\n",
      "Total Months: 86\n",
      "Total Revenue: $38382578\n",
      "Average Revenue Change: $446309.05\n",
      "Greatest Increase in Revenue: Feb-2012($1170593)\n",
      "Greatest Decrease in Revenue: Sep-2013($-1196225)\n",
      "\n"
     ]
    }
   ],
   "source": [
    "with open(PyBankoutput_path, 'r') as readerfile:\n",
    "    print(readerfile.read())"
   ]
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
