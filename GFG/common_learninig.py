# Indentation in python 
# python variables
    # no need to declare the variable types var,const,
    # cannot start with digit .
    # case sensitive (myvar and MyVar both are different)
    # x,y,z=1,2,3
    # basic casting functionlities are int(),float(),str()
    # to get the type fo variable type()
    # to use the global variable inside funciton use global syntax

# Keywords in python are(to get the keywords use import keyword and do keyword.kwlist)
    # False,await,else,import,pass,None,break,except,in,raise,True,class,finally,is,return,and,continue,for,lambda,try,as,def,from,nonlocal,while,assert,del,global,not,with,async,elif,if,or,yield
    # lambda is an anonomys function
# to Take input from user 
    # input(),input().split( or , or :s),int(input('Enter your number:'))
    # list(input('enter your name')) -- 12345 --output -- [1,2,3,4,5]
    # map(int,input.split())--map method used to converts each of elements in list to integers

    # faster method to read the input is stdin,stdout--from sys import stdin,stdout
    # to read input stdin.readline(),to print the ourput stdin.write()
# to print the output 
    # print()
    # using sep and end parameters in the output (print('test',end="$") print('teee')) - -output--testtee
    # print('t','a','t',sep="-") --- output=t-a-t
    # using variable print(f"this si my {name}")
    # print("{0} and Portal".format("Geeks"))


# Data types
#  string -- we can access as character from the list in s[0],s+s[0]
    # s[::-]reverses a string
    # you cannot change a string character at a particular line thorug index
    # methods are
    # --replace(new_relplace_word,string_word).
    # --len(word) -- will return the length of the string.
    # --upper() and lower()--you know.
    # -string()--will remove the empty spaces across the word.
    # --for concatenating use +.for repeating using *
    # -in printing the output use formatting
    # separator.join(list of strings)--to join the array of words into a astring.

# Lists -- [] --list(can be a tuple,string or list)--
    # -can contain duplicate items.these are mutable items.--ordered of how they are added.
# --operations
    # append()--adds element at the end of the list
    # extend--multiple elements adding at the end of the list
    # iterable.insert(index,item)---adds elements at specific positon.
    # iteratble.remove(item to remove) -- removes the first occurance of element
    # iteratble.pop(index)--removes at specific index or last element if no index is spcified--will returned the pop val
    # del statement--deletes an entire specified index -- a[0]
    # looping through list --for item in list:
    #to read the input -- list(map(int,input('enter.number').split('')))--
    # to find the length of the list -- len()
    # list comprehensions are [print(1) for i in a]--not good as it createa additional space

    # list sorting techniques are
    #   sorted(a, key=len)=sorted() function creates a new list without modifying the original.
    # a.sort(key=len)--changes the original lsit
    #   sorted(a, key=len, reverse=True)


# Tuple-() -tuple(list,string,tuple)--()
    # ---mixed data types.ordered list--immutable collection of list
    # we generally use ‘tuples’ for heterogeneous (different) data types and ‘lists’ for homogeneous (similar) data types.
    # We can access the tuple data by using indexing or slicing (::)
    # concatenation of tuples will be done by "+".

# Sets-{} -- {},set()
    # in Set the order of elements is not quaranteed by the same order in which they added.
    # for adding add(element) --for removing--remove(element)
    # we cannot use the set to index 


