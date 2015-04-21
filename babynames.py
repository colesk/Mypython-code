#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""


"""
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
 
'''  for line in f:
    match = re.search(r'Popularity\s\in\s\d\d\d\d',line)
    if match:
      year_string=match.group()
      #print('year_string :',year_string)
      final_year=re.search(r'\d\d\d\d',year_string)
      print(final_year.group())'''

def extract_names(filename):
  f = open(filename,'rU')
  text=f.read()
  output=[] #output is a list
  name_rank={}
  key=0
  value=0
  tuples=() # Gets three words
  '''
    year = re.search(r'Popularity\s\in\s\d\d\d\d',text)
    if year:
      year_string=year.group()
      final_year=re.search(r'\d\d\d\d',year_string)
      #name_rank[0]=final_year.group()
      output.append(final_year)

      print ('output':output)'''
    
  tuples=re.split(r'<td>.*</td>',text)

  print('tuples',tuples)
      
  '''name_to_rank={}
      
  for rank_tuple in tuples:
    (rank,boyname,girlname)=rank_tuple
    if boy_name not in name_of_rank:
      names_to_rank[boyname]=rank
    if girl_name not in name_of_rank:
      names_to_rank[girlname]=rank
    print(' name_to_rank :', name_to_rank)
    sorted_names= sorted(name_to_rank.keys())
    for name in sorted_names:
      names.append(name + " " + name_to_rank[name])


    return names'''

      
      '''
        #extract_name=re.search(r'<td>.+<\td>',line)
        #if extract_name:
        #print('in extract_name')
        rank_female_male=match.group()
        #print('names:',rank_female_male)
        list=rank_female_male.split('</td>')
        #print('list:',list)
        for k in list:
          rank=re.search(r'\d+',k)
          if rank:
            key=rank.group()
            #print('key:',key)
           
          else:
            name=re.search(r'\w+$',k)
            if name:
              #print('checking digit',name.group())
               value=name.group()
               name_rank[value]=key'''

  
 # print('pair of names and ranks', name_rank)
  return


def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  if not args:
    print( 'usage: [--summaryfile] file [file ...]')
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]
    extract_names(args[0]) 
 
  
if __name__ == '__main__':
  main()
