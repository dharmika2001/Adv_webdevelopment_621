#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install requests


# In[2]:


import requests
import json
url = "https://michaelgathara.com/api/python-challenge"
response = requests.get(url)
challenges = response.json()
print(challenges)


# In[3]:


import requests
import math
import json

    
print("name:[NAGA DHARMIKA KANDERI]")
print("blazerid:[NKANDERI]")

def python_challenge(problems):
    
    for problem in problems:
        exp_id,question,operator = problem['id'],problem['problem'],None
        
        symbols = ['+','-','*','/']
        for op in symbols:
            if op in question:
                operator = op
                break

        if operator is None:
            print(f"question {exp_id}: {question} cannot be solved")
            continue
        elif operator is "":
            print(f"question {exp_id}:{question}cannot be determined")
            continue
        elif operator is -1:
            print(f"question {exp_id}:{question}cannot be determined")
            continue
        else:
            operands = question.split(operator)
            op1 = int(''.join([char for char in operands[0].strip() if char.isdigit()]))
            op2 = int(''.join([char for char in operands[1].strip() if char.isdigit()]))

        
        def expression_output(operator, operand1, operand2):
            operations = {
                '+': lambda x, y: x + y,'-': lambda x, y: x - y,
                '*': lambda x, y: x * y,'/': lambda x, y: x / y,
            }
            return operations[operator](operand1, operand2)

        answer = expression_output(operator, op1, op2)
        
        #math.floor to round off to integer values
        print(f"ANSWER[{exp_id}] FOR THE GIVEN QUESTION [{question}] IS: [{math.floor(answer)}],[{math.ceil(answer)}]")
#main block to be indented outside python_challenges to avoid indentation errors
url = "https://michaelgathara.com/api/python-challenge"
response = requests.get(url)
challenges = response.json()
print(challenges)
python_challenge(challenges)
    


# In[ ]:




