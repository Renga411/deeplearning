
# coding: utf-8

# In[1]:


import os as os
from os import *
import random


# In[2]:


PATH="/home/paperspace/fastai/courses/dl1/data/seedlings"


# In[3]:


classes = get_ipython().getoutput('ls {PATH}/train')


# In[4]:


def copy_to_valid(chosen_files,class_dir):
    for i in range (len(chosen_files)):
        get_ipython().system('mv "{PATH}/train/{class_dir}/{chosen_files[i]}" "{PATH}/valid/{class_dir}"')


# In[5]:


for classname in classes:
    os.makedirs(f'{PATH}/valid/{classname}', exist_ok=True)
    list_of_files = get_ipython().getoutput('ls "{PATH}/train/{classname}"')
    random.shuffle(list_of_files)
    n_files_moved=int(len(list_of_files)*0.2)
    selected_files = [list_of_files[m] for m in range(n_files_moved)]
    copy_to_valid(selected_files,classname)

