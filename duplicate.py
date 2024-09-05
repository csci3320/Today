import sys

list = [1,2,3,4,1]
list2 = [1,2,3,4,5,6,7,8,9]

# sort + compare each number to the one next
# create an array of bins
# Double for for 

def double_for(list):
    count = 0
    for index in range(len(list)):
        for second_index in range(index+1, len(list)):
            count += 1
            if index != second_index:
                if list[index] == list[second_index]:
                    return True
    print(count)
    return False

def bin(list):
    #print(sys.maxsize)
    count = 0
    list_of_bins = []
    for i in range(10):
        count += 1
        list_of_bins.append(0)
    for i in list:
        count += 1
        list_of_bins[i] += 1
    for i in range(10):
        count += 1
        if list_of_bins[i] > 1:
            return True
    print(count)
    return False

print(double_for(list))
print(double_for(list2))

print(bin(list))
print(bin(list2))
