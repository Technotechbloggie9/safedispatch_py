# safedispatch.py
When creating a dispatch function table via python dictionaries a simple problem arises, the key error.
While there are many ways to avoid the key error, including using try/catch, this library adds extra functionality to make it easy to avoid.
This is where the dispatch function comes in. 
After importing the library like:
```python
from safedispatch import *
```
And defining the function like:
```python
def function1():
    pass
```
And making a blank dictionary:
```python
dispatch_dictionary = {}
```
Either add the key normally like:
```python
dispatch_dictionary['function1']=function1 
```
Or use the addkey function like:
```python
addkey('function1', dispatch_dictionary, function1)
```
Then you can dispatch like so:
```python
dispatch('function1', dispatch_dictionary)
```
If you need to call a failsafe if the function hasn't been entered
```python
if not dispatch('function1, dispatch_dictionary):
     print("That's it, nothing else")
```
It's a fairly simple library, but if you want to make a menu structure, you can also do as below
```python
#add top level menu option
 addinner('option1', dispatch_dictionary)
 #add inner function item
 addkey('function1',dispatch_dictionary['option1'],function1)
 #dispatch the inner function
 dispatch('function1',dispatch_dictionary['option1'])
 ```
I've recently removed the warnings in the logging component, opting to use logging.info instead. (as of 2/10/2021)
In order to display follow this guide to alter the logger settings. 
https://docs.python.org/3/howto/logging-cookbook.html

