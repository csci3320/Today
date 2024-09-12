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
  first_half = list[:middle]
  second_half=list[middle:]
  print(first_half)
  print(second_half)
  first_half = merge_sort_recursive(first_half)
  second_half = merge_sort_recursive(second_half)
  final = []
  while len(first_half) > 0 and len(second_half) > 0:
    if first_half[0] < second_half[0]:
      item = first_half.pop(0)
      final.append(item)
    else:
      item = second_half.pop(0)
      final.append(item)

  while len(first_half) > 0 and len(second_half) == 0:
    item = first_half.pop(0)
    final.append(item)
  while len(second_half) > 0 and len(first_half) == 0:
    item = second_half.pop(0)
    final.append(item)
  
  return final
    

# print(bubble_sort(l))
# print(selection_sort(l))
# print(insertion_sort(l))
print(merge_sort(l))