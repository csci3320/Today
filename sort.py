l = [1,9,2,8,3,7,4,6,5,10,12,11]

def bubble_sort(original_list):
  # Copy the list so we don't mutate it
  # This allows future sorting functions to still use the original list
  list = original_list.copy()

  for i in range(len(list)):
    # Loop over the unsorted part of the list
    # and flip values in the list that are in the wrong order
    
    # Note we go to len(list)-1 since we call index+1
    # If we failed to do this, we would get an index 
    # out of bounds error
    for index in range(i, len(list)-1):
      # If the value at index is greater than the following value
      # i.e. the values are not in the right order...
      if list[index] > list[index+1]:
        # ... then flip them 
        temp = list[index]
        list[index] = list[index+1]
        list[index+1] = temp
  return list

def selection_sort(original_list):
  list = original_list.copy()

  for i in range(len(list)):
    # Go through and find the smallest value in the unsorted part of the list

    smallest = 1000 # A number that is bigger than anything we will put in this example
    smallest_index = -1

    for index in range(i, len(list)):
      # If we find a smaller number...
      if list[index] < smallest:
        # ... then update our smallest to this number
        smallest = list[index]
        smallest_index = index

    # Once we are done searching, we can swap it with the first value in 
    # the unsorted part of the list
    temp = list[i]
    list[i] = smallest
    list[smallest_index] = temp
  return list

def insertion_sort(original_list):
  list = original_list.copy()

  # Take the first value in the unsorted part of the list
  # and move it left until it is in the right place
  for i in range(1,len(list)):
    index = i

    # Move left until we find the right place for our number
    while index > 0:
      # If the number in question is smaller than the number to the left...
      if list[index] < list[index-1]:
        # ... then swap positions
        temp = list[index]
        list[index] = list[index-1]
        list[index-1] = temp
        index -= 1
      else:
        # ... otherwise we are in the right place, so we can stop
        break
  return list

def merge_sort(original_list):
  list = original_list.copy()
  # As a best practice, call a separate recursive function
  return merge_sort_recursive(list)


def merge_sort_recursive(list):
  # Stop if we have a list of length one or an empty list
  if(len(list) <= 1):
    return list
  
  # Find the middle index of the list
  middle = len(list)//2

  # Recursively sort the first and second halfs
  first_half = merge_sort_recursive(list[:middle])
  second_half = merge_sort_recursive(list[middle:])
  
  #When we get here, we know both first_half and second_half are sorted

  # final holds the list that we will return.
  final = []
  
  # While two non-empty lists, add the lower of their first values
  while first_half and second_half:
    if first_half[0] < second_half[0]:
      final.append(first_half.pop(0))
    else:
      final.append(second_half.pop(0))

  # If we get here, at least one of our lists is empty.
  # So we can just append the remaining values in each list
  while first_half:
    final.append(first_half.pop(0))
  while second_half:
    final.append(second_half.pop(0))
  
  return final
    

print(bubble_sort(l))
print(selection_sort(l))
print(insertion_sort(l))
print(merge_sort(l))