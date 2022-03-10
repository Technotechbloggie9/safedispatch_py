
import logging

def dispatch(key, table):
    #this part ensures that if the key isn't found, a key error won't result
    '''
    get has a backup value, but here I put a function instead
    since dispatch is intended to call a function in a dictionary
    no error results
    '''
    result = False
    a = str(type(table.get(key, None)))
    if a == "<class 'function'>":
        table.get(key, notfound)()
        result = True
    else:
        logging.info("not a callable function")
    return result
    
def addkey(key, table, function):
    '''
    chose not to do a type-check here,
    it was more efficient in dispatch
    '''
    table[key] = function
    

def delkey(key, table):
    result = False
    if key in table.keys():
        del table[key]
        result = True
    else:
        notfound()
        return result
def addinner(key, table, innertable = {}):
    result = False
    if isinstance(innertable, dict):
        table[key] = innertable
        result = True
    else:
        logging.info("not a dictionary, try addkey")
    return result
def dictdir(table, option = "none"):
    '''
    intended to have options for keys and values,
    but these weren't very straightforward
    '''
    directory = ""
    print(table)
    directory = str(table)
    return directory
        
def sayhi():
    '''
    sayhi is a built in function for testing
    that the library is working, gives a warning
    '''
    logging.info("hello, this is just a test")
def notfound():
    '''
    This simple function gives an error message of key not found
    '''
    logging.info("key not found")
def billybob():
    '''
    billybob is a built in function for testing
    that the library is working, gives a warning
    (I thought having two might help)
    '''
    logging.info ("testing: Well if it isn't Billy Bob!")
'''
#example code
#purposely doesn't result in errors, at least that often
#but dispatch, delkey, addinner all return False on failure
#logging function also gives message, but as warning, not error
#but if used for webdev or gui, it should be using tightly controlled file
#TODO: adaptation to allow better logging for webdev/GUI
#thus we use a failsafe option for these such as the if not statement below
from safedispatch import *
def main():
    table = {}
    table["say hi"] = sayhi
    print(dispatch("say hi", table))
    print(dispatch("billy bob", table))
    #billybob wasn't added yet
    addkey("billy bob", table, billybob)
    if not dispatch("billy bob", table):
        #billybob still runs here despite if statement
        print("this message won't appear")
        #easier than try/catch, anyway
    addkey("hot taters", table, "taters")
    addkey("hot taters", table, "taters")
    print(table['hot taters'])
    dispatch("hot taters", table)
    addinner("mean lunch", table)
    delkey("mean lunch", table)
    delkey("mean lunch", table)
    if not dispatch("missing data", table):
        print("that was a failure")
    a = str(type(billybob))
    if a == "<class 'function'>":
        print("Okay Billy Bob.")
    dictdir(table, 'keys')
    
if __name__ == "__main__":
    main()
'''




