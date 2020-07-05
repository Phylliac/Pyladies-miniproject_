#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random


# In[2]:


# creating a list withe words from the words text file
with open('words.txt', 'r') as words:
    word_list = words.readlines()


# In[3]:


# Dividing the lists of words into easy and hard words for the two different levels of difficulty
easy_words = []
hard_words = []
for word in word_list:
    if len(word) <= 5:
        easy_words.append(word)
    else:
        hard_words.append(word)


# In[4]:


# Defining the function for getting the random word
def get_word(list):
    random_num = random.randint(0, len(list)-1)
    word_chosen = list[random_num]
    return word_chosen


# In[5]:


#this code doesm't run as expected...debug
def guess_game(difficulty):
    if difficulty == 'easy':
        word = get_word(easy_words)
    elif difficulty == 'hard':
        word = get_word(hard_words)
    word.strip()
    print('Guess the word:{}'.format('#' * len(word)) )
    print('The word begins with {} and ends with {} '. format(word[0], word[len(word)-1]))
    return word
    


# In[6]:


guess_game('easy')


# In[ ]:


#this code doesm't run as expected...debug
def choose_level():
    name = input('Hi there! May I know your name? ')
    print('Welcome {} to the word guessing game!'. format(name))
    level = input('There are two levels in this game. Which level would you like to play?\nEnter 1 for easy and 2 for hard: ')
    while True:
        if (int(level) == 1):
            print('You have chosen level {} which is easy'.format(level))
            break
        elif (int(level) == 2):
            print('You have chosen level {} which is hard'.format(level))
            break
        else:
            print('Invalid option')
            level = input('There are two levels in this game. Which level would you like to play?\nEnter 1 for easy and 2 for hard: ')
        return int(level)


# In[ ]:


#choose_level()


# In[15]:


name = input('Hi there! May I know your name? ')
print('Welcome {} to the word guessing game!'. format(name))
level = input('There are two levels in this game. Which level would you like to play?\nEnter 1 for easy and 2 for hard: ')

while True:
    if (int(level) == 1):
        print('You have chosen level {} which is easy'.format(level))
        difficulty = 'easy'
        print(difficulty)
        break
    elif (int(level) == 2):
        print('You have chosen level {} which is hard'.format(level))
        difficulty = 'hard'
        print(difficulty)
        break
    else:
        print('Invalid option')
        level = input('There are two levels in this game. Which level would you like to play?\nEnter 1 for easy and 2 for hard: ')
        
#confirms level selcted and proceed if confirmed or request level required from user if denied
confirm = input('Would you like to proceed? y/n: ')
if (confirm.lower == 'y'):
    if (difficulty == 'easy'):
        word = get_word(easy_words)
    elif (difficulty == 'hard'):
        word = get_word(hard_words)
    word.strip()
    print('Guess the word:{}'.format('#' * len(word)) )
    print('The word begins with {} and ends with {} '. format(word[0], word[len(word)-1]))


# In[ ]:





# In[ ]:




