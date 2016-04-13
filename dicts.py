#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0


###########################################
##                                       ##
##  Author: Sravanthi Kandukuri          ##
##                                       ##   
###########################################


## SCRIPT : PLAYING WITH DICTS

dict = {}

dict['a']= 'Dr. Suess ABC'
dict['b']= 'Play with Ball'
dict['c']=  'Catch a Fly'
dict['d']='Doll in the toy chest'

print (dict)

print (dict['a'])

dict['a']=6

print (dict['a'],"\n")



print (dict)

print (dict.get('z'))

