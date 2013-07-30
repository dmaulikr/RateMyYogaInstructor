#!/usr/bin/env python

'''
  this script does not generate the given json
  json was modified using manual bash/text manipulation

  add keyID variable that generates randon string for the key of yogaInstructor
'''

import json, sys, string, random

def jsonTheYogaGirls():
  data           =  open("data.txt", "r")
  output         = open("data_after_python.txt", 'w+')
  yogaData       = []
  yogaInstructor = {}
  firstName      = {}
  lastName       = {}
  city           = {}
  state          = {}
  country        = {}
  count_line     = 0


  for line in data:
    if len(line) == 2:
      keyID = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(20))
      yogaInstructor[keyID] = firstName, lastName, city, state, country
      yogaData.append(yogaInstructor)

      yogaInstructor = dict()
      firstName      = dict()
      lastName       = dict()
      city           = dict()
      state          = dict()
      country        = dict()
      count_line     = 0
    else:
      if count_line == 0:
        key = 'firstName'
        value = line
        firstName[key] = value
      if count_line == 1:
        key = 'lastName'
        value = line
        lastName[key] = value
      if count_line == 2:
        key = 'city'
        value = line
        city[key] = value
      if count_line == 3:
        key = 'state'
        value = line
        state[key] = value
      if count_line == 4:
        key = 'country'
        value = line
        country[key] = value

      count_line += 1

  for i in yogaData:
    print i

  output.writelines(["%s" % i for i in yogaData])
    

jsonTheYogaGirls()


