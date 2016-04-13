#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0


###########################################
##                                       ##
##  Author: Sravanthi Kandukuri          ##
##                                       ##   
###########################################


## WORDCOUNT.PY


import sys

# +++your code here+++
# Define print_words(filename) and print_top(filename) functions.
# You could write a helper utility function that reads a file
# and builds and returns a word/count dict for it.
# Then print_words() and print_top() can just call the utility function.

###

# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.

"""
For the --count flag, implement a print_words(filename) function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2



def print_words(s):
    f = open(s,'rU')
    list_word1=[]
    a ={}
    count=0
    for line in f:
        #print ('line:',line)
        for x in line.split(' '):
            #print('x :',x)
                if x is '\n':
                    continue
                else:
                    if x in a.keys():
                        a[x]=a[x]+1
                    else :
                        a[x]=1
             
    for k,v in a.items(): print(k,'> :',v)
                  
    return

'''
            if x in a.keys():
                a[x].value()=a[x].value+1
            else:
                a[x]=1
                '''
        

    

# End Print words


2. For the --topcount flag, implement a print_top(filename) which is similar
to print_words() but which prints just the top 20 most common words sorted
so the most common word is first, then the next most common, and so on.

Use str.split() (no arguments) to split on all whitespace.


def print_top(s):
    
    f = open(s,'rU')
    list_word1=[]
    a ={}
    count=0
    for line in f:
        #print ('line:',line)
        for x in line.split(' '):
            #print('x :',x)
                if x is '\n':
                    continue
                else:
                    if x in a.keys():
                        a[x]=a[x]+1
                    else :
                        a[x]=1
             
    for k,v in sorted(a.items()):
        if (count<20 and v>1):
                print(k ,' : ',v)
                
    return

# End Print top

"""


def read_file(f):
    s = open(f,'rU')
    list_word1=[]
    a ={}
    count=0
    for line in s:
        #print ('line:',line)
        for x in line.split(' '):
            #print('x :',x)
                if x is '\n':
                    continue
                else:
                    if x in a.keys():
                        a[x]=a[x]+1
                    else :
                        a[x]=1
    #print('a :', a)
    return(a)


def print_words(s):
    a=read_file(s)
    print('a :',a)

    for k,v in a.items(): print(k,'> :',v)
       
    return(a)


def print_top(s):
    dict=read_file(s)
    count=0
    for k,v in sorted(dict.items()):
        if (count<20 and v>1):
            print(k ,' : ',v)
    return


def main():
  if len(sys.argv) != 3:
    print ('usage: ./wordcount.py {--count | --topcount} file')
    sys.exit(1)

  option = sys.argv[1]
  filename = sys.argv[2]
  if option == '--count':
    print_words(filename)
  elif option == '--topcount':
    print_top(filename)
  else:
    print ('unknown option: ', + option)
    sys.exit(1)

if __name__ == '__main__':
  main()
