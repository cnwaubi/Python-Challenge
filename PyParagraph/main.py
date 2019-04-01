#!/usr/bin/env python
# coding: utf-8

# In[8]:


#Dependencies
import os
import string


# In[9]:


#sets file
textpath = os.path.join('Python-Challenge','PyParagraph','Resources','raw_data','paragraph_1.txt')


# In[10]:


#Opens and reads file and saves text as a paragraph string
paragraph_str = ''
with open(textpath,'r') as txtfile:
    paragraph_str = txtfile.read()


# In[11]:


#Sentence count by counting .,?, and ! as sentences
sen_count = paragraph_str.count('.') + paragraph_str.count('?') + paragraph_str.count('!')
#creates a string of upper and lowercase letters
letters = string.ascii_letters + " "
#loop through paragraph string and removes all characters 
#that are not letters replacing with nothing 
for c in paragraph_str:
    if c not in letters:
        paragraph_str = paragraph_str.replace(c,'')


# In[12]:


#reassigns the paragraph string and makes a list of words by splitting at spaces
paragraph_list = paragraph_str.split(" ")
#counts all of the letters in list paragraph
letter_total = 0

for word in paragraph_list:
    letter_total += len(word)
 #counts words by counting the length of paragraph list   
word_count = len(paragraph_list)
#calculates average word length by dividing the total# of letters
#by the number of words
avg_word_length = letter_total/word_count
#calculates words per sentence by dividing the number of words by the number of sentences.
words_per_sentence = word_count/sen_count

output_file = os.path.join('Python-Challenge','PyParagraph','Paragraph_Analysis','Analysis.txt')
#sets output file
with open(output_file, 'w') as txtfile:
    txtfile.writelines('Paragraph Analysis\n--------------------\nApproximaate word count: '
                      + str(word_count)+ '\nApproximate Sentence Count: '+ str(sen_count) + '\nAverage Letter Count: ' + str(avg_word_length)
                      + '\nAverage Sentence Length: ' + str(words_per_sentence))


# In[13]:


#opens output file and prints to terminal
with open (output_file, 'r') as txtout:
    print(txtout.read())

