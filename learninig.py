# import sys
# print(sys.version)
"""
if(5>2):
    print('testing')
    """

# casting of variables
# x=5
# y=10
# x1=int(5)->5
# x2=str(5)->'5'

# to get the type of the function 
# print(type(x))

# case sensitive
# x=5
# X='tesitng'
# print(x,X)

# camel_case  myVaraiblName
# pascal_case MyVariableName
# snake_case my_variable_name

# single line values assigning are 
# x,y,z = 1,2,3
# unpacking a collection will be 
# x,y,z =['testi','tee','teet']

# global keyword will delcare any variable as global

# datatypes in python are

# str --text type
# int,float,complex(ij) -- Numeric
# list(['1',2]),tuple((1,2)),range(range(9))--sequence types
# dict{'':''} --mapping
# set({'as','asd'}),frozenset(frozenset({'sad','asd'})) -- set
# bool--boolean
# bytes(b"hel"),bytearray(bytearray(5)),memoryview(bytes(4))--binarytypes

# import random
# print(random.randrange(1,10))


# Strings
# Looping thorugh strings ,access first letter of string
# for x in "Ganesh":
#     print(x)
# to get the length of string --len()
# check string exists ('test' in 'Ganesh')
# in ,not in
#  
# slicing of strings are 
# v = 'ganesh is Good boy'
# print(v[2:5]) =2 to 5
# print(v[:4]) until 4 index
# v[-3:-10] revers 3rd index to 10gh index

# modifying strings are 
# a.upper(),a.lower(),
# a.strip()-removes the white space
# a.replace('3',4) -replaces charactedor string/
# a.split(,)split the character into based on variable
# contact strings  a+c
# joining strings with numbers will be 
# a=6
# f"testing {a}"


# operattors of different types
# arthimetic operatos(+,-),assignment operators(=+),comparisoon Operatos(==,!=),locical operators(and,or),membership operators(in,not in),
# bitwise operatoss(&,|)


# Lists --
# these items are ordered,changable,allow duplicate values 
# len(list);
# a list can contain different data types
# list(('test')) here list( ) is a constructor

# collections data types are of 4 types --list,set,typle and disctorinary
# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members. --do add /remove
# Dictionary is a collection which is ordered** and changeable. No duplicate members.



# thislist = ["apple", "banana", "cherry"]
# thislist[1:2] = ["blackcurrant", "watermelon"]
# outout ==['apple','blackcurrant','cherry','watermelon']

# list.insert(2,'test')
# list.append()./will add at the end
# list.extend(anothelist) will make new list od list
# list.extend(typle) --will add into list
# list.remove(item)
# list.pop(index) -if no index it will pop tghe last index
# del list[index]
# list.clear()will clear the list


# for x in lists:
# for x in range(len(list)):
# while a
# [print(x) for x in list]
# list compresntions are   new_list = [expression for item in list if condition=true ]

# sorting lists will be list.sort()
# list.sort(reverse=true)
# list.revers()
 
#  copy(),list(),list[:] --will do copy of list into new variable

# to update a tuple convert it into a list using list() casting and do reverse reverse casting
# (1,2,*3) = tuple it will do assign 3 all the reminig tuple items
# tuple methods are index(),count()

