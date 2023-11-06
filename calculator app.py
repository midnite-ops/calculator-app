#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def calculation(num1,num2):
    
    number1 = int(num1)
    number2 = int(num2)
    
    print('Enter the operation')
    operation = input('arithmetic operation: ')
    
    while operation != '+' and operation != '-' and operation != '/' and operation != '*':
        print('Enter a valid operation')
        operation = input('arithmetic operation: ')
        
    if operation == '+':
        result = number1 + number2
    
    elif operation == '-':
        result = number1 - number2
    
    elif operation == '/':
        result = number1 / number2
        
    elif operation == '*':
        result = number1 * number2
    
    return result

calculation(input('Enter first number: '), input('Enter second number: '))
    
    


# In[ ]:




