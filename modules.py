import sys
import re
import time
import collections

# sys.path: info about the local system
print(sys.path)

# re.findall: finds all numbers in the given text
text = 'My phone number is (311) 123 121, the dialing code is 1 and my favorite number is 3'
result = re.findall('[0-9]+', text)
print(result)

# time.time: gives the time
timestamp = time.time()
# Machine time
print(timestamp)

local = time.localtime()
result = time.asctime(local)
# Human readable time
print(result)

# collections.counter: counts the number of times a number was found in the list
numbers = [1, 1, 2, 1, 2, 1, 4, 5, 3, 3, 21]
counter = collections.Counter(numbers)
print(counter)
