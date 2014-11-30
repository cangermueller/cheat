#!/usr/bin/python

import sys



def convert(val):
  try:
    print ' '.join(val)
  except TypeError, msg:
    print 'Error occurred: ', msg
  else:
    print 'ok'

def open_file(filename):
  try:
    file = open(filename)
    print 'File opened!'
  except IOError:
    sys.stderr.write('Error opening {:s}!\n'.format(filename))
  else:
    file.close()
    print 'File closed!'
  print 'Done!'



class StringError(RuntimeError):
  def __init__(self, msg):
    self.msg = msg

  def __str__(self):
    return self.msg


def self_defined(i):
  values = [1, 2, 3]
  try:
    if i == 0:
      raise StringError('Unknown error')
    else:
      print values[i]
  except StringError, arg:
    print arg
  except IndexError:
    print 'Index out of range'
  else:
    print 'No error'

a = 1
b = 2
c = a + b
print c
a = 'aa'a
1 = 1


