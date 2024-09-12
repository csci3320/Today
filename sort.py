l = [1,9,2,8,3,7,4,6,5]

def bubble_sort(original_list):
  list = original_list.copy()
  for i in range(len(list)):
    for index in range(i, len(list)-1):
      if list[index] > list[index+1]:
        temp = list[index]
        list[index] = list[index+1]
        list[index+1] = temp
  return list

def selection_sort(original_list):
  list = original_list.copy()
  for i in range(len(list)):
    smallest = 10000
    smallest_index = -1
    for index in range(i, len(list)):
      if list[index] < smallest:
        smallest = list[index]
        smallest_index = index
    temp = list[i]
    list[i] = smallest
    list[smallest_index] = temp
  return list

def insertion_sort(original_list):
  list = original_list.copy()
  for i in range(1,len(list)):
    index = i
    while index > 0:
      if list[index] < list[index-1]:
        temp = list[index]
        list[index] = list[index-1]
        list[index-1] = temp
        index -= 1
      else:
        break
  return list

def merge_sort(original_list):
  list = original_list.copy()
  return merge_sort_recursive(list)


def merge_sort_recursive(list):
  if(len(list) <= 1):
    return list
  
  middle = len(list)//2
  first_half = merge_sort_recursive(list[:middle])
  second_half = merge_sort_recursive(list[middle:])
  
  final = []
  
  while first_half and second_half:
    if first_half[0] < second_half[0]:
      final.append(first_half.pop(0))
    else:
      final.append(second_half.pop(0))

  while first_half and not second_half:
    final.append(first_half.pop(0))
  while not first_half and second_half:
    final.append(second_half.pop(0))
  
  return final
    

print(bubble_sort(l))
print(selection_sort(l))
print(insertion_sort(l))
print(merge_sort(l))