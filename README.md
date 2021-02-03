# simpledispatch_py
When creating a dispatch function table via python dictionaries a simple problem arises, the key error.
While there are many ways to avoid the key error, including using try/catch, this library adds extra functionality to make it easy to avoid.
This is where the dispatch function comes in. 
After importing the library like:
`from safedispatch import *`
And defining the function like:
```python
def function1():
    pass
```
And making a blank dictionary:
`dispatch_dictionary = {}`
Either add the key normally like:
`dispatch_dictionary['function1']=function1 `
Or use the addkey function like:
`addkey('function1', dispatch_dictionary, function1)`
Then you can dispatch like so:
`dispatch('function1', dispatch_dictionary)`
If you need to call a failsafe if the function hasn't been entered
`if not dispatch('function1, dispatch_dictionary):
     print("That's it, nothing else)`
It's a fairly simple library, but if you want to make a menu structure, you can also do as below
`#add top level menu option
 addinner('option1', dispatch_dictionary)
 #add inner function item
 addkey('function1',dispatch_dictionary['option1'],function1)
 #dispatch the inner function
 dispatch('function1',dispatch_dictionary['option1'])`
 Hopefully everything works for you, as it has for me. 