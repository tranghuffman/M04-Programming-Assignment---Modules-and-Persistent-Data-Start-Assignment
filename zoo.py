#Create a file called zoo.py. In it, define a function called hours() that prints the string 'Open 9-5 daily'. Then, use the interactive interpreter to import the zoo module and call its hours() function.
def hours():
    print("Open 9-5 daily")
from zoo import hours as info
hours()

#In the interactive interpreter, import the zoo module as menagerie and call its hours() function.

import zoo as menagerie
menagerie.hours()