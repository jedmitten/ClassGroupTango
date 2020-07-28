"""
This program will read a file (default names.txt) and 
will shuffle the lines to create groups of some size that
you specify by updating the make_groups 'group_size' 
value (default 4)
"""
import random

def read_and_shuffle_names(filename="names.txt"):
  """
  Read a file and shuffle the lines that do not start with 
  a '#'. These are assumed to be names of classroom 
  participants. 
  """
  with open(filename) as f:
    names = [l.strip() for l in f.readlines() if l.strip()[0] != '#']

  random.shuffle(names)
  return names

def make_groups(lst, group_size=4):
  """
  Yield successive group_size-sized chunks from lst.
  """
  for i in range(0, len(lst), group_size):
      yield lst[i:i + group_size]

def print_groups(groups):
  """
  Given a list of lists (groups), format the output of
  those groups
  """
  group_num = 0
  
  for group in groups:
    print("Group {}".format(group_num + 1))
    for name in group:
      print("* {}".format(name))
    
    group_num += 1

    print()

# get the groups
shuffled_group_names = list(make_groups(read_and_shuffle_names('names.txt'), group_size=4))

# print the groups
print_groups(shuffled_group_names)
