list = [1,2,3,4,5,6,7,8,9]


def find_for_loop(search_for):
    for index in range(len(list)): #Starting Condition, Change (Increment),  Stopping Condition, and Loop in one
        if list[index] == search_for: return True # Body
    return False   

def find_while(search_for):
    index = 0 # Starting Condition
    while index < len(list): # Stopping Condition and Loop
        if list[index] == search_for: return True # Body
        index += 1 # Change (Increment)
    return False


def find_recursive(search_for):
    return find_recursive_loop(search_for, 0) #Starting Condition

def find_recursive_loop(search_for, index):
    if index < len(list): # Stopping Condition
        if list[index] == search_for: return True #Body
        index += 1 # Change (Increment)
        return find_recursive_loop(search_for, index) # Loop
    else:
        return False
         

print(find_for_loop(8))
print(find_while(8))
print(find_recursive(8))
