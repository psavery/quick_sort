#!/usr/bin/env python

import random
import time
import copy

# Start is the index of the starting position. Finish is the index of the
# ending position
def quicksort(my_list, start, finish):
  assert type(start) is int, "Starting index must be an integer."
  assert type(finish) is int, "Ending index must be an integer."
  assert finish > start, "Ending index must be greater than starting index."
  assert type(my_list) is list, "List parameter must be a list."
  # comparisonIndex keeps track of which position contains the item we
  # are currently comparing with the rightmost item.
  # swapIndex keeps track of the position that needs to be swapped
  # swapIndex basically forces all numbers that are less than the number at
  # the ending index to be moved to the far left side
  comparisonIndex = start
  swapIndex = start

  # Loop through every item and compare them with the one on the far right.
  # If any items are less than the one on the right, place that item on the left
  # All items greater than the left side items will be on the right
  while comparisonIndex != finish:
    if my_list[comparisonIndex] <= my_list[finish]:
      my_list[comparisonIndex], my_list[swapIndex] = \
        my_list[swapIndex], my_list[comparisonIndex]
      # Only add 1 to the swap index if an item is swapped
      swapIndex += 1
    # Add 1 to the comparison index after every iteration of the loop
    comparisonIndex += 1
  # Swap the item on the far right with the left-most item that is greater
  # than it.
  my_list[swapIndex], my_list[finish] = my_list[finish], my_list[swapIndex]

  # We assume that the right-most item, after being moved as it was in the
  # previous line, is in the exact correct position and does not need to be
  # moved anymore. Thus, we will only perform quicksort on the side to the
  # left and to the right of it (without including it). It's current position
  # is at swapIndex
  if start < swapIndex - 1:
    quicksort(my_list, start, swapIndex - 1)

  if swapIndex + 1 < finish:
    quicksort(my_list, swapIndex + 1, finish)
  # End of function

listLength = 0
firstNumber = 0
lastNumber = 0
errorMessage = "Invalid number entered. Please try again.\n"

while True:
  listLength = raw_input(str("\nEnter the length of the list of random " +
                             "numbers to be generated.\n"))
  if listLength.isdigit():
    listLength = int(listLength)
    break
  else:
    print errorMessage

while True:
  firstNumber = raw_input(str("\nEnter the smallest number in the range of " +
                              "random numbers to be generated.\n"))
  if firstNumber.isdigit():
    firstNumber = int(firstNumber)
    break
  else:
    print errorMessage

while True:
  lastNumber = raw_input(str("\nEnter the largest number in the range of " +
                             "random numbers to be generated.\n"))
  if lastNumber.isdigit():
    lastNumber = int(lastNumber)
    break
  else:
    print errorMessage

print "\nGenerating a list of random numbers of length " , listLength, ", "
print "with numbers between ", firstNumber, " and " , lastNumber , ".\n"

randList1 = []
for i in range(0,listLength):
  randList1.append(random.randrange(firstNumber, lastNumber))

# We need to do a deepcopy here because randList1 will be edited and sorted.
# In order to do the future tests, we need the original unsorted randList
randList2 = copy.deepcopy(randList1)
randList3 = copy.deepcopy(randList1)

# Write an output file that contains the unsorted and sorted lists
my_file = open("generatedLists.txt", "w")

banner = "=================================================================\n"

my_file.write(banner)
my_file.write("randList unsorted is:\n")
my_file.write(banner)

for item in randList1:
  my_file.write("%s\n" % item)

print "Beginning nested loop sort...\n"
startTime = time.clock()

for i in range(len(randList1) - 1):
  for j in range(i + 1, len(randList1)):
    if randList1[i] > randList1[j]:
      randList1[i], randList1[j] = randList1[j], randList1[i]

endTime = time.clock()
print "Total elapsed nested-loop time is: %.3fs" % (endTime - startTime) , "\n"

my_file.write(banner)
my_file.write("randList after nested loop sorting is:\n")
my_file.write(banner)

for item in randList1:
  my_file.write("%s\n" % item)

print "Beginning quicksort...\n"
startTime = time.clock()

# First, we'll pick a random number to put at the end...
randomIndex = random.randrange(0, len(randList1) - 1)

# Now, we'll move that random number to the end of the list
randList2[randomIndex], randList2[len(randList2) - 1] = \
  randList2[len(randList1) - 1], randList2[randomIndex]

# Now, we will begin the sorting
quicksort(randList2, 0, len(randList2) - 1)

endTime = time.clock()
print "Total elapsed quicksort time is: %.3fs" % (endTime - startTime) , "\n"

my_file.write(banner)
my_file.write("randList after quicksort sorting is:\n")
my_file.write(banner)

for item in randList2:
  my_file.write("%s\n" % item)


startTime = time.clock()

randList3 = randList3.sort()

endTime = time.clock()
print "Total elapsed built-in Python sorter is: %.3fs" % (endTime - startTime) \
  , "\n"
